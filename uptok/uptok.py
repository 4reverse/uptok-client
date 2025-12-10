from typing import Dict, Any

from uptok.http import UPTokHTTP


class UPTok:

    def __init__(
            self,
            key: str,
            base_url: str = "https://api.uptok.ru",
    ) -> None:
        self.http = UPTokHTTP(key=key, base_url=base_url)

    def get_user_id(
            self,
            username: str
    ) -> Dict[str, Any]:
        """
        Get user id
        :param username: TikTok username
        :return: json
        """
        return self.http.get(f"/user/{username}/id")

    def get_user(
            self,
            user_id: str
    ) -> Dict[str, Any]:
        """
        Get user by user id
        :param user_id: sec_user_id or user_id
        :return: json
        """
        return self.http.get(f"/user/{user_id}/info")

    def get_user_followers(
            self,
            user_id: str,
            count: int = 10,
            offset: int = 0,
            page_token: str = "",
    ) -> Dict[str, Any]:
        """
        Get user followers
        :param user_id: sec_user_id or user_id
        :param count: followers per page
        :param offset: if 'has_more' in response -> use 'min_time' as offset
        :param page_token: if 'has_more' in response -> use 'next_page_token'
        :return: json
        """
        params = {
            "count": count,
            "offset": offset,
            "page_token": page_token
        }
        return self.http.get(f"/user/{user_id}/followers", params=params)

    def get_user_following(
            self,
            user_id: str,
            count: int = 10,
            offset: int = 0,
            page_token: str = "",
    ) -> Dict[str, Any]:
        """
        Get user following
        :param user_id: sec_user_id or user_id
        :param count: following per page
        :param offset: if 'has_more' in response -> use 'min_time' as offset for next request
        :param page_token: if 'has_more' in response -> use 'next_page_token' for next request
        :return: json
        """
        params = {
            "count": count,
            "offset": offset,
            "page_token": page_token
        }
        return self.http.get(f"/user/{user_id}/following", params=params)

    def get_user_videos(
            self,
            user_id: str,
            count: int = 10,
            offset: int = 0,
    ) -> Dict[str, Any]:
        """
        Get user followers
        :param user_id: sec_user_id or user_id
        :param count: video per page
        :param offset: if 'has_more' in response -> use 'cursor' as offset for next request
        :return: json
        """
        params = {
            "count": count,
            "offset": offset
        }
        return self.http.get(f"/user/{user_id}/videos", params=params)

    def search_user_by_keyword(
            self,
            keyword: str,
            count: int = 10,
            offset: int = 0
    ) -> Dict[str, Any]:
        """
        Search users by keyword
        :param keyword: text for search
        :param count: users per page
        :param offset: if 'has_more' in response -> use 'cursor' as offset for next request
        :return: json
        """
        params = {
            "keyword": keyword,
            "count": count,
            "offset": offset
        }
        return self.http.get(f"/search/user", params=params)

    def search_video_by_keyword(
            self,
            keyword: str,
            count: int = 10,
            offset: int = 0
    ) -> Dict[str, Any]:
        """
        Search videos by keyword
        :param keyword: text for search
        :param count: videos per page
        :param offset: if 'has_more' in response -> use 'cursor' as offset for next request
        :return: json
        """
        params = {
            "keyword": keyword,
            "count": count,
            "offset": offset
        }
        return self.http.get(f"/search/video", params=params)

    def search_music_by_keyword(
            self,
            keyword: str,
            count: int = 10,
            offset: int = 0
    ) -> Dict[str, Any]:
        """
        Search musics by keyword
        :param keyword: text for search
        :param count: musics per page
        :param offset: if 'has_more' in response -> use 'cursor' as offset for next request
        :return: json
        """
        params = {
            "keyword": keyword,
            "count": count,
            "offset": offset
        }
        return self.http.get(f"/search/music", params=params)

    def search_hashtag_by_keyword(
            self,
            keyword: str,
            count: int = 10,
            offset: int = 0
    ) -> Dict[str, Any]:
        """
        Search hashtags by keyword
        :param keyword: text for search
        :param count: hashtags per page
        :param offset: if 'has_more' in response -> use 'cursor' as offset for next request
        :return: json
        """
        params = {
            "keyword": keyword,
            "count": count,
            "offset": offset
        }
        return self.http.get(f"/search/hashtag", params=params)

    def search_location_by_keyword(
            self,
            keyword: str,
            count: int = 10,
            page: int = 1
    ) -> Dict[str, Any]:
        """
        Search location by keyword
        :param keyword: text for search (ex: London)
        :param count: locations per page
        :param page: 1 and more
        :return: json
        """
        params = {
            "keyword": keyword,
            "count": count,
            "page": page
        }
        return self.http.get(f"/search/location", params=params)

