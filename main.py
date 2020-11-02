import argparse
import build_reader

parser = argparse.ArgumentParser(description="Read out a SC2 build order.")
parser.add_argument('--build', type=str, required=True, help='filename of the build to read in the builds folder')
parser.add_argument('--shorthand', type=bool, default=True, help='whether to use shorthand names for units and buildings')
args = parser.parse_args()

build_reader.read(args.build, args.shorthand)
