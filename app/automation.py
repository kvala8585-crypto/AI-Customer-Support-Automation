def generate_response(intent, message):

    if intent == "ORDER_ISSUE":
        return "Your order is being processed. Please wait 2-3 days."

    elif intent == "REFUND":
        return "Your refund request has been received. It will be processed in 5-7 days."

    elif intent == "COMPLAINT":
        return "We are sorry for the inconvenience. Our support team will contact you soon."

    else:
        return "Thank you for contacting us. How can we assist you further?"