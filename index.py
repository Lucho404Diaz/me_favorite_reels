from app.reels_app import ReelsApp
from app.utils import configure_logging

LOGGER = configure_logging('Main:')


def init_app():
    """Method for init application"""
    LOGGER.info('Welcome to APP')
    ReelsApp.start_application()


if __name__ == "__main__":
    init_app()
