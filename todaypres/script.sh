#!/bin/bash

# read the list of URLs from a file
input_file="karuna.txt"
if [[ ! -f $input_file ]]; then
    echo "Error: input file $input_file not found."
    exit 1
fi

# create a directory to store the downloaded MP3 files
output_dir="mp3s"
if [[ ! -d $output_dir ]]; then
    mkdir $output_dir
fi

# loop over each URL in the input file and download the corresponding MP3 file
while read url; do
    if [[ -z $url ]]; then
        continue  # skip empty lines
    fi

    # use youtube-dl to download the MP3 file from the YouTube URL
    youtube-dl -x --audio-format mp3 --output "$output_dir/%(title)s.%(ext)s" "$url"
done < "$input_file"

