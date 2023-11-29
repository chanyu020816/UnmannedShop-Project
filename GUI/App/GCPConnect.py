from __future__ import print_function
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
from google.cloud import bigquery
from google.oauth2 import service_account

global client
client = None

def activateService():
    SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
              'https://www.googleapis.com/auth/drive.file']

    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES
    )
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

def DBClientConnect():
    global client
    credentials = service_account.Credentials.from_service_account_file('./unmannedshop.json')
    project_id = "unmannedshop"
    client = bigquery.Client(credentials=credentials, project=project_id)



def upload2Drive(service, filename):
    file_metadata = {'name': f'{filename}', 'parents': ['1sjgHIQPuIzNTLtZpZbmTmZJfsELtr8ix']}
    media = MediaFileUpload(f"purchase_images/{filename}.png", mimetype="image/png")
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
