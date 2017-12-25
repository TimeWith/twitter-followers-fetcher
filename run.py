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
        'Enter your Application name (Python Twitter Followers): '
    )
    client_secret_file_msg = (
        'Enter your client_secret filename (client_sercet.json): '
    )
    twitter_consumer_key_msg = 'Enter the Twitter Consumer Key: '
    twitter_consumer_secret_msg = 'Enter the Twitter Consumer Secret: '
    twitter_access_token_msg = 'Enter the Twitter Access Token: '
    twitter_access_token_secret_msg = 'Enter the Twitter Access Token Secret: '

    input_data = {}

    twitter_accounts = [raw_input(first_account_msg)]
    another_account = raw_input(another_account_msg)
    while another_account != 'end':
        twitter_accounts.append(another_account)
        another_account = raw_input(another_account_msg)

    input_data['twitter_consumer_key'] = raw_input(twitter_consumer_key_msg)
    input_data['twitter_consumer_secret'] = raw_input(
        twitter_consumer_secret_msg
    )
    input_data['twitter_access_token'] = raw_input(twitter_access_token_msg)
    input_data['twitter_access_token_secret'] = raw_input(
        twitter_access_token_secret_msg
    )

    input_data['twitter_accounts'] = twitter_accounts
    input_data['spreadsheet_id'] = raw_input(spreadsheet_id_msg)

    application_name = raw_input(application_name_msg)
    input_data['application_name'] = (
        application_name if application_name else 'Python Twitter Followers'
    )

    client_secret_file = raw_input(client_secret_file_msg)
    input_data['client_secret'] = (
        client_secret_file if client_secret_file else 'client_secret.json'
    )
    return input_data


def main():
    """Main function."""
    input_data = read_user_input()

    # Get data from Twitter API
    twitter_api = TwitterClient(
        consumer_key=input_data['twitter_consumer_key'],
        consumer_secret=input_data['twitter_consumer_secret'],
        access_token=input_data['twitter_access_token'],
        access_token_secret=input_data['twitter_access_token_secret']
    )
    data = []
    for handler in input_data['twitter_accounts']:
        data.append(twitter_api.get_followers(screen_name=handler))

    # Format data for the Google Sheet
    formatted_data = [
        ['demo', '123']
    ]

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
        range_name='A1:B1'
    )

if __name__ == '__main__':
    main()
