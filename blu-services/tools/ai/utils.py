import os
import re
import json
import tiktoken
import logging
import openai
from dotenv import load_dotenv
from .enums import Prompt

load_dotenv(".env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY

def count_tokens(context):
    encoding = tiktoken.encoding_for_model("gpt-4o")
    return len(encoding.encode(context))

def parse_completions(response_text: str):
    """
    Parses OpenAI's response and organizes sections into a structured dictionary.

    :param response_text: JSON-like string containing structured markdown content.
    :return: Dictionary { "Section Title": "Section Content" }
    """

    # Ensure response_text is properly parsed into a dictionary
    response_dict = json.loads(response_text) if isinstance(response_text, str) else response_text
    content_list = response_dict.get("content", [])
    heading_pattern = re.compile(r"^(#{1,3})\s+(.+)$")  # Detects #, ##, ### Titles

    sections = []
    current_section = None

    for line in content_list:
        line = line.strip()

        # Check for Markdown headings `# Title`, `## Subtitle`, `### Subsection`
        heading_match = heading_pattern.match(line)
        if heading_match:
            if current_section:
                sections.append(current_section)

            #  Start new section
            current_section = {heading_match.group(2): ""}  # Title: Content
            continue

        #  Append content under the current section
        if current_section:
            key = list(current_section.keys())[0]
            current_section[key] += "\n" + line if current_section[key] else line

    #  Store the last section
    if current_section:
        sections.append(current_section)

    return sections
