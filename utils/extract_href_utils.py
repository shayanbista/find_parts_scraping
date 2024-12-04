def _extract_href(self, selector):
    """Utility function to extract href attribute."""
    element = self.soup.select_one(selector)
    if element and element.get("href"):
        return element["href"]
    return None
