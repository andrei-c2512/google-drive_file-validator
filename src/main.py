
from file_filtering import find_invalid_files
from google_api import *

MAX_FILE_LIFETIME: int = 30

DRIVE_ID = "0ANtwa3WJVNrUUk9PVA"
# DRIVE_ID = '1Rq8uetK6bnE6RrzMzf1QRBLUfRVSov8A'

# 
# Sa dau print la fisierele care vor fi sterse
# sa fac sa accepte argumente la linia de comanda
# optional , sa folosesc libraria de logging

def main():
    try:
        service = build_service()
        items = get_drive_files(service, DRIVE_ID)

        if not items:
            print("No files found.")
            return

        invalid_file_list = find_invalid_files(items)
        for item in invalid_file_list:
            print(
                service.files()
                .delete(fileId=f"{item['id']}", supportsAllDrives=True)
                .execute()
            )

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
