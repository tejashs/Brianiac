import os
script_dir = os.path.dirname(__file__)
config_params_path = "params.config"
flower_category_file_path = "flower_categories.txt"


HOSTNAME='HOSTNAME'
PORT='PORT'
USER='USER'
PASSWORD='PASSWORD'

NUMBER_SCHEMA='NUMBER_SCHEMA'
NUMBER_DETAILS_TABLE='NUMBER_DETAILS_TABLE'
FLOWER_SCHEMA='FLOWER_SCHEMA'
FLOWER_DETAILS_TABLE='FLOWER_DETAILS_TABLE'

def getParamsFromFile(abs_file_path):
    with open(abs_file_path) as f:
       lines = list(f)
    params = {}
    for l in lines:
        l = l.rstrip("\r\n")
        entry = l.split('=')
        params[str(entry[0])] = str(entry[1])
    return params

def get_hana_config_params():
    path = os.path.join(script_dir, config_params_path)
    return getParamsFromFile(path)


def get_flower_params():
    path = os.path.join(script_dir, flower_category_file_path)
    return getParamsFromFile(path)
