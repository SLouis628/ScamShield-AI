def explain_results(threat_score, matched_keywords, urls, domains, phone_numbers, emails):
    reasons = []

    if matched_keywords:
        reasons.append("Suspicious scam-related keywords were detected.")

    urgency_words = ["immediately", "act now", "limited time", "expires today", "final warning", "last chance"]

    for word in matched_keywords:
        if word in urgency_words:
            reasons.append("Urgency language was detected, which is common in phishing scams.")
            break

    if urls:
        reasons.append("A suspicious URL was detected.")

    if domains:
        reasons.append("A domain was extracted for reputation and age analysis.")

    if phone_numbers:
        reasons.append("A phone number was detected and may require reputation checking.")

    if emails:
        reasons.append("An email address was detected and may be part of a phishing attempt.")

    if threat_score >= 80:
        reasons.append("Overall risk is high due to multiple scam indicators.")

    return reasons