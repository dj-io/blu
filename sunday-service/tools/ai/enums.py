from enum import Enum

class Prompt(Enum):
    """Enum class to store system and user messages for OpenAI API."""

    DEVELOPER_ARCHITECT_TECH_DOCS = "You are are a principal architect who specializes in technical writing at a market defining software company, you will be writing technical documentation for a {content_type}"
    USER_ANALYZE_CONTEXT_PROMPT = "Analyze this project context and define the key topics the {content_type} documentation should address:\n\n{context}"
    USER_SECTIONS_PROMPT = "Analyze this '{context}' and generate a comprehensive {content_type}"
    USER_DOC_PROMPT = "Write a documentation section for '{section}' using the following project context:\n\n{context}"
    USER_CODE_REVIEW = "Analyze the following code and provide improvements:\n\n{code}"


class Gpt(Enum):
    GPT_4o = "gpt-4o"
    GPT_4o_MINI = "gpt-4o mini"
    OPENAI_o3_MINI = "o3-mini"

class Model(Enum):
    APP_MODEL = Gpt.GPT_4o_MINI
