import argparse
import build_reader

parser = argparse.ArgumentParser(description="Read out a SC2 build order.")
parser.add_argument('--build', type=str, required=True, help='filename of the build to read in the builds folder')
parser.add_argument('--shorthand', type=bool, default=True, help='whether to use shorthand names for units and buildings')
parser.add_argument('--supply', type=bool, default=False, help='whether to read the supply number with the action')
parser.add_argument('--delay', type=int, default=-3, help='seconds to delay speech (can be negative)')
args = parser.parse_args()

build_reader.read(args.build, args.shorthand, args.supply, args.delay)
