#!/bin/bash

# Define the Python script file name
python_script="scraper.py"

# Loop through lines in the input file
while IFS= read -r line; do
    # Extract phone number, start page, and end page
    phone_number=$(echo "$line" | awk '{print $1}')
    start_page=$(echo "$line" | awk '{print $2}')
    end_page=$(echo "$line" | awk '{print $3}')

    # Run the Python script with the extracted arguments
    python "$python_script" "$phone_number" "$start_page" "$end_page"
done < "input.txt"