import yaml
import os
from .getinfo.model.configdata import ConfigData


class Config():
    def __init__(self):
        project_path = os.path.dirname(__file__)
        config_file = os.path.join(project_path, 'config', 'config.yaml')
        try:
            f = open(config_file, 'r', encoding='utf-8')
        except IOError:
            print('Cannot read the configuration file file! Please check if ./dailynotehelper/config/config.yaml exists.')
            exit()
        else:
            self.config_dict = yaml.load(f,Loader=yaml.FullLoader)

    def get_config(self):
        for key in self.config_dict:
            k = key
            for key in self.config_dict[k]:
                if 'COOKIE' in key or 'EXCLUDE_UID' in key:
                    self.config_data[key] = self.config_dict[k][key] if self.config_dict[k][key] else []
                else:
                    self.config_data[key] = self.config_dict[k][key]

    def parse_config(self):
        self.config_data = {}
        self.get_config()
        return ConfigData.parse_obj(self.config_data)

config = Config().parse_config()