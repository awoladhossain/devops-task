url = "https://api.github.com/v3"

removed_protocol = url.split("://")[1]
full_domain_name = removed_protocol.split("/")[0]
domain_name = full_domain_name.split(".")
domain = ".".join(domain_name[1:])
print(domain)


