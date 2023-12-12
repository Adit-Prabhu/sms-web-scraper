import langid

def separate_non_english_messages(input_file, non_english_file):
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(non_english_file, 'w', encoding='utf-8') as non_english_outfile:

        for line_number, message in enumerate(infile, start=1):
            message = message.strip()

            # Use langid to detect the language of the message
            lang, _ = langid.classify(message)

            # If the detected language is not English, write the message to the non-English file
            if lang != 'en':
                non_english_outfile.write(f"{message}\n")

if __name__ == "__main__":
    input_file = "../sms_messages.txt"
    non_english_file = "../non_english_messages.txt"

    separate_non_english_messages(input_file, non_english_file)

    print("Separation of non-English messages completed.")
