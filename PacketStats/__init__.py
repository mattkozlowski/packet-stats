# __init__.py
import csv

from .statistics import *
from .convertion import *


def generate_csv(source_filename, csv_filename, udp_filename, output_filename, move, percentage, header_names):
    """
    Generating permutations based on statistics from pcap file.

    :param source_filename: str
        Filename of pcap file
    :param csv_filename: str
        Filename of generated csv from pcap file
    :param udp_filename: str
        Filename of generated csv with only udp packets from csv file
    :param output_filename: str
        Filename of generated permutations based on statistics from udp csv file
    :param move: int
        defines the position of data (default is 0)
        0 -> top,
        1 -> last,
        -1 -> range
    :param percentage: int
        percent value [0-100] of how many data is needed  (default is 20)
    :param header_names:
        list of column names
    """
    export_to_txt(source_filename, csv_filename)
    delete_non_udp(csv_filename, udp_filename, header_names)
    print("%s %s %s" % (source_filename, move, percentage))
    result = permutations(statistics(udp_filename, header_names), header_names, move, percentage)
    with open(output_filename, 'w', newline='') as file:
        csv_file = csv.writer(file, delimiter='\t')
        for row in result:
            csv_file.writerow(row)


def generate_udp(source_filename, csv_filename, udp_filename, header_names):
    """
    Generating udp files from pcap file.

    :param source_filename: str
        Filename of pcap file
    :param csv_filename: str
        Filename of generated csv from pcap file
    :param udp_filename: str
        Filename of generated csv with only udp packets from csv file
    :param header_names:
        list of column names
    """
    export_to_txt(source_filename, csv_filename)
    delete_non_udp(csv_filename, udp_filename, header_names)


def generate_csv_from_udp(udp_filename, output_filename, move, percentage, header_names):
    """
    Generating permutations based on statistics from udp file and saving into output file

    :param udp_filename: str
        Filename of generated csv with only udp packets from csv file
    :param output_filename: str
        Filename of generated permutations based on statistics from udp csv file
    :param move: int
        defines the position of data (default is 0)
        0 -> top,
        1 -> last,
        -1 -> range
    :param percentage: int
        percent value [0-100] of how many data is needed  (default is 20)
    :param header_names:
        list of column names
    """
    result = generate_permutations(udp_filename, move, percentage, header_names)
    with open(output_filename, 'w', newline='') as file:
        csv_file = csv.writer(file, delimiter='\t')
        for row in result:
            csv_file.writerow(row)


def generate_permutations(udp_filename, move, percentage, header_names):
    """
    Generating permutations based on statistics from udp file.

    :param udp_filename: str
        Filename of generated csv with only udp packets from csv file
    :param move: int
        defines the position of data (default is 0)
        0 -> top,
        1 -> last,
        -1 -> range
    :param percentage: int
        percent value [0-100] of how many data is needed  (default is 20)
    :param header_names:
        list of column names
    """
    print("%s %s %s" % (udp_filename, move, percentage))
    result = permutations(statistics(udp_filename, header_names), header_names, move, percentage)
    return result
