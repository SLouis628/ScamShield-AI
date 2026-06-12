# ScamShield AI v0.1

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

print("\n--- ScamShield Analysis ---")
print("Threat Score:", threat_score)

if threat_score >= 50:
    print("Risk Level: HIGH")
elif threat_score >= 20:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")
    