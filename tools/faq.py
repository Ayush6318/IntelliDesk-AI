from langchain.tools import tool

FAQS = {
    "working hours":
        "We are open Monday to Friday from 9:00 AM to 6:00 PM.",

    "refund policy":
        "Refunds are available within 7 days of purchase.",

    "support":
        "You can contact us at support@intellidesk.ai.",

    "phone":
        "Our support number is +91-9876543210.",

    "shipping":
        "We provide shipping across India.",
}


@tool
def faq(question: str) -> str:
    """
    Answer frequently asked questions about the company.
    """

    question = question.lower()

    for keyword, answer in FAQS.items():
        if keyword in question:
            return answer

    return (
        "Sorry, I couldn't find an answer to that question."
    )
