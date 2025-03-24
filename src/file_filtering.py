from datetime import datetime
import os

MAX_FILE_LIFETIME: int = 30


def find_invalid_files(file_list):
    invalid_file_list = []

    for file_item in file_list:
        try:
            # splits the name into two (name and extension), we store the name
            file_name = os.path.splitext(file_item["name"])[0]

            if valid_file(file_name):
                invalid_file_list.append(file_item)
        except Exception as e:
            print(
                f"There was an exception: {e}. The file with the name '{file_item['name']}' was ignored"
            )

    return invalid_file_list


def valid_file(file_name: str):
    current_date: datetime = datetime.now()
    # splits it into date, time and project name
    file_metadata = file_name.split("_", 2)

    date_info_list = file_metadata[0].split("-", 2)

    # we skip this file because we will keep every backup from the first day
    if len(date_info_list) != 3:
        print(
            f"File '{file_name}' was ignored because of invalid number of date fields. Format is 'YYYY-MM-DD'"
        )
        return False

    if date_info_list[2] == "1" or date_info_list[2] == "01":
        return False

    # we transform the string list into a date object
    file_date: datetime = datetime(
        int(date_info_list[0]),
        int(date_info_list[1]),
        int(date_info_list[2]),
        0,
        0,
        0,
    )
    # we calculate the difference
    file_lifetime: int = (current_date - file_date).days
    return file_lifetime > MAX_FILE_LIFETIME
