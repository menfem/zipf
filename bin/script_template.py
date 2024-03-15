"""Breif description of what the script does."""
import argparse

def main(args):
  """run the program"""
  print('input file:', args.infile)
  print('Output file:', args.outfile)

if __name__ == '__main__':
  USAGE = 'Brief description of what the script does.'
  parser = argparse.ArgumentParser(description=__doc__)	
  parser.add_argument('infile', type=str, help='Input file name')
  parser.add_argument('outfile', type=str, help='Output file name')
  args = parser.parse_args()
  main(args)
