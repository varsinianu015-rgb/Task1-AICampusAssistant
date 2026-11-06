
from langchain_openai import ChatOpenAI
from langchain_core.messages import ToolMessage

from .config import API_KEY, MODEL
from .tools import TOOLS, TOOL_MAP


def answer_question(question):
    if not API_KEY:
        raise RuntimeError("OPENAI_API_KEY is missing in .env")

    llm = ChatOpenAI(
        model=MODEL,
        api_key=API_KEY,
        temperature=0
    ).bind_tools(TOOLS)

    messages = [
        {
            "role": "system",
            "content": (
                "You are a College ERP assistant. "
                "Use ERP tools for factual college data. "
                "Never invent student records or numbers. "
                "If data is unavailable, say so."
            )
        },
        {
            "role": "user",
            "content": question
        }
    ]

    used = []

    for _ in range(5):
        reply = llm.invoke(messages)

        messages.append(reply)

        calls = getattr(reply, "tool_calls", []) or []

        if not calls:
            return str(reply.content), used

        for call in calls:
            tool_name = call["name"]
            tool_args = call["args"]

            used.append(tool_name)

            result = TOOL_MAP[tool_name].invoke(tool_args)

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=call["id"]
                )
            )

    return "I could not complete the lookup. Please try again.", used
