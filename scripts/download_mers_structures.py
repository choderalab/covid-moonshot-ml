import argparse
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from covid_moonshot_ml.datasets import pdb

################################################################################
def get_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-d', help='Directory name to put the structures')
    parser.add_argument('-y', help='MERS structures yaml file')
    parser.add_argument('-r', default=None, help='Path to pdb reference file to align to')
    parser.add_argument('-n', default=None, help='Name of reference')
    return(parser.parse_args())

def main():
    args = get_args()
    pdb_list = pdb.load_pdbs_from_yaml(args.y)
    pdb.download_PDBs(pdb_list, args.d)
    pdb.align_all_pdbs(pdb_list, args.d, args.r, args.n)

if __name__ == '__main__':
    main()