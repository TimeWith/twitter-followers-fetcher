import json
import os

CONFIG_FILENAME = 'config.json'
CONFIG_DIR = os.path.abspath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    os.pardir
))


def config_exists():
    """Check if configuration file already exists."""
    return os.path.exists(os.path.join(CONFIG_DIR, CONFIG_FILENAME))


def save_config(config_data):
    """
    Store the configuration to a configuation file.

    Args:
        config_data -- The configuration data dictionary.
    """
    with open(os.path.join(CONFIG_DIR, CONFIG_FILENAME), 'w') as config_file:
        json.dump(config_data, config_file)


def get_config_cli():
    """Get configuration from CLI."""
    twitter_consumer_key_msg = 'Enter the Twitter Consumer Key: '
    twitter_consumer_secret_msg = 'Enter the Twitter Consumer Secret: '
    twitter_access_token_msg = 'Enter the Twitter Access Token: '
    twitter_access_token_secret_msg = 'Enter the Twitter Access Token Secret: '
    client_secret_file_msg = (
        'Enter your client_secret filename (client_sercet.json): '
    )

    config_data = {}

    config_data['twitter_consumer_key'] = raw_input(twitter_consumer_key_msg)
    config_data['twitter_consumer_secret'] = raw_input(
        twitter_consumer_secret_msg
    )
    config_data['twitter_access_token'] = raw_input(twitter_access_token_msg)
    config_data['twitter_access_token_secret'] = raw_input(
        twitter_access_token_secret_msg
    )
    client_secret_file = raw_input(client_secret_file_msg)
    config_data['client_secret_file'] = (
        client_secret_file if client_secret_file else 'client_secret.json'
    )

    return config_data


def read_config():
    """Read configuration from configuration file."""
    config_data = {}
    if config_exists():
        with open(
            os.path.join(CONFIG_DIR, CONFIG_FILENAME), 'r'
        ) as config_file:
            config_data = json.load(config_file)
    else:
        config_data = get_config_cli()
        save_config(config_data)

    return config_data
