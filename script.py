import re
import json

def extract_ips_from_file(file_path):
    """
    Reads a local file and extracts all valid IPv4 addresses.

    Args:
        file_path (str): The path to the local file.

    Returns:
        dict: A JSON object containing a list of unique IP addresses
              in the format {"hosts": ["ip1", "ip2", ...]}.
              Returns an empty list if no IPs are found or the file cannot be read.
    """
    ip_addresses = set()
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Regular expression to find IPv4 addresses
                ips_in_line = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', line)
                ip_addresses.update(ips_in_line)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return {"hosts": []}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"hosts": []}

    return {"hosts": list(ip_addresses)}

if __name__ == "__main__":
    ip_list_json = extract_ips_from_file("host_ips.txt")
    print(json.dumps(ip_list_json))