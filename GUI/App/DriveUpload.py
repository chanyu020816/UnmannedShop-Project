from __future__ import print_function
from apiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload

def activateService():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret_369303562290-o7pql1tptjpa45skuf6ljlbp908av0qj.apps.googleusercontent.com.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file']


def upload2Drive(service, filename):
    file_metadata = {'name': f'{filename}', 'parents': ['1sjgHIQPuIzNTLtZpZbmTmZJfsELtr8ix']}
    media = MediaFileUpload(f"purchase_images/{filename}.png", mimetype="image/png")
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
