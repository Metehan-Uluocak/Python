import os
import shutil
import virustotal_python

API_KEY = "YOUR_API_KEY"

def scan_file(file_path):
    vt = virustotal_python.Virustotal(API_KEY)

    
    files = {"file": (os.path.basename(file_path), open(os.path.abspath(file_path), "rb"))}
    
    try:
        resp = vt.request("files", files=files, method="POST")
        result = resp.json()

        if result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious") == 0:
            print("File is safe.")
        else:
            print(result)
            print("File is malicious.")

        return result

    except Exception as e:
        print(f"Error: {e}")
        return None

def move_file(file_path, destination_folder):
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

def main():
    main_folder = r"SCANNER PATH"
    safe_folder = os.path.join(main_folder, "safe")
    malicious_folder = os.path.join(main_folder, "malicious")

    for folder in [main_folder, safe_folder, malicious_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    file_path = input("Please drag and drop the file to be scanned: ")

    try:
        result = scan_file(file_path)

        if result and result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious") == 0:
            move_file(file_path, safe_folder)
        else:
            move_file(file_path, malicious_folder)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
