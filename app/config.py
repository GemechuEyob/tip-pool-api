import collections
import configparser
import os

from pydantic import BaseModel

env = os.getenv("ENV", "qa")


class Config(BaseModel):
    log_level: str = "INFO"


config_parser = configparser.RawConfigParser()
config_file_path = f"config/{env}.cfg"
config_parser.read(config_file_path)


def get_config_section():
    if not hasattr(get_config_section, "section_dict"):
        get_config_section.section_dict = collections.defaultdict()

        for section in config_parser.sections():
            get_config_section.section_dict[section] = dict(
                config_parser.items(section)
            )

    return get_config_section.section_dict


val = Config(**get_config_section()["core"])
