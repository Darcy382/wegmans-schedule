from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


class Calendar:
    def __init__(self):
        """Shows basic usage of the Google Calendar API.
                Prints the start and name of the next 10 events on the user's calendar.
                """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

        self.gmt_off = '-04:00'

    def create_event(self, title, start, hours):
        str_start = start.strftime('%Y-%m-%dT%H:%M:00')
        delta = datetime.timedelta(hours=hours)
        end = start + delta
        str_end = end.strftime('%Y-%m-%dT%H:%M:00')
        event = {
            'summary': title,
            'start': {'dateTime': str_start + '%s' % self.gmt_off},
            'end': {'dateTime': str_end + '%s' % self.gmt_off}
        }
        e = self.service.events().insert(calendarId='primary', body=event).execute()
        print(e)




#cal = Calendar()
#cal.create_event('FE Managment', datetime.datetime(2019, 7, 19, 13), 5)
