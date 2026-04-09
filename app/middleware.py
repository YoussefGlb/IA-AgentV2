def guardrails(query):
    banned = ["hack", "illegal"]
    for word in banned:
        if word in query.lower():
            return "Blocked request"
    return query


def human_in_loop(response):
    print("Agent:", response)
    decision = input("Approve? (yes/no): ")
    return response if decision == "yes" else "Rejected"