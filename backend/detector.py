# ScamShield AI v0.1
import re

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
print("\n--- ScamShield Analysis ---")
print("Threat Score:", threat_score)

if threat_score >= 50:
    print("Risk Level: HIGH")
elif threat_score >= 20:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")