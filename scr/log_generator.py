import random

def generate_logs():
    ips = ["192.168.1.15", "10.0.0.5", "185.106.96.158"]
    normal_paths = ["/home", "/products", "/contact"]
    attack_paths = [
        "/login?user=admin' OR 1=1--",
        "/products?id=1 UNION SELECT username,password FROM users",
        "/admin/config",
    ]
    
    all_paths = normal_paths + attack_paths
    status_codes = ["200", "401", "403", "404", "500"]

    with open("data/sample_access.log", "w") as file:
        for _ in range(50):
            ip = random.choice(ips)
            path = random.choice(all_paths)
            status = random.choice(status_codes)
            
            line = f'{ip} - [01/Nov/2026:14:36:11] "GET {path} HTTP/1.1" {status}\n'
            file.write(line)
            
    print("[+] Log file generated successfully!")

if __name__ == "__main__":
    generate_logs()