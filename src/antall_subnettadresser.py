"""
Et subnett har nettverksmasken 11111111.11111111.00000000.00000000
Hvor mange gyldige IP-adresser kan tildeles verter i subnettet?
"""

def num_adresses_subnet(network_mask_binary_string):
    subnet = ''

    network_mask_binary_string = network_mask_binary_string.split('.')
    for byte in network_mask_binary_string:
        for bit in byte:
            if bit == '0':
                subnet += '1'

    adresses = 2**len(subnet) - 2

    return adresses


print(num_adresses_subnet('11111111.11111111.00000000.00000000'))
