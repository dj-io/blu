import os
import logging
import openai
from dotenv import load_dotenv
from Resource.schemas.generation import ContentGenRequest, TikToken
from .utils import parse_completions, count_tokens
from .enums import Prompt

load_dotenv(".env")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
openai.api_key = OPENAI_API_KEY

async def generate_docs(content: ContentGenRequest):
    """
    Generates documentation based on the context provided, outputs token in and count to track average usage

    :param content: the Content Request Obj containing all the details for informing how to guide content generation
    (e,g. content_type: str, content_context: str, user_context: str, user_id: UUID)
    :return: generated_sections -> dict
    """

    doc = {}
    tokens: TikToken = {"_out": 0}

    DEVELOPER_ARCHITECT_TECH_DOCS = Prompt.DEVELOPER_ARCHITECT_TECH_DOCS.value.format(content_type=content.content_type)
    USER_SECTIONS_PROMPT = Prompt.USER_SECTIONS_PROMPT.value.format(content_type=content.content_type, context=content.content_context)
    MESSAGES = [{"role": "developer", "content": DEVELOPER_ARCHITECT_TECH_DOCS }, {"role": "user", "content": USER_SECTIONS_PROMPT }]

    tokens["_in"] = count_tokens(content.content_context.strip())

    try:
      completion = openai.chat.completions.create(model="gpt-4o", messages=MESSAGES, max_completion_tokens=1000)
      doc["content"] = completion.choices[0].message.content.strip().split("\n\n")
      tokens["_out"] += count_tokens(completion.choices[0].message.content.strip())
      generated_sections = parse_completions(doc)
      logger.info(f"Successfully Generated {content.content_type}")
    except Exception as e:
      logger.error(f"{content.content_type} Generation request failed: {e}")
      raise

    return generated_sections, tokens

