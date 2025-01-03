#Given a valid (IPv4) IP address, return a defanged version of that IP address. A defanged IP address replaces every period "." with "[.]".

def defangIPaddr(address: str) -> str:
        return address.replace(".","[.]")

print(defangIPaddr(address="255.100.50.0"))
