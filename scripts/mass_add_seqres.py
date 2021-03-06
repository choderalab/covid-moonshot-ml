"""
Add MPRO seqres for an entire directory downloaded from fragalysis.
"""
import argparse
import glob
import multiprocessing as mp
import os
import sys

sys.path.append(f'{os.path.dirname(os.path.abspath(__file__))}/../')
from covid_moonshot_ml.datasets.utils import add_seqres

def get_args():
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-i', required=True, help='Input directory.')

    return(parser.parse_args())

def main():
    args = get_args()

    ## Find all files to fix
    in_fns = glob.glob(f'{args.i}/*/*_bound.pdb')
    ## Replace _bound with _seqres in output filenames
    out_fns = [f'{fn[:-10]}_seqres.pdb' for fn in in_fns]

    with mp.Pool(32) as pool:
        pool.starmap(add_seqres, zip(in_fns, out_fns))

if __name__ == '__main__':
    main()
