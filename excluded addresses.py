X_Series = ['X0', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17',
            'X18', 'X19', 'LAN', 'WAN', 'U0', 'U1', 'MGMT']
ip = []
subnet = []
ipv6_link_local_address = []
ipv6_primary_static_address = []
ipv6_primary_static_address_subnet = []
ipv6_primary_dynamic_address = []
ipv6_primary_dynamic_address_subnet = []
all_management_ip = []
ipv6_addresses = []
management_ipv6_addresses = []
for x in X_Series:
    ip.append(str(x) + ' IP')
    subnet.append(str(x) + ' Subnet')
    ipv6_link_local_address.append(str(x) + ' IPv6 Link-Local Address')
    ipv6_primary_static_address.append(str(x) + ' IPv6 Primary Static Address')
    ipv6_primary_static_address_subnet.append(str(x) + ' IPv6 Primary Static Address Subnet')
    ipv6_primary_dynamic_address.append(str(x) + ' IPv6 Primary Dynamic Address')
    ipv6_primary_dynamic_address_subnet.append(str(x) + ' IPv6 Primary Dynamic Address Subnet')
    # below comes under group category...
    all_management_ip.append('All ' + str(x) + ' Management IP')
    ipv6_addresses.append(str(x) + ' IPv6 Addresses')
    management_ipv6_addresses.append(str(x) + ' Management IPv6 Addresses')

# print(ip)
# print(subnet)
# print(ipv6_link_local_address)
# print(ipv6_primary_static_address)
# print(ipv6_primary_static_address_subnet)
# print(ipv6_primary_dynamic_address)
# print(ipv6_primary_dynamic_address_subnet)
# print(all_management_ip)
# print(ipv6_addresses)
# print(management_ipv6_addresses)

total = ip + subnet + ipv6_link_local_address + ipv6_primary_static_address + ipv6_primary_static_address_subnet + ipv6_primary_dynamic_address + ipv6_primary_dynamic_address_subnet + all_management_ip + ipv6_addresses + management_ipv6_addresses

print (total)