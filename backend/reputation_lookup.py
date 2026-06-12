known_scam_domains = [
    "fake-bank-login.com",
    "winner-prize.net",
    "claim-money-now.org"
]

known_scam_numbers = [
    "+1-800-555-1234",
    "+1-888-999-0000"
]

def check_domain(domain):
    if domain in known_scam_domains:
        return "Known Scam Domain"
    return "Unknown Domain"

def check_phone(number):
    if number in known_scam_numbers:
        return "Known Scam Number"
    return "Unknown Number"