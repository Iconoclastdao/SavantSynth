import re

def parse_sections(text):
    # Simple section splitter (replace with PDF/NLP parser as needed)
    sections = re.split(r'\n\s*(?=[A-Z][a-z]+:)', text)
    return sections

def extract_claims(text):
    # Basic pattern matching for "we found", "our results", etc.
    return [line.strip() for line in text.split('\n') if re.search(r'\b(we|our)\b.+\b(found|show|suggest|demonstrate)', line, re.IGNORECASE)]