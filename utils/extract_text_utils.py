def _extract_text(self, selector, is_required=False):
    """Utility function to extract text from an element."""
    element = self.soup.select_one(selector)
    if element:
        return element.text.strip()
    if is_required:
        return None
    return ""
