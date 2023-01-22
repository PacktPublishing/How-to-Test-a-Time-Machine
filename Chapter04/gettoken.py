from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
import requests

flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['openid', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'],
    redirect_uri='https://localhost:8080/oauthcallback')

auth_url, state = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type='offline',
    prompt='consent',
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes='true')

print(auth_url)


code = input('Enter the authorization code for the above url: ')
code = code.replace("%2F", "/")
token = flow.fetch_token(code=code)
auth_url, state = flow.authorization_url(
    # Enable offline access so that you can refresh an access token without
    # re-prompting the user for permission. Recommended for web server apps.
    access_type='offline',
    prompt='consent',
    # Enable incremental authorization. Recommended as a best practice.
    include_granted_scopes='true')
code1 = requests.get(auth_url)
print(code1)
print(code1.content)
print(code1.url)

# retrieve access token
print('access token below')
print(token['access_token'])
print('duration')
print(token['expires_in'])

# View the email address of the authenticated user.
user_info_service = build('oauth2', 'v2', credentials=flow.credentials)
user_info = user_info_service.userinfo().get().execute()
print(user_info['email'])
