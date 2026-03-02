import re

def parse_log(log_line):
    """
    Extract IP address, timestamp, and URL from an Apache/Nginx log entry.
    """
    # Regex pattern for common/combined log format
    pattern = r'(?P<ip>\S+) .* \[(?P<timestamp>[^\]]+)\] "\S+ (?P<url>\S+)'

    match = re.search(pattern, log_line)
    
    if match:
        return {
            "ip_address": match.group("ip"),
            "timestamp": match.group("timestamp"),
            "url": match.group("url")
        }
    else:
        return None


# Example usage
log_entry = '127.0.0.1 - - [26/Feb/2026:10:15:32 +0530] "GET /index.html HTTP/1.1" 200 2326'

result = parse_log(log_entry)

if result:
    print("IP Address:", result["ip_address"])
    print("Timestamp:", result["timestamp"])
    print("URL Accessed:", result["url"])
else:
    print("Invalid log format")