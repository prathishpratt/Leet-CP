# Question 4: You are given a list of email addresses. Write a Python function, extract_unique_company_names, that extracts and returns the unique company names from the email domains in the list.

# Your function should follow these specifications:

# It should take a single argument, emails, which is a list of email addresses (strings).
# It should return a sorted list of unique company names extracted from the email domains in the input list. The company name is the part of the email domain before the top-level domain (TLD).
# Example
# emails = [ "john.doe@example.com", "jane_smith@company.net", "alice@domain.com", "test.user@example.com", "user@domain.net" ]

# Returns: ['company', 'domain', 'example']

import re
def extract_unique_company_names(emails):
    ret = []
    for i in emails:
        l1 = re.split(r"@",i)[1]
        l2 = re.split(r"\.",l1)[0]
        ret.append(l2)
    return sorted(list(set(ret)))