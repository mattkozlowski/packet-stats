import PacketStats as ps

f_name = 'illegal.pcap'
csv_name = f_name.split('.')[0] + '.csv'
udp_name = csv_name.split('.')[0] + '-udp.csv'
output_name = csv_name.split('.')[0] + '-generated-data.csv'


ps.generate_csv(f_name, csv_name, udp_name, output_name, 0, 20, ['time', 'ip-src', 'port-source', 'port-dest', 'length'])