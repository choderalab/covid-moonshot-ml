import argparse
import os
import requests
import time

MPRO_API_CALL = {
    'target_name': 'Mpro',
    'proteins': '',
    'event_info': 'false',
    'sigmaa_info': 'false',
    'diff_info': 'false',
    'trans_matrix_info': 'false',
    'NAN': 'false',
    'mtz_info': 'false',
    'cif_info': 'false',
    'NAN2': 'false',
    'map_info': 'false',
    'single_sdf_file': 'false',
    'sdf_info': 'true',
    'pdb_info': 'true',
    'bound_info': 'true',
    'metadata_info': 'true',
    'smiles_info': 'true',
    'static_link': 'false',
    'file_url': ''
}

def download(fn_out):
    url = 'https://fragalysis.diamond.ac.uk/api/download_structures/'
    ## First send POST request to prepare the download file and get its URL
    r = requests.post(url, data=MPRO_API_CALL)
    url_dl = r.text.split(':"')[1].strip('"}')
    ## Send GET request for the zip archive
    r_dl = requests.get(url, params={'file_url': url_dl})
    ## Full archive stored in r_dl.content, so write to zip file
    with open(fn_out, 'wb') as fp:
        fp.write(r_dl.content)

################################################################################
def get_args():
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-o', required=True, help='Output zip file.')

    return(parser.parse_args())

def main():
    args = get_args()

    download(args.o)

if __name__ == '__main__':
    main()