import re
from typing import List,Union

def to_lower(text: Union[str, None]) -> Union[str,None]:
    if text is None:
        return None
    return text.lower()

def rmv_whitespace(text: Union[str, None]) -> Union[str, None]:
    if text is None:
        return None 
    return text.strip()

def normalise_whitespace(text: Union[str, None]) -> Union[str, None]:
    if text is None:
        return None 
    return re.sub(r"\s+", " ",text).strip()

def tokenize(text: Union[str, None]) -> List[str]:
    """Split text into lowercase word tokens."""
    if not text:
        return []
    text = text.lower()
    return re.findall(r"\b\w+\b", text)

def cleaning_pipeline(text: Union[str, None]) -> Union[str, None]:
    if text is None:
        return None
    text = to_lower(text)
    text = rmv_whitespace(text)
    text = normalise_whitespace(text)

def string_to_number(text: Union[str, None]) -> Union[float, None]:
    if text is None:
        return None
    # try to check if string can be converted or not first 
    try:
        cleaned = text.replace("$", "").replace(",", "").strip()
        return float(cleaned)
    except (ValueError, TypeError):
        return None