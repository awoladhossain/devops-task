port_string="80080"
port_int=int(port_string)
print(port_int)

if 1 <= port_int <= 65535:
  print("Valid")
else:
  print("Invalid")
