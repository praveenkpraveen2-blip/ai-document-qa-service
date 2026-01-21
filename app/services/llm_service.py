def generate_answer(context: str, question: str) -> str:
    """
    Mocked LLM integration.
    In production, this would call an external LLM API.
    """
    if not context:
        return "I don't know"

    return f"Answer generated using provided context: {context[:200]}..."
