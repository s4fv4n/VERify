import requests
import argparse
import warnings

# Suppress warnings from requests (e.g., about unverified HTTPS requests)
warnings.filterwarnings("ignore")

def collect_headers(url):
    try:
        response = requests.get(url, verify=False)
        
        headers = response.headers
        
        print(f"\nHeaders for {url}:")
        #for key, value in headers.items():
            #print(f"{key}: {value}")
        
        # Check for specific headers and print if present
        if any(header in headers for header in ['Server', 'X-AspNet-Version', 'X-Powered-By', 'X-FEServer', 'X-OWA-Version']):
            if 'Server' in headers:
                print(f"[+] Server header: {headers['Server']}")
            if 'X-AspNet-Version' in headers:
                print(f"[+] X-AspNet-Version header: {headers['X-AspNet-Version']}")
            if 'X-Powered-By' in headers:
                print(f"[+] X-Powered-By header: {headers['X-Powered-By']}")
            if 'X-FEServer' in headers:
                print(f"[+] X-FEServer header: {headers['X-FEServer']}")
            if 'X-OWA-Version' in headers:
                print(f"[+] X-OWA-Version header: {headers['X-OWA-Version']}")
        else:
            print("\nNo relevant headers found in the response.")
    except requests.exceptions.RequestException as e:
        print(f"Error collecting headers: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Collect server headers from a given URL or a file containing URLs")
    parser.add_argument("-u", "--url", type=str, help="URL to collect headers from")
    parser.add_argument("-f", "--file", type=str, help="File containing a list of URLs")

    args = parser.parse_args()

    urls = []

    if args.file:
        try:
            with open(args.file, 'r') as file:
                urls = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: File {args.file} not found.")
            exit(1)
    elif args.url:
        urls.append(args.url) 

    for url in urls:
        collect_headers(url)
