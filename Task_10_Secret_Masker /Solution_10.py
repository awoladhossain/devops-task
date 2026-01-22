api_key = "YOUR_API_KEY"

print(f"API key: {api_key}")

masked_key = api_key[:4]

masked_key += "*" * (len(api_key) - 4)

print(f"Masked API key: {masked_key}")
