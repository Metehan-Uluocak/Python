import yara
import os

def yara_scan(directory, rule_file):
    rules = yara.compile(rule_file)
    with open("output_yara.txt", "w") as output_file:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    matches = rules.match(file_path)
                    if matches:
                        output_file.write(f"[!] {file_path} matched rule {matches}\n")
                except Exception as e:
                    output_file.write(f"[ERROR] Error scanning {file_path}: {e}\n")

if __name__ == "__main__":
    directory = r"C:\Users\Mete\Desktop"  
    rule_file = r"C:\Users\Mete\Desktop\YaraExample\example.yara"  
    yara_scan(directory, rule_file)
