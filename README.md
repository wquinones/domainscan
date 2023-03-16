# Domain Scanner

Domain Scanner is a Python script that scans a single domain or a list of domains, captures the HTTP response code, and takes a screenshot of the domain landing page. The results are saved in a folder named by the domain and organized under a timestamped scan folder.

## Features

- Scan a single domain or a list of domains
- Capture HTTP response code
- Take a screenshot of the domain landing page
- Set a custom timeout for domain scans
- Organize scan results in timestamped folders

## Dependencies

- Python 3.6+
- Requests
- Selenium
- Chrome WebDriver

## Installation

1. Clone the repository:
git clone https://github.com/wquinones/domain-scanner.git

2. Navigate to the project folder:
cd domain-scanner

3. Install the required dependencies:
pip install requests selenium

4. Make sure you have the Chrome WebDriver installed and available in your system's PATH.

## Usage

To scan a single domain:
python domain_scanner.py -d example.com

To scan a list of domains from a file:
python domain_scanner.py -dl domain_list.txt

To set a custom timeout for domain scans in seconds (default is 10 seconds):
python domain_scanner.py -d example.com -t 5

To view help information and available command line options:
python domain_scanner.py --help
