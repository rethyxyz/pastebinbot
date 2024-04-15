import random
import os
import string
import requests
import threading
import rethyxyz.rethyxyz

MAX_CONSECUTIVE_ERRORS = 10
NUM_THREADS = 10  # Adjust the number of threads as needed

# Define a global constant variable containing relay server hostnames
RELAY_LOCATIONS = ["us", "ca", "uk", "de", "nl", "se", "ch", "fi", "fr", "it", "no"]

def save_url_content(url, file_path):
    consecutive_429_errors = 0
    consecutive_522_errors = 0

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"{url}: Content saved to {file_path}")
        elif response.status_code == 404:
            print(f"{url}: Error 404: Page not found")
        elif response.status_code == 429:
            print(f"{url}: Error 429: Too Many Requests")
            consecutive_429_errors += 1
            if consecutive_429_errors > MAX_CONSECUTIVE_ERRORS:
                reset_mullvad_connection()
                print("Resetting Mullvad connection...")
        elif response.status_code == 522:
            print(f"{url}: Error 522: Connection Timed Out")
            consecutive_522_errors += 1
            if consecutive_522_errors > MAX_CONSECUTIVE_ERRORS:
                reset_mullvad_connection()
                print("Resetting Mullvad connection...")
        else:
            print(f"{url}: Unexpected status code: {response.status_code}")
            consecutive_429_errors = 0
            consecutive_522_errors = 0
    except requests.RequestException as e:
        print(f"Error: {e}")

def randchar(iterations):
    charstring = ""
    for i in range(0, iterations):
        if not random.randint(0,1):
            charstring += str(random.randint(0,9))
        else:
            if not random.randint(0,1):
                charstring += random.choice(string.ascii_letters).upper()
            else:
                charstring += random.choice(string.ascii_letters).lower()

    return charstring

def reset_mullvad_connection():
    # Randomly select a location from RELAY_LOCATIONS
    location = random.choice(RELAY_LOCATIONS)
    # Construct the mullvad command with the selected location
    command = f"mullvad relay set location {location}"
    # Execute the command
    os.system(command)
    print(f"Mullvad location set to: {location}")

def parallel_url_calls(url):
    while True:
        id = randchar(8)
        save_url_content(f"{url}{id}", f"{id}")

def main():
    urls = [
        "https://pastebin.pl/view/raw/",
        "https://pastebin.com/raw/"
    ]

    rethyxyz.rethyxyz.show_intro("pastebinbot")

    # Start a thread for each URL
    threads = []
    for url in urls:
        for _ in range(NUM_THREADS):
            thread = threading.Thread(target=parallel_url_calls, args=(url,))
            thread.start()
            threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()