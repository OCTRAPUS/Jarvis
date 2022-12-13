from util import ec2MetaData
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key",
                        type=str,
                        help="Input the key to fetch details")
    return parser.parse_args()
if __name__ == '__main__':
    args = parse_args()
    meta_util = ec2MetaData()
    meta_util.get_meta_data()