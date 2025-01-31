import requests
import ipaddress
import csv

# URL of the source CSV file
CSV_URL = "https://raw.githubusercontent.com/govcert-ch/CTI/refs/heads/main/OffensiveCIDRs/Bruteforce_CIDR-only.csv"
OUTPUT_FILE = "expanded_ips.csv"

# Fetch the CIDR list from the URL
response = requests.get(CSV_URL)
cidr_list = response.text.splitlines()

# Convert CIDRs to individual IPs (including .0 and .255)
expanded_ips = []
for cidr in cidr_list:
    try:
        network = ipaddress.ip_network(cidr.strip(), strict=False)
        expanded_ips.extend([str(ip) for ip in network])  # Includes all IPs
    except ValueError:
        print(f"Skipping invalid CIDR: {cidr}")

# Save to a new CSV file
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["IP Address"])
    for ip in expanded_ips:
        writer.writerow([ip])

print(f"Expanded IP list saved to {OUTPUT_FILE}")