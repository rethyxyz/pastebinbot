import os
import sys
import time
import random
import string
import requests

urls = [
    "https://pastebin.pl/view/raw/",
    "https://pastebin.com/raw/"
]

def motd():
    print("pastebinbot\n")
def help():
    counter = 0
    print("Choose from one of the following URLs.")
    for url in urls:
        print(f"{counter}: {url}")
        counter+=1
    print("")
    print("Example: pastebinbot.py 1")

def switch_vpn():
    # TODO: get location strings dynamically through mullvad command:
    # mullvad relay list
    location_strings = [
        "us-qas-ovpn-001", "us-qas-ovpn-002", "us-qas-ovpn-101",
        "us-qas-ovpn-102", "us-qas-wg-001", "us-qas-wg-002", "us-qas-wg-003",
        "us-qas-wg-004", "us-qas-wg-102", "us-qas-wg-103", "us-atl-ovpn-001",
        "us-atl-ovpn-002", "us-atl-ovpn-101", "us-atl-ovpn-102",
        "us-atl-ovpn-103", "us-atl-ovpn-104", "us-atl-ovpn-105",
        "us-atl-wg-001", "us-atl-wg-002", "us-atl-wg-101", "us-atl-wg-102",
        "us-atl-wg-103", "us-atl-wg-104", "us-atl-wg-105", "us-atl-wg-106",
        "us-atl-wg-107", "us-atl-wg-108", "us-atl-wg-110", "us-atl-wg-201",
        "us-atl-wg-202", "us-atl-wg-203", "us-atl-wg-204", "us-bos-wg-001",
        "us-bos-wg-002", "us-bos-wg-101", "us-bos-wg-102", "us-chi-ovpn-001",
        "us-chi-ovpn-002", "us-chi-ovpn-003", "us-chi-wg-001", "us-chi-wg-002",
        "us-chi-wg-003", "us-chi-wg-004", "us-chi-wg-005", "us-chi-wg-006",
        "us-chi-wg-101", "us-chi-wg-102", "us-chi-wg-104", "us-chi-wg-201",
        "us-chi-wg-202", "us-chi-wg-203", "us-dal-ovpn-001", "us-dal-ovpn-002",
        "us-dal-ovpn-101", "us-dal-ovpn-102", "us-dal-ovpn-103",
        "us-dal-ovpn-104", "us-dal-ovpn-105", "us-dal-wg-001", "us-dal-wg-002",
        "us-dal-wg-003", "us-dal-wg-101", "us-dal-wg-102", "us-dal-wg-103",
        "us-dal-wg-104", "us-dal-wg-105", "us-dal-wg-106", "us-dal-wg-107",
        "us-dal-wg-108", "us-dal-wg-109", "us-dal-wg-110", "us-dal-wg-301",
        "us-dal-wg-302", "us-dal-wg-303", "us-dal-wg-401", "us-dal-wg-402",
        "us-dal-wg-403", "us-den-ovpn-001", "us-den-ovpn-002", "us-den-wg-001",
        "us-den-wg-002", "us-den-wg-003", "us-den-wg-101", "us-den-wg-102",
        "us-hou-wg-001", "us-hou-wg-002", "us-hou-wg-003", "us-hou-wg-004",
        "us-lax-ovpn-101", "us-lax-ovpn-102", "us-lax-ovpn-201",
        "us-lax-ovpn-202", "us-lax-ovpn-401", "us-lax-ovpn-402",
        "us-lax-ovpn-403", "us-lax-ovpn-404", "us-lax-wg-101", "us-lax-wg-102",
        "us-lax-wg-103", "us-lax-wg-201", "us-lax-wg-202", "us-lax-wg-203",
        "us-lax-wg-301", "us-lax-wg-302", "us-lax-wg-303", "us-lax-wg-401",
        "us-lax-wg-402", "us-lax-wg-403", "us-lax-wg-404", "us-lax-wg-405",
        "us-mia-ovpn-101", "us-mia-ovpn-102", "us-mia-wg-001", "us-mia-wg-002",
        "us-mia-wg-003", "us-mia-wg-101", "us-mia-wg-102", "us-mia-wg-103",
        "us-mia-wg-301", "us-mia-wg-302", "us-nyc-ovpn-401", "us-nyc-ovpn-402",
        "us-nyc-ovpn-403", "us-nyc-ovpn-501", "us-nyc-ovpn-502",
        "us-nyc-ovpn-503", "us-nyc-ovpn-504", "us-nyc-ovpn-601",
        "us-nyc-ovpn-602", "us-nyc-ovpn-603", "us-nyc-ovpn-604",
        "us-nyc-wg-301", "us-nyc-wg-302", "us-nyc-wg-303", "us-nyc-wg-401",
        "us-nyc-wg-402", "us-nyc-wg-403", "us-nyc-wg-501", "us-nyc-wg-502",
        "us-nyc-wg-503", "us-nyc-wg-504", "us-nyc-wg-505", "us-nyc-wg-601",
        "us-nyc-wg-602", "us-nyc-wg-603", "us-nyc-wg-604", "us-nyc-wg-605",
        "us-phx-ovpn-101", "us-phx-ovpn-102", "us-phx-wg-101", "us-phx-wg-102",
        "us-phx-wg-103", "us-rag-ovpn-101", "us-rag-ovpn-102",
        "us-rag-ovpn-103", "us-rag-wg-101", "us-rag-wg-102", "us-rag-wg-103",
        "us-rag-wg-104", "us-rag-wg-105", "us-slc-ovpn-101", "us-slc-ovpn-102",
        "us-slc-ovpn-103", "us-slc-ovpn-104", "us-slc-ovpn-105",
        "us-slc-ovpn-106", "us-slc-wg-101", "us-slc-wg-102", "us-slc-wg-103",
        "us-slc-wg-104", "us-slc-wg-105", "us-slc-wg-106", "us-slc-wg-107",
        "us-slc-wg-108", "us-slc-wg-109", "us-sjc-ovpn-001", "us-sjc-ovpn-002",
        "us-sjc-wg-001", "us-sjc-wg-002", "us-sjc-wg-003", "us-sjc-wg-101",
        "us-sjc-wg-102", "us-sjc-wg-103", "us-sjc-wg-104", "us-sjc-wg-105",
        "us-sjc-wg-106", "us-sjc-wg-107", "us-sjc-wg-108", "us-sjc-wg-302",
        "us-sjc-wg-303", "us-sea-ovpn-101", "us-sea-ovpn-102", "us-sea-wg-001",
        "us-sea-wg-002", "us-sea-wg-003", "us-sea-wg-101", "us-sea-wg-103",
        "us-sea-wg-201", "us-sea-wg-202", "us-sea-wg-203", "us-sea-wg-204",
        "us-sea-wg-205", "us-sea-wg-206", "us-sea-wg-207", "us-sea-wg-208",
        "us-sea-wg-301", "us-sea-wg-302", "us-uyk-wg-101", "us-uyk-wg-102",
        "us-uyk-wg-103"
    ]

    os.system(f"mullvad relay set location {location_strings[random.randint(0,len(location_strings))]}")
    time.sleep(8)

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

    # output examples:
    # RCND62By
    # jsD4NwP3
    # tSKQFMNc
    return charstring

def main():
    counter = 0
    forbidden_counter = 0

    motd()

    if len(sys.argv) < 2:
        print("Error: No argument provided.\n")
        help()
        sys.exit(1)

    try:
        url = urls[int(sys.argv[1])]
    except IndexError:
        print("Error: argv[1] doesn't exist in URL list.\n")
        help()
        sys.exit(1)

    while True:
        id = randchar(8)
        try:
            returncode = requests.get(f"{url}/{id}")
        except requests.exceptions.ConnectionError:
            print(f"Network failure {url}{id}")
            continue

        if returncode.status_code == 200:
            print(f"{counter}: Found {url}{id} {returncode.status_code}")
            f = open(f"{id}", "w")
            f.write(f"{url}{id}\n")
            f.write(f"{returncode.text}")
            f.close()
        elif returncode.status_code == 403:
            if forbidden_counter >= 5:
                switch_vpn()
                forbidden_counter = 0
            else:
                forbidden_counter += 1
        else:
            print(f"{counter}: {url}{id} {returncode.status_code}")

        counter += 1

if __name__ == "__main__":
    main()