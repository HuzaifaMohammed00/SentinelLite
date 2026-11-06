import re

file = "data/sample_access.log"


def parser_ip(file_name):
    with open(file_name, "r") as file:
        file = file.read()
        ip = re.findall(r"(\d+\.\d+\.\d+\.\d+)", file)
    return ip


def parser_path(file_name):
    with open(file_name) as file:
        file = file.read()
        path = re.findall(r"GET\s(.*?)\s+HTTP", file)
    return path


def parser_status(file_name):
    with open(file_name) as file:
        file = file.read()
        status = re.findall(r"(\d+)$", file, re.MULTILINE)
    return status


def classify_request(path):
    path_upper = path.upper()

    if "UNION SELECT" in path_upper or "OR 1=1" in path_upper:
        return "SQL injection"
    elif "/ADMIN" in path_upper or "../" in path_upper:
        return "Unauthorized Admin access"

    return "Normal"


def parse_logs(file_name):
    ips = parser_ip(file_name)
    pathes = parser_path(file_name)
    statuse = parser_status(file_name)
    events = []
    for ip, path, status in zip(ips, pathes, statuse):
        attack_type = classify_request(path)
        event = {"ip": ip, "path": path, "status": status, "attack_type": attack_type}
        events.append(event)
    return events


def main():
    all_events = parse_logs(file)
    print(f"[+] Total events parsed: {len(all_events)}")

    attacker_ips = set()
    for event in all_events:
        if event["attack_type"] != "Normal":
            attacker_ips.add(event["ip"])
            print(
                f"[ALERT] {event['attack_type']} from {event['ip']} -> Status: {event['status']}"
            )

    print(f"\n[+] Unique Attacker IPs (using Set): {attacker_ips}")


if __name__ == "__main__":
    main()
