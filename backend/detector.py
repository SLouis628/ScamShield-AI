# ScamShield AI v0.1
import re
from reputation_lookup import check_domain, check_phone
from domain_lookup import get_domain_age

message = input("Enter suspicious message: ")

threat_score = 0

suspicious_keywords = [
    "urgent",
    "verify",
    "click",
    "account",
    "password",
    "bank",
    "suspended",
    "winner",
    "claim",
    "prize"
]

for keyword in suspicious_keywords:
    if keyword.lower() in message.lower():
        threat_score += 10

urls = re.findall(r'https?://\S+|www\.\S+', message)

if urls:
    threat_score += 30
    print("Suspicious URL detected!")

domains = re.findall(
    r'https?://(?:www\.)?([^/\s]+)',
    message
)

if domains:
    print("Domain detected:")
    print(domains)
    for domain in domains:
        result = check_domain(domain)
        print("Reputation:", result)

        age = get_domain_age(domain)
        print("Creation Date:", age)

        if result == "Known Scam Domain":
            threat_score += 40

phone_numbers = re.findall(
    r'(\+?\d[\d\-\(\) ]{7,}\d)',
    message
)

if phone_numbers:
    threat_score += 20
    print("Phone number detected:")
    print(phone_numbers)
    for number in phone_numbers:
        result = check_phone(number)
        print("Reputation:", result)

        if result == "Known Scam Number":
            threat_score += 40

emails = re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
    message
)

if emails:
    threat_score += 15
    print("Email address detected:")
    print(emails)
print("\n--- ScamShield Analysis ---")
print("Threat Score:", threat_score)

if threat_score >= 50:
    print("Risk Level: HIGH")
elif threat_score >= 20:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")