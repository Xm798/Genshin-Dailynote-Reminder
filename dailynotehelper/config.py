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
            print('配置文件读取错误，请检查 ./dailynotehelper/config/config.yaml 是否存在且可读。')
            exit()
        else:
            self.config_dict = yaml.load(f,Loader=yaml.FullLoader)

    def get_config(self):
        for key in self.config_dict:
            k = key
            for key in self.config_dict[k]:
                self.config_data[key] = self.config_dict[k][key] if self.config_dict[k][key] else ''

    def parse_config(self):
        self.config_data = {}
        self.get_config()
        return ConfigData.parse_obj(self.config_data)

config = Config().parse_config()