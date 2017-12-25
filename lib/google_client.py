import argparse
import httplib2
import os

from apiclient import discovery
from oauth2client import client, tools
from oauth2client.file import Storage

flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
flags.noauth_local_webserver = True


class GoogleSheetsClient(object):
    """Class to handle communication with the Google Sheets API."""

    def __init__(self, config={}):
        """
        Class constructor.

        Args:
            config -- The API config.
        """
        self.SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
        self.CLIENT_SECRET_FILE = config.get(
            'client_secret_file',
            'client_secret.json'
        )
        self.APPLICATION_NAME = config.get(
            'application_name',
            'Python Twitter Followers'
        )
        self.DISCOVERY_URL = (
            'https://sheets.googleapis.com/$discovery/rest?version=v4'
        )
        self.CREDENTIALS_DIR = '.googleapis-credentials'
        self.CREDENTIALS_FILE = (
            'sheets.googleapis.com-python-twitter-followers.json'
        )

        credentials = self._get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build(
            'sheets',
            'v4',
            http=http,
            discoveryServiceUrl=self.DISCOVERY_URL
        )

    def _get_credentials(self):
        """Get valid user credentials from storage."""
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, self.CREDENTIALS_DIR)
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, self.CREDENTIALS_FILE)

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
                self.CLIENT_SECRET_FILE,
                self.SCOPES
            )
            flow.user_agent = self.APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            print 'Storing credentials to ' + credential_path
        return credentials

    def append_rows(self, spreadsheet_id, rows, range_name='',
                    value_input_option='RAW'):
        """
        Append rows to a specific spreadsheet.

        Args:
            spreadsheet_id -- The id of the spreadsheet to update.
            rows           -- The values to append to the spreadsheet.
        """
        body = {
            'values': rows
        }
        result = self.service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption=value_input_option,
            body=body
        ).execute()

        print '{} rows appended.'.format(
            result.get('updates').get('updatedRows')
        )
