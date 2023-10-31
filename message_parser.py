import re

# Open the SMS messages file and the output file
with open('sms_messages.txt', 'r') as infile, open('parsed_companies.txt', 'w') as outfile:
    messages = infile.readlines()

    # Regular expressions for common keywords related to company names
    company_keywords = [
        r'Your (.*?) verification code',
        r'Your (.*?) code is',
        r'your (\w+) code',
        r'Use \d+ to verify your (.*?) account',
        r'Tap to reset your (.*?) password',
        r'Your (.*?) verification code is',
        r'Your security code is:.*? in (.*?)\.',
        r'Verification code for (.*?):',
        r'Código de verificación para (.*):',
        r'Código de verificación:.*?(.*?). It expires',
        r'(\w+) link',
        r'para (\w+) es',
        r'use this OTP(\d+)for (\w+)\.',
        r'Tap to reset your (\w+) password:',
    ]

    # Function to extract company name from a message
    def extract_company_name(message):
        for pattern in company_keywords:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                return match.group(1)
        return None

    # Iterate through the messages and extract company names, then write to the output file
    for message in messages:
        company_name = extract_company_name(message)
        if company_name:
            outfile.write(company_name + '\n')

print("Company names extracted and saved to parsed_companies.txt.")