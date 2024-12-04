from bs4 import BeautifulSoup


from utils.safe_call_utils import safe_call

class PartsDetailScraper:
    def __init__(self, soup):
        self.soup = soup

    def parse(self):

        parts_dict = {}
        parts_dict["title_section"] = self.scrape_title_section()
        parts_dict["stock_and_prices"] = self.scrape_stock_and_prices()
        parts_dict["parts_detail"] = self.scrape_parts_detail()
        parts_dict["related_parts"] = self.scrape_related_parts()
        parts_dict["alternate_sections"] = self.scrape_alternate_sections()

        return parts_dict

    def scrape_title_section(self):
        title_informations = {}

        product_number = self.soup.select_one("span.analytics-part-number").get_text(strip=True)
        description =self.soup.select_one("div.wrapper p").get_text(strip=True)        
        try:
            manufacturer=self.soup.select_one("div.select-manufacturer option:nth-of-type(2)").get_text(strip=True)
        except:
            try:
                manufacturer =self.soup.select_one("span.analytics-part-manufacturer span:nth-of-type(2)").get_text(strip=True)
            except:
                mfg = ""


        title_informations["product_number"] = product_number
        title_informations["manufacturer"] = manufacturer
        title_informations["description"] = description

        return title_informations

    def scrape_stock_and_prices(self):

        stock_dist = {}

        rows = self.soup.select("tr.price-stock-tr")

        if not rows:
            return stock_dist

        for row in rows:
            part_url = safe_call(
                lambda: row.select_one("div.part-name.new a").get("href")
            )
            part_name = safe_call(
                lambda: row.select_one("div.part-name.new a").get_text(strip=True)
            )
            distributor_url = safe_call(lambda: row.select_one(".td-dis a").get("href"))
            distributor_name = safe_call(
                lambda: row.select_one(".td-dis a").get_text(strip=True)
            )
            description = safe_call(
                lambda: row.select_one("span.td-description.more")
            ).get_text(strip=True)
            additional_description = safe_call(
                lambda: row.select("span.additional-description")
            )

            title_value = []

            if not additional_description:
                return title_value

            for span_row in additional_description:
                title = safe_call(
                    lambda: span_row.select_one("span:first-child").get_text(strip=True)
                )
                value = safe_call(
                    lambda: span_row.select_one("span:last-child").get_text(strip=True)
                )

                title_value.append({"title": title, "value": value})

            prices_column = safe_call(lambda: row.select(".td-price > ul > li"))

            prices = []

            if not prices_column:
                return prices

            for quantity_prices in prices_column:
                quantity = safe_call(
                    lambda: quantity_prices.select_one(".label").get_text(strip=True)
                )
                price = safe_call(
                    lambda: quantity_prices.select_one(".value").get_text(strip=True)
                )

                prices.append({"quantity": quantity, "price": price})

            purchase_url = safe_call(
                lambda: row.select_one(".td-buy.last a").get("href")
            )

            stock_dist.update(
                {
                    "part_url": part_url,
                    "part_name": part_name,
                    "distributor_url": distributor_url,
                    "distributor_name": distributor_name,
                    "description": description,
                    "title_value": title_value,
                    "prices": prices,
                    "purchase_url": purchase_url,
                }
            )

            return stock_dist

    def scrape_parts_detail(self):

        compare_table = safe_call(
            lambda: self.soup.select(".default-table.compare-table tr.data-row")
        )

        parts_detail = []

        if not compare_table:
            return parts_detail

        for row in compare_table[1:]:
            title = safe_call(
                lambda: row.select_one(".main-part-cell").get_text(strip=True)
            )
            value = safe_call(
                lambda: row.select_one(".compare-part-cell").get_text(strip=True)
            )

            parts_detail.append(
                {
                    "title": title,
                    "value": value,
                }
            )

        return parts_detail

    def scrape_related_parts(self):

        related_part_section = safe_call(
            lambda: self.soup.select("section#relatedParts ul li span.name")
        )

        related_part = []

        if not related_part_section:
            return related_part

        for span_elements in related_part_section:
            related_names = safe_call(lambda: span_elements.get_text(strip=True))

            related_part.append(
                {
                    "name": related_names,
                }
            )

        return related_part

    def scrape_alternate_sections(self):

        alternate_data = []

        alternate_section_tables = safe_call(
            lambda: self.soup.select(".dash-section-content.analytics-fff table")
        )

        if not alternate_section_tables:
            return alternate_data

        for table in alternate_section_tables:
            rows = table.select("tbody tr")

            for row in rows:

                part_url = safe_call(
                    lambda: row.select_one(".td-col-1 a").get("href")
                )
                part_name = safe_call(
                    lambda: row.select_one(".td-col-1 a").get_text(strip=True)
                )

                manufacturer = safe_call(
                    lambda: row.select_one(".td-col-2").get_text(strip=True)
                )
                prices_url = safe_call(
                    lambda: row.select_one(".td-col-3 a").get("href")
                )
                description = safe_call(
                    lambda: row.select_one(".td-col-4").get_text(strip=True)
                )
                comparison_url = safe_call(
                    lambda: row.select_one(".td-col-5 a").get("href")
                )

                alternate_data.append(
                    {
                        "part_url": part_url,
                        "part_name": part_name,
                        "manufacturer": manufacturer,
                        "prices_url": prices_url,
                        "description": description,
                        "comparison_url": comparison_url,
                    }
                )

        return alternate_data
