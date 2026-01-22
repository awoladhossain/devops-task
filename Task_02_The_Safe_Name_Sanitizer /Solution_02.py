bucket_name = "My Project Backup"

bucket_name = bucket_name.strip()
bucket_name = bucket_name.replace(" ", "-")
bucket_name = bucket_name.lower()

print(bucket_name)
