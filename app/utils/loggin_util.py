"""
Logging for application
"""
import logging


def configure_logging(name):
    """ Configure logging with file path """
    root = logging.getLogger(name)
    root.setLevel(logging.INFO)
    default_format = '%(levelname)s:Lucho404Diaz:%(name)s: %(message)s'
    formatter = logging.Formatter(default_format)
    default_handler = logging.StreamHandler()
    default_handler.setFormatter(formatter)
    root.addHandler(default_handler)
    root.propagate = False
    return root
