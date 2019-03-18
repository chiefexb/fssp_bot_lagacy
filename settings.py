import pathlib
import yaml
from yaml import load, dump
from yaml import Loader, Dumper

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'bot.yaml'

def get_config(path):
    stream = open(path, 'r')
    return load(stream, Loader=Loader) 

config = get_config(config_path)
