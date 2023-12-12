from mtranslate import translate
import time

def batch_translate_messages(input_file, original_file, translated_file, batch_size=100, max_retries=3):
    messages = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line_number, message in enumerate(infile, start=1):
            message = message.strip()
            messages.append(message)

            if len(messages) == batch_size:
                translate_batch(messages, original_file, translated_file, line_number - batch_size + 1, max_retries)
                messages = []

        # Translate the remaining messages (if any) in the last batch
        if messages:
            translate_batch(messages, original_file, translated_file, line_number - len(messages) + 1, max_retries)

def translate_batch(messages, original_file, translated_file, start_line_number, max_retries):
    retries = 0

    while retries < max_retries:
        try:
            translations = [translate(message, 'en') for message in messages]

            # Check if translations is not None
            if translations:
                with open(original_file, 'a', encoding='utf-8') as original_outfile, \
                     open(translated_file, 'a', encoding='utf-8') as translated_outfile:
                    for i, translation in enumerate(translations):
                        original_outfile.write(f"{messages[i]}\n")
                        translated_outfile.write(f"{translation}\n")

                break  # Successful translation, exit the loop

            else:
                print(f"Error translating lines {start_line_number} - {start_line_number + len(messages) - 1}: No translation data")
                retries += 1
                time.sleep(1)  # Add a delay before retrying

        except Exception as e:
            print(f"Error translating lines {start_line_number} - {start_line_number + len(messages) - 1}: {e}")
            retries += 1
            time.sleep(1)  # Add a delay before retrying

if __name__ == "__main__":
    input_file = "../non_english_messages.txt"
    original_file = "batch_original.txt"
    translated_file = "batch_translated.txt"
    batch_size = 10000
    max_retries = 3

    start_time = time.time()
    batch_translate_messages(input_file, original_file, translated_file, batch_size, max_retries)
    end_time = time.time()

    print(f"Translation completed in {end_time - start_time:.2f} seconds.")