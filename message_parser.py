import re

# Open the SMS messages file and the output files
with open('sms_messages.txt', 'r') as infile, open('parsed_companies.txt', 'w') as outfile, open('unparsed_messages.txt', 'w') as unparsedfile:
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

    # Create a dictionary to store company names and their counts
    company_counts = {}
    parsed_count = 0  # Counter for parsed messages

    # Function to extract company name from a message
    def extract_company_name(message):
        for pattern in company_keywords:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                return match.group(1)
        return None

    # Iterate through the messages and extract company names, then update the counts
    unparsed_messages = []
    for message in messages:
        company_name = extract_company_name(message)
        if company_name:
            parsed_count += 1
            company_counts[company_name] = company_counts.get(company_name, 0) + 1
        else:
            unparsed_messages.append(message)  # Store unparsed messages in a list

    sorted_companies = sorted(company_counts.items(), key=lambda x: len(x[0]))

    # Write the total parsed message count at the beginning of the output file
    outfile.write(f"Total Parsed Messages: {parsed_count}\n\n")

    # Write company names and their counts to the output file
    for company, count in sorted_companies:
        outfile.write(f"{company}: {count}\n")

    # Write the total unparsed message count at the beginning of the unparsed file
    unparsedfile.write(f"Total Unparsed Messages: {len(unparsed_messages)}\n\n")

    # Write unparsed messages at the beginning of the unparsed file
    for message in unparsed_messages:
        unparsedfile.write(message)

print("Company names and their counts extracted and saved to parsed_companies.txt.")
print("Unparsed messages saved to unparsed_messages.txt.")