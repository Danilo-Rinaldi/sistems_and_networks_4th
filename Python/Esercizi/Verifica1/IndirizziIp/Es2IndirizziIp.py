import ipaddress

# Verifica se una stringa rappresenta un indirizzo IP valido
def is_valid_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

# Verifica se una stringa rappresenta una rete IP valida
def is_valid_network(network_str):
    try:
        ipaddress.ip_network(network_str)
        return True
    except ValueError:
        return False

# Restituisce la versione (IPv4 o IPv6) di un indirizzo IP
def get_ip_version(ip_str):
    ip = ipaddress.ip_address(ip_str)
    return ip.version

# Restituisce una lista di tutti gli indirizzi IP in una determinata rete
def get_all_ips_in_network(network_str):
    network = ipaddress.ip_network(network_str)
    return [str(ip) for ip in network.hosts()]

# Verifica se un indirizzo IP appartiene a una determinata rete
def is_ip_in_network(ip_str, network_str):
    ip = ipaddress.ip_address(ip_str)
    network = ipaddress.ip_network(network_str)
    return ip in network

# Esempi di utilizzo delle funzioni
ip_address = "192.168.1.1"
network_address = "192.168.1.0/24"

print(f"Is {ip_address} a valid IP address? {is_valid_ip(ip_address)}")
print(f"Is {network_address} a valid network? {is_valid_network(network_address)}")
print(f"The version of {ip_address} is IPv{get_ip_version(ip_address)}")
print(f"All IPs in network {network_address}: {get_all_ips_in_network(network_address)}")
print(f"Is {ip_address} in network {network_address}? {is_ip_in_network(ip_address, network_address)}")
