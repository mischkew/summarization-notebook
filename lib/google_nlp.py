from googleapiclient import discovery
import httplib2
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = ('https://{api}.googleapis.com/'
                 '$discovery/rest?version={apiVersion}')

def google_service():
    http = httplib2.Http()

    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)

    return discovery.build('language', 'v1beta1', http=http,
                              discoveryServiceUrl=DISCOVERY_URL)
    
def google_sentiment_analysis(text):
    '''Run a sentiment analysis request on text'''
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text
        }
    }

    service = google_service()
    service_request = service.documents().analyzeSentiment(body=body)

    response = service_request.execute()
    
    polarity = response['documentSentiment']['polarity']
    magnitude = response['documentSentiment']['magnitude']
    return (polarity, magnitude)

def google_syntax_analysis(text):
    '''Run a syntax analysis request on text''' 
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'features': {
            'extract_syntax': True,
        }
    }

    service = google_service()
    service_request = service.documents().annotateText(body=body)
    response = service_request.execute()
    return response
