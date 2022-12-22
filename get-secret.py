import logging
from google.cloud import secretmanager
from google.oauth2 import service_account
from google.api_core.exceptions import ClientError

project_id = "pristine-sum-249722"
secret_id = "outputs"
version_id = "4"


def get_secret(project_id, secret_id, version_id):
    try:
        credentials = service_account.Credentials.from_service_account_file('')
        client = secretmanager.SecretManagerServiceClient(credentials=credentials)

        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"

        response = client.access_secret_version(request={"name": name})

        payload = response.payload.data.decode('UTF-8')

        print(response)
    except ClientError as error:
        logging.error(error)



get_secret(project_id, secret_id, version_id)
