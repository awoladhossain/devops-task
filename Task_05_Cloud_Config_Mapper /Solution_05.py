vm = {
    "id": "i-0abc123def001",
    "ip": "192.168.1.100",
    "status": "running",
    "region": "us-east-1",
}

vm["status"] = "stopped"

vm["instance_type"] = "t3.large"

print(f"Updated VM config: {vm}")
