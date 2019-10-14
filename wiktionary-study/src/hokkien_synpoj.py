import argparse
import csv
import io


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--syn-csv", help="hokkien synonyms csv", required=True)
    parser.add_argument("-p", "--poj-csv", help="poj csv output file", required=True)
    parser.add_argument("-c", "--combined-csv", help="combined output file", required=True)
    args = parser.parse_args()
