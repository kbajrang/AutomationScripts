import os
import re
import json
import chardet
from concurrent.futures import ThreadPoolExecutor
import requests

# Specify the path to your input folder
folder_path = "path of folder"  # Replace with the actual folder path

# Specify the server endpoint where you want to send the JSON data
server_endpoint = 'http://44.198.44.136:8000/malware/data_dump'
headers = {'Content-Type': 'application/json'}

# Get a list of all files in the folder with full paths
file_list = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Define regular expression patterns for different types of data
patterns = {
    "APICall": re.compile(r".*\.api.*", re.MULTILINE | re.IGNORECASE),
    "Permission": re.compile(r".*\.permission.*", re.MULTILINE | re.IGNORECASE),
    "URL": re.compile(r".*Url.*", re.MULTILINE | re.IGNORECASE),
    "Feature": re.compile(r".*Feature.*", re.MULTILINE | re.IGNORECASE),
    "Intent": re.compile(r'Action: "(.+)"', re.MULTILINE | re.IGNORECASE),
    "Activity": re.compile(r".*Activity.*", re.MULTILINE | re.IGNORECASE),
    "Call": re.compile(r".*Call.*", re.MULTILINE | re.IGNORECASE),
    "ServiceReceiver": re.compile(r".*Service.*", re.MULTILINE | re.IGNORECASE),
    "RealPermission": re.compile(r".*RealPermission.*", re.MULTILINE | re.IGNORECASE),
}

def process_file(file_name):
    try:
        print(f"Processing file: {file_name}")

        # Detect the encoding of the file
        with open(file_name, 'rb') as raw_file:
            result = chardet.detect(raw_file.read())
            encoding = result['encoding']

        # Read the content of the input file with the detected encoding
        with open(file_name, "r", encoding=encoding) as input_file:
            data = input_file.read()

        # Extract data for each pattern
        extracted_data = {key: pattern.findall(data) for key, pattern in patterns.items()}

        # Remove slashes and quotes around each value
        extracted_data = {key: '\n'.join([match.replace('\\', '').strip('"') for match in matches]) for key, matches in extracted_data.items()}

        # Convert the extracted data to JSON format
        json_data = json.dumps(extracted_data, indent=2)

        # Print the JSON data
        print(json_data)

        # Send the JSON data to the server
        response = requests.post(server_endpoint, data=json_data, headers=headers)
        if response.status_code == 200:
            print("JSON data successfully sent to the server.")
        else:
            print(f"Failed to send JSON data to the server. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error processing file {file_name}: {e}")

if __name__ == "__main__":
    # Process each file in the folder using ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        executor.map(process_file, file_list)
