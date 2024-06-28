import argparse
import os, io
import threading

parser = argparse.ArgumentParser(prog="Veeam_backup_solution", 
                                description="Synchronizes 2 forders from src to dst with a given interval and logs the actions to std out and a specified file",
                                )

parser.add_argument('in_folder', help='Source folder which\'s content is synchronized')
parser.add_argument('out_folder', help='Target folder which contents will be replaced to be identical to in_folder')
parser.add_argument('period', help='How often to perform synchronization in minutes', type=int)
parser.add_argument('log_file', help='Path to file where to write logs')

args = parser.parse_args()
print(args.in_folder, args.out_folder, args.period, args.log_file)

if not os.path.exists(args.in_folder):
    print(f'Source folder ({args.in_folder}) does not exist')
    exit(1)

if not os.path.exists(args.out_folder):
    print(f"{args.out_folder} does not exist, creating...")
    os.makedirs(args.out_folder)

logfile = io.open(args.log_file, mode="+at")