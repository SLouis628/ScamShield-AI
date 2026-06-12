import whois

def get_domain_age(domain):
    try:
        info = whois.whois(domain)

        creation_date = info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        return creation_date.strftime("%Y-%m-%d")

    except Exception:
        return "Unknown"