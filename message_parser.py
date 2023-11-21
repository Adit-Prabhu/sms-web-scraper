import re

# Open the SMS messages file and the output files
with open('sms_messages.txt', 'r') as infile, open('parsed_companies.txt', 'w') as outfile, open('unparsed_messages.txt', 'w') as unparsedfile:
    messages = infile.readlines()

    # Regular expressions for common keywords related to company names
    company_keywords = [
        r'Your (.*?) verification code',
        r'Your (.*?) code is',
        r'Your (.*?) ID code is:',
        r'Account notification: The password for your (.*?) Account',
        r'(.*?) blocked someone with the password',
        r'Use \d+ to verify your (.*?) account',
        r'Tap to reset your (.*?) password',
        r'Your (.*?) verification code is',
        r'\[REAP\]\d+is the One Time Password for purchase of CNY \d+.00 at (.*?) with card ending',
        r'Your security code is:.*? in (.*?)\.',
        r'\d+is your (.*?) code.',
        r'(.*?) code: \d+',
        r'(.*?): Incoming!',
        r'(.*?): Great news!',
        r'(.*?) order cancellation: returns violation.',
        r'We\'re sorry, please return the item to any (.*?) store',
        r'As requested, we\'ve canceled your (.*?) order',
        r'(.*?) Optional Scan sender',
        r'\[#\]\[(.*?)\]\d+is your verification code',
        r'\[#\]\[(.*?)\] \d+ is your verification code',
        r'\[(.*?)\] \d+ is your verification code, valid for 5 minutes',
        r'\[(.*?)\]\d+is your verification code, valid for 5 minutes',
        r'\d+is your (.*?) code',
        r'\d+ is your (.*?) code',
        r'(.*?): your code is \d+',
        r'\d+ is your (.*?) password reset code',
        r'(.*?): Here\'s your temporary authentication code',
        r'Verification code for (.*?):',
        r'Use verification code\d+for (.*?) authentication.',
        r'Código de verificación para (.*):',
        r'Código de verificación:.*?(.*?). It expires',
        r'您的 (.*?) ID 验证码为：',
        r'(.*?) ID 代码为：\d+。请勿与他人共享。',
        r'(\w+) link',
        r'(.*?): Thanks for confirming your phone number. Log in',
        r'para (\w+) es',
        r'use this OTP(\d+)for (\w+)\.',
        r'Tap to reset your (\w+) password:',
        r'【阿里巴巴】您正在登录验证，验证码\d+，',
        r'您正在进行短信登录，验证码\d+，',
        r'注册验证码 \d+，5分钟内有效，请勿告知他人',
        r'您本次验证码为:\d+,如非本人操作，请联系客服：',
        r'短信验证码:\d+ 有效期5分钟.',
        r'Account notification: The password for your (.*?) duyh[email protected] was recently changed',
        r'Use\d+to verify your (.*?) account',
        r'From:\s+(SoFi)',
        r'\d+is your (.*?) OTP',
        r'\d+ is your (.*?) OTP',
        r'(.*?) Password Reset Code: \d+',
        r'(.*?) 2FA Code: \d+\.',
        r'(.*?) code: \d+. Do not share it or use it elsewhere!',
        r'Hello \s+! Your (.*?) ride',
        r'Please enter the below OTP code in the (.*?) to verify your phone number',
        r'\d+ 是 (.*?)的验证码，15分钟内有效，仅用于登录，请勿告知他人。',
        r'\d+是 (.*?)的验证码，15分钟内有效，仅用于登录，请勿告知他人。',
        r'(\w+): Alert on Econoday event on',
        r'(\w+): Your order is ready for pickup at',
        r'(\w+): order canceled due to unusual account activity',
        r'(\w+): DO NOT share this code',
        r'Use\d+as (.*?) account security code',
        r'Use \d+ as (.*?) account security code',
        r'Use \d+ as (\w+) account password reset code',
        r'Good news! A refund was issued for (\w+) order',
        r'欢迎使用(.*?)，您的注册验证码为：',
        
    ]

    # Create a dictionary to store company names and their counts
    company_counts = {}
    parsed_count = 0  # Counter for parsed messages

    # Function to extract company name from a message
    def extract_company_name(message):
        for pattern in company_keywords:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                if "【阿里巴巴】您正在登录验证" in message:
                    return "Alibaba"
                elif "您正在进行短信登录" in message:
                    return "Unamed Chinese Company"
                elif "注册验证码" in message:
                    return "Unamed Chinese Company"
                elif "您本次验证码为" in message:
                    return "Unamed Chinese Company"
                elif "短信验证码" in message:
                    return "Unamed Chinese Company"
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

    #sorted_companies = sorted(company_counts.items(), key=lambda x: len(x[0]))

    # Sort the company names based on their counts
    sorted_companies = sorted(company_counts.items(), key=lambda x: x[1], reverse=True)

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