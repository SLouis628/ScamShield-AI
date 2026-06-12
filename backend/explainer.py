def explain_results(threat_score):
    reasons = []

    if threat_score >= 80:
        reasons.append("High number of scam indicators detected.")
    elif threat_score >= 50:
        reasons.append("Several suspicious indicators detected.")
    elif threat_score >= 20:
        reasons.append("Some suspicious indicators detected.")
    else:
        reasons.append("Few or no suspicious indicators detected.")

    return reasons