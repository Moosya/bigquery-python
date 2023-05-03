from google.oauth2.credentials import Credentials
from google.auth.transport.requests import AuthorizedSession
from google.cloud import bigquery

# Set up credentials
creds = Credentials.from_authorized_user_info(info)  # replace 'info' with your own authorization info

# Set up AuthorizedSession with credentials
authed_session = AuthorizedSession(creds)

# Create BigQuery client with AuthorizedSession
client = bigquery.Client(project=project_id, credentials=creds, _http=authed_session)

# Construct HTTP header with access token
access_token = creds.token
headers = {'Authorization': f'Bearer {access_token}'}

# Make BigQuery API request with header
response = authed_session.get(url, headers=headers)  # replace 'url' with your own API request URL
