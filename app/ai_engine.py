def detect_intent(message):
    msg = message.lower()

    if "order" in msg or "delivery" in msg:
        return "ORDER_ISSUE"
    elif "refund" in msg or "money" in msg:
        return "REFUND"
    elif "complaint" in msg or "bad" in msg:
        return "COMPLAINT"
    else:
        return "GENERAL"