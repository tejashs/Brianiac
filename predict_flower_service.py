from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from googleapiclient import errors
import json

# Store your full project ID in a variable in the format the API needs.

# Get application default credentials (possible only if the gcloud tool is
#  configured on your machine).

def predict(json_file_path):
    credentials = GoogleCredentials.get_application_default()
    project='steam-airfoil-169600'
    model='flowers'
    version='v1'

    instances = []
    with open(json_file_path) as f:
        for line in f:
            instances.append(json.loads(line))
    # Build a representation of the Cloud ML API.
    ml = discovery.build('ml', 'v1', credentials=credentials)

    name = 'projects/{}/models/{}'.format(project, model)

    if version is not None:
    	name += '/versions/{}'.format(version)

    response = ml.projects().predict(
            name=name,
            body={'instances': instances}
        ).execute()

    if 'error' in response:
    	raise RuntimeError(response['error'])

    return response['predictions']
