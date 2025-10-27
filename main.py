import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--packet_name', type=str)
parser.add_argument('-u', '--url_link_repo', type=str)
parser.add_argument('-m', '--repo_work_mode', type=str)
parser.add_argument('-a', '--ascii_tree_mode', action='store_true')
parser.add_argument('-d', '--max_depth', type=int)

args = parser.parse_args()

print("Arguments: \n")
print("packet_name = " + str(args.packet_name))
print("url_link_repo = " + str(args.url_link_repo))
print("repo_work_mode = " + str(args.repo_work_mode))
print("ascii_tree_mode = " + str(args.ascii_tree_mode))
print("max_depth = " + str(args.max_depth))

if args.packet_name is None:
    print("Error: no packet name provided")
    exit(1)

if args.url_link_repo is None:
    print("Error: no repo link provided")
    exit(1)

if args.repo_work_mode is None:
    print("Error: no repo work mode provided")
    exit(1)

if args.max_depth is None:
    print("Error: no max depth provided")
    exit(1)

if args.max_depth <= 0:
    print("Error: max depth must be positive")
    exit(1)

print("All parameters are valid")