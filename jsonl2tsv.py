#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json


def main(jsonl_path, output_path):
    with open(jsonl_path, 'r') as f_in, open(output_path, 'w') as f_out:
        f_out.write("file_name\ttext\n")
        for line in f_in.readlines():
            j = json.loads(line)
            f_out.write(f"{j['file_name']}\t{j['transcript']}\n")


if __name__ == "__main__":
	jsonl_path = sys.argv[1]
	output_path = sys.argv[2]

	main(jsonl_path, output_path)
