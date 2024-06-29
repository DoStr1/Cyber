import requests
import time
import os

def main(path):
    if os.path.isfile(path):
        print(path+ " Status:"+ check(path))
    else:
        list = list_files_recursive(path)
        for cell in list:
            print(cell + " Status:"+ check(cell))

    print("Done")



def list_files_recursive(directory):
    files_list = [] 
    for root, dirs, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def check(path):
    api_key = "059844901e337742b3fa8b1644072bfb4574cad562ee03e99c9de81ef8d9ef45"

    file_scan_endpoint = 'https://www.virustotal.com/vtapi/v2/file/scan'

    file_report_endpoint = 'https://www.virustotal.com/vtapi/v2/file/report'
    try:
        with open(path, 'rb') as file_to_scan:
            scan_params = {'apikey': api_key}
            files = {'file': (path, file_to_scan)}
            response = requests.post(file_scan_endpoint, files=files, params=scan_params)
            scan_data = response.json()

        resource_id = scan_data.get('resource')
        
        print("Please wait")
        time.sleep(30)

        report_params = {'apikey': api_key, 'resource': resource_id}
        response = requests.get(file_report_endpoint, params=report_params)
        report_data = response.json()

        positives = report_data.get('positives', 0)
        total = report_data.get('total', 0)

        if positives > 0:
            return f'The file contains {positives} virus(es) out of {total} scans.'
        else:
            return'The file is safe. No viruses detected.'

    except OSError as e:
        return f'Error opening file: {e}'
    except Exception as e:
        return f'An error occurred: {e}'
    
main(r'C:\Users\d9787\Desktop\Images')
#r'D:\Yesodot\webroot\imgs\5.jpg'
