import argparse
import os
import sys
import datetime
import requests
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def check_dependencies():
    try:
        import requests
        import selenium
    except ImportError:
        print("Some dependencies are missing. Do you want to install them?")
        choice = input("Enter Y/N: ").lower()
        if choice == 'y':
            subprocess.call("pip install requests selenium", shell=True)
        else:
            print("Please install the required dependencies manually.")
            sys.exit(1)

def create_scan_folder():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    scan_folder = f"scan_{timestamp}"
    os.makedirs(scan_folder, exist_ok=True)
    return scan_folder

def save_http_response_code(scan_folder, domain, response_code):
    file_name = f"HTTP_RESPONSE_CODE_{response_code}.txt"
    with open(os.path.join(scan_folder, domain, file_name), "w") as f:
        f.write(f"{domain} - HTTP response code: {response_code}\n")

def save_screenshot(scan_folder, domain, timeout):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(timeout)
    try:
        driver.get(f"http://{domain}")
        screenshot_file = os.path.join(scan_folder, domain, "screenshot.png")
        driver.save_screenshot(screenshot_file)
    except Exception as e:
        print(f"Error capturing screenshot for {domain}: {e}")
    finally:
        driver.quit()

def scan_domains(scan_folder, domains, timeout):
    for domain in domains:
        os.makedirs(os.path.join(scan_folder, domain), exist_ok=True)
        try:
            response = requests.get(f"http://{domain}", timeout=timeout)
            save_http_response_code(scan_folder, domain, response.status_code)
        except Exception as e:
            print(f"Error while scanning {domain}: {e}")

        save_screenshot(scan_folder, domain, timeout)

def main():
    check_dependencies()

    parser = argparse.ArgumentParser(description="Domain scanning script")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-dl", "--domainlist", type=str, help="Path to the list of domains")
    group.add_argument("-d", "--domain", type=str, help="A single domain to scan")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Timeout for domain scans in seconds")

    args = parser.parse_args()

    scan_folder = create_scan_folder()

    if args.domainlist:
        with open(args.domainlist, "r") as f:
            domains = [line.strip() for line in f]
    else:
        domains = [args.domain]

    scan_domains(scan_folder, domains, args.timeout)

if __name__ == "__main__":
    main()

