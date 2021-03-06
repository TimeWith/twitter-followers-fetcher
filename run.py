from lib import utils
from lib.google_client import GoogleSheetsClient
from lib.twitter_client import TwitterClient


def read_user_input():
    """Read user input from the CLI."""
    #
    # User input messages
    #
    first_account_msg = 'Enter a Twitter Account: '
    another_account_msg = 'Enter another account (type \'end\' to finish): '
    spreadsheet_id_msg = 'Enter the Spreadsheet ID: '
    application_name_msg = (
        'Enter your Application name for SpreadSheets API '
        '(Python Twitter Followers): '
    )

    input_data = {}

    twitter_accounts = [raw_input(first_account_msg)]
    another_account = raw_input(another_account_msg)
    while another_account != 'end':
        twitter_accounts.append(another_account)
        another_account = raw_input(another_account_msg)

    input_data['twitter_accounts'] = twitter_accounts
    input_data['spreadsheet_id'] = raw_input(spreadsheet_id_msg)

    application_name = raw_input(application_name_msg)
    input_data['application_name'] = (
        application_name if application_name else 'Python Twitter Followers'
    )
    return input_data


def main():
    """Main function."""
    # Load configuration
    config = utils.read_config()

    # Get input data from user input.
    input_data = read_user_input()
    input_data.update(config)

    # Get data from Twitter API
    twitter_api = TwitterClient({
        'consumer_key': input_data['twitter_consumer_key'],
        'consumer_secret': input_data['twitter_consumer_secret'],
        'access_token_key': input_data['twitter_access_token'],
        'access_token_secret': input_data['twitter_access_token_secret']
    })
    twitter_data = {}
    for handler in input_data['twitter_accounts']:
        print 'Getting Twitter data for account: {}'.format(handler)
        twitter_data[handler] = twitter_api.get_followers(screen_name=handler)

    # Format data for the Google Sheet
    print 'Formatting data to send to Google Sheet API ...'
    formatted_data = []
    for handler in twitter_data:
        for item in twitter_data[handler]:
            formatted_data.append([
                handler,
                item.screen_name,
                item.name,
                item.email
            ])

    # Save data to a Google Sheet
    print 'Saving data to Google Sheet with ID: {}'.format(
        input_data['spreadsheet_id']
    )
    google_api = GoogleSheetsClient({
        'application_name': input_data['application_name'],
        'client_secret_file': input_data['client_secret_file']
    })
    google_api.append_rows(
        input_data['spreadsheet_id'],
        formatted_data,
        range_name='A1:D1'
    )

if __name__ == '__main__':
    main()
