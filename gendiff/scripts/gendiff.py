#!/usr/bin/env python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file', )
    parser.add_argument('-f', '--format', default='lines',
                        help='Set format of output (default: lines)')

    args = parser.parse_args()
    print(f'Comparing {args.first_file} with {args.second_file} using format {args.format}.')

    # TODO: Implement the comparison logic with respect to args.format

if __name__ == '__main__':
    main()

