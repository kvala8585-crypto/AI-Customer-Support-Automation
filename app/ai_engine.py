def detect_intent(message):
    msg = message.lower()

    # ORDER STATUS (tracking related)
    if any(word in msg for word in ["where", "track", "status", "when", "delivered"]):
        if "order" in msg or "delivery" in msg:
            return "ORDER_STATUS"

    # ORDER ISSUE (problem related)
    if any(word in msg for word in ["late", "delay", "not received", "missing", "wrong", "damaged"]):
        return "ORDER_ISSUE"

    # REFUND
    if any(word in msg for word in ["refund", "money back", "return"]):
        return "REFUND"

    # COMPLAINT
    if any(word in msg for word in ["complaint", "bad", "worst", "poor service"]):
        return "COMPLAINT"

    # DEFAULT
    return "GENERAL"