from app.models.enums.header_enum import HeaderEnum
from app.utils.loggin_util import configure_logging
from instascrape import Reel
LOGGER = configure_logging('ReelsApp:')


class ReelsApp:
    """Main class in the app"""
    @staticmethod
    def start_application():
        LOGGER.info('[start_application] <Start application>')
        ReelsApp.download_reel()

    @staticmethod
    def generate_headers():
        session_id = '704007794'
        user_agent = HeaderEnum.USER_AGENT.value
        cookie = HeaderEnum.COOKIE.value
        return {
            user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
            Safari/537.36 Edg/79.0.309.43",
            cookie: f'sessionid={session_id};'
        }

    @staticmethod
    def download_reel():
        name_reel = 'pythonTest'
        url_reel = 'https://www.instagram.com/reel/CVVVm0OBFeA/'
        LOGGER.info('[download_reel] <Init Download reel > %s ', name_reel)
        headers_for_request = ReelsApp.generate_headers()
        LOGGER.info('[download_reel] <Headers for request:   %s >', headers_for_request)
        me_reel = Reel(url_reel)
        me_reel.scrape(headers=headers_for_request)
        me_reel.download(fp=f"reels/{name_reel}.mp4")
        LOGGER.info('[download_reel] <FINISH PROCESS>')




