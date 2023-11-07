import psutil
import socket
import requests

# Function to check disk usage
def check_disk_usage():
    usage = psutil.disk_usage('/')
    return usage.percent > 20

# Function to check CPU utilization
def check_cpu_utilization():
    return psutil.cpu_percent() < 75

# Function to check localhost availability
def check_localhost():
    try:
        socket.gethostbyname('localhost')
        return True
    except socket.error:
        return False

# Function to check internet access by sending a request to Google
def check_internet_access():
    try:
        response = requests.get('http://www.google.com')
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

if __name__ == "__main__":
    disk_usage_ok = check_disk_usage()
    cpu_utilization_ok = check_cpu_utilization()
    localhost_ok = check_localhost()
    internet_access_ok = check_internet_access()

    if not (disk_usage_ok and cpu_utilization_ok):
        print("ERROR! Disk usage or CPU utilization is out of bounds.")
    elif not (localhost_ok and internet_access_ok):
        print("Network checks failed.")
    else:
        print("Everything is OK.")
