#Printmain.py
import argparse
from main import findNum

parser = argparse.ArgumentParser(description='Fills the input')
parser.add_argument('string', type=str, help='Enter your string')
args = parser.parse_args()

findNum(args.string)
