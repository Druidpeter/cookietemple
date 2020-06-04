from pathlib import Path
from ruamel.yaml import YAML


def load_yaml_file(yaml_file_path: str) -> dict:
    """
    Loads a yaml file and returns the content as nested dictionary.

    :return: nested dictionary as the content of the yaml file
    """
    path = Path(yaml_file_path)
    yaml = YAML(typ='safe')
    return yaml.load(path)
