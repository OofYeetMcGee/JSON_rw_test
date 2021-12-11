import json
import pickle


def json_save_conf(lst, file_name):
    with open(file_name, 'w') as conf_file:
        json.dump(lst, conf_file)

    print(f'List dumped to {file_name}')


def json_load_conf(file_name):
    with open(file_name, 'r') as conf_file:
        lst = json.load(conf_file)
        return lst


def pickle_save_conf(lst, file_name):
    # Pickle needs bytes flag
    with open(file_name, 'wb') as conf_file:
        pickle.dump(lst, conf_file)

    print(f'Pickled list to {file_name}')


def pickle_load_conf(file_name):
    with open(file_name, 'rb') as conf_file:
        lst = pickle.load(conf_file)
        return lst


def print_dict_elements(obj):

    for key in obj.keys():
        print(f'{key}: {obj[key]}')


if __name__ == '__main__':

    # Test Config, a list of dictionaries with keys for ID, pan, and tilt values
    pan_tilt_config = [
        {
            'id': 1,
            'pan': 100,
            'tilt': 150,
        },
        {
            'id': 2,
            'pan': 200,
            'tilt': 250,
        },
        {
            'id': 3,
            'pan': 300,
            'tilt': 350,
        },
        {
            'id': 4,
            'pan': 400,
            'tilt': 450,
        },
    ]

    # Save list to JSON and Pickle formats
    json_save_conf(pan_tilt_config, 'conf.json')
    pickle_save_conf(pan_tilt_config, 'conf.pickle')

    # Load config from JSON & print
    pan_tilt_json_loaded = json_load_conf('conf.json')
    print(pan_tilt_json_loaded)

    # Load config from Pickle and print
    pan_tilt_pickle_loaded = pickle_load_conf('conf.pickle')
    # This loop is just for example, the returned object should be the same for JSON or Pickle
    for obj in pan_tilt_pickle_loaded:
        print_dict_elements(obj)

    print(pan_tilt_json_loaded == pan_tilt_pickle_loaded)
