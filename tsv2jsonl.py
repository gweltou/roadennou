import sys


def main(tsv_path, output_path):
    with open(tsv_path, 'r') as f_in, open(output_path, 'w') as f_out:
        for line in f_in.readlines()[1:]:
            seg_audio_file, sentence = line.split('\t')
            sentence = sentence.strip().replace('\"', '\\"')
            f_out.write(f'{{"file_name": "{seg_audio_file}", "transcript": "{sentence}"}}\n')


if __name__ == "__main__":
	tsv_path = sys.argv[1]
	output_path = sys.argv[2]

	main(tsv_path, output_path)
