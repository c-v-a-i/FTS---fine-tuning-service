from typing import Any, List, Dict
from pydantic import BaseModel, Field, ConfigDict
from typing import Literal


class ConversationItem(BaseModel):
    type: Literal["assistant", "user"]
    content: str

class GPTOutputSchema(BaseModel):
    document_representation: str = Field(str, description="YAML representation of the CV outputted as a string")
    conversation_translation: List[ConversationItem]
