import os
import pydantic


class EnvironConstants:
    """
    Class wrapper for environment constants
    """

    PROJECT_PATH: str = pydantic.parse_obj_as(str, os.environ.get('PROJECT_PATH', None))
