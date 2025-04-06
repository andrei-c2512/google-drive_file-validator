import config
# native libraries
import sys
import logging
import os
# external libraries
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError

SCOPE = "https://www.googleapis.com/auth/drive"

REQUESTED_FILE_PARAMS = ["id", "name", "parents", "driveId"]


def build_service():
    return build("drive", "v3", credentials=get_credential(str(os.environ.get(config.CREDENTIAL_VAR, config.DEFAULT_CREDENTIALS_PATH))))

def file_params_string():
    result = ""
    for i in range(0, len(REQUESTED_FILE_PARAMS)):
        result += REQUESTED_FILE_PARAMS[i]
        if i != len(REQUESTED_FILE_PARAMS) - 1:
            result += " , "
    return result

def print_params(item, param_list = REQUESTED_FILE_PARAMS):
    result: str = "\n"
    for param in param_list:
        result += param + " : " 
        result += str(item[param])
        result += "\n"

    logging.info(result)
def param_stream(item , param_list = REQUESTED_FILE_PARAMS):
    result: str = "\n" 
    for param in param_list:
        result += param + " : " 
        result += str(item[param])
        result += "\n"
    return result

def get_credential(service_account_key_file: str):
    """Creates a Credential object with the correct OAuth2 authorization.

    Uses the service account key stored in service_account_key_file.

    Args:
        service_account_key_file: path to the file

    Returns:
        Credentials, the user's credential.
    """
    credential = ServiceAccountCredentials.from_json_keyfile_name(
        service_account_key_file, SCOPE
    )

    if not credential or credential.invalid:
        logging.error("Unable to authenticate using service account key.")
        sys.exit(1)

    return credential


def get_drive_files(drive_service, drive_id: str , folder_id : str):
    query : str = "mimeType != 'application/vnd.google-apps.folder' and trashed=false" 
    if folder_id != "NULL":
        query= query + f" and '{folder_id}' in parents"
    
    response = (
        drive_service.files()
        .list(
            driveId=drive_id,
            corpora="drive",
            supportsAllDrives=True,
            q=query,
            #sa bag flag ul ala ca sa nu returneze foldere
            includeItemsFromAllDrives=True,
            fields=f"files({file_params_string()})",
        )
        .execute()
    )

    return response.get("files", [])


def print_drive_files(file_list, params = REQUESTED_FILE_PARAMS):
    result = ""
    if len(file_list) == 0:
        logging.info("The target destination has no files")
        return
    else:
        result +="Files:\n"
    for item in file_list:
        result += param_stream(item , params)
    logging.info(result)

