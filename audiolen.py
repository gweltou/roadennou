import os
import sys
from pydub import AudioSegment


def sec2hms(seconds):
    """ Return a string of hours, minutes, seconds from a given number of seconds """
    minutes, seconds = divmod(round(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}' {seconds}''"


def get_total_length(folder_path):
    total_length = 0

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the file is an audio file
        if file_path.lower().endswith(('.mp3', '.wav')):
            # Load the audio file using pydub
            audio = AudioSegment.from_file(file_path)

            # Add the length of the audio file to the total
            total_length += len(audio)

    return total_length



if __name__ == "__main__":
	# Get the total length of all audio files in the folder
	total_length = get_total_length(sys.argv[1])

	# Print the result
	print(f'Total length of all audio files: {sec2hms(total_length/1000)}')
