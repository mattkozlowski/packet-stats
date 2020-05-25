import PacketStats as ps

f_name = 'illegal.pcap'
csv_name = f_name.split('.')[0] + '.csv'
udp_name = csv_name.split('.')[0] + '-udp.csv'
output_name = csv_name.split('.')[0] + '-generated-data.csv'

print('\n\nTest-Generate-CSV\n\n')
ps.generate_csv(f_name, csv_name, udp_name, output_name, 0, 20, ['time', 'ip-src', 'port-source', 'port-dest', 'length'])

print('\n\nTest-Generate-Permutations\n\n')
results = ps.generate_permutations(udp_name, 0, 20, ['time', 'ip-src', 'port-source', 'port-dest', 'length'])
for r in results:
    print(r)

print('\n\nTest-Generate-UDP\n\n')
ps.generate_udp(f_name, csv_name, udp_name, ['time', 'ip-src', 'port-source', 'port-dest', 'length'])

print('\n\nTest-Generate-CSV-FROM-UDP\n\n')
ps.generate_csv_from_udp(udp_name, output_name + '2', 0, 20, ['time', 'ip-src', 'port-source', 'port-dest', 'length'])

