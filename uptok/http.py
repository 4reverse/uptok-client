from typing import Dict, Any

from httpx import Client, Response

from uptok.exceptions import RateLimit, PaymentRequired, Unauthorized, AccessDenied, BadRequest


class UPTokHTTP:

    def __init__(
            self,
            base_url: str,
            key: str
    ) -> None:
        self.key = key
        self._http = Client(
            base_url=base_url,
            timeout=10.0
        )

    def get(
            self,
            path: str,
            params: Dict[str, Any] | None = None
    ) -> Dict[str, Any]:
        """Base request for our API service"""
        response = self._http.get(path, params=params, headers=self.headers)
        response_json = self._handle_response(response=response)

        return response_json

    @staticmethod
    def _handle_response(response: Response) -> Dict[str, Any] | None:
        if response.status_code != 200:
            if response.status_code == 401:
                raise Unauthorized("Missing or invalid API key")
            elif response.status_code == 403:
                raise AccessDenied("Invalid API key")
            elif response.status_code == 429:
                raise RateLimit("You have reached the limit of requests per minute")
            elif response.status_code == 402:
                raise PaymentRequired("The quota is exhausted")
            else:
                raise BadRequest(f"Bad request - {response.url} {response.text}")

        response = response.json()

        return response

    @property
    def headers(self) -> Dict[str, str]:
        return {
            "content-type": "application/json",
            "x-api-key": self.key,
        }