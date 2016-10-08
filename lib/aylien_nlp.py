from aylienapiclient import textapi

APP_ID = '317c30f4'
APP_KEY = 'd37aa76b712e9a9d77084b09cb16792e'
client = textapi.Client(APP_ID, APP_KEY)

def summarize(options):
    return client.Summarize(options)