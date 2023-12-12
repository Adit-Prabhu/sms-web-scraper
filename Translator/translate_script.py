from googletrans import Translator

def is_english(text):
    # Simple check to identify English messages
    return all(ord(char) < 128 for char in text)

def translate_messages(input_file, original_file, translated_file):
    translator = Translator()
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(original_file, 'w', encoding='utf-8') as original_outfile, \
         open(translated_file, 'w', encoding='utf-8') as translated_outfile:

        for line_number, message in enumerate(infile, start=1):
            message = message.strip()

            if not is_english(message):
                # Non-English message, translate it
                try:
                    translation = translator.translate(message, dest='en').text
                    original_outfile.write(f"{message}\n")
                    translated_outfile.write(f"{translation}\n")
                except Exception as e:
                    print(f"Error translating line {line_number}: {e}")

if __name__ == "__main__":
    input_file = "../sms_messages.txt"
    original_file = "original.txt"
    translated_file = "translated.txt"

    translate_messages(input_file, original_file, translated_file)