from bs4 import BeautifulSoup


class PartsDetailScraper:
    def __init__(self, soup):
        self.soup = soup

    def parse(self):
        # self.scrape_title_section()
    #    print(self.scrape_stock_and_prices())
        #  print(self.scrape_parts_detail())
        self.scrape_related_parts()



    def scrape_title_section(self):
        product_number_div = self.soup.select_one(
            "div.wrapper>div.analytics-part-info>span"
        )
        manufacturer_div = self.soup.select_one(
            "div.wrapper>div.analytics-part-info>span.analytics-part-manufacturer>div.select-manufacturer select>option:nth-of-type(2)"
        )

        description_paragraph = self.soup.select_one("div.wrapper p")


        product_number = product_number_div.text.strip()
        manufacturer = manufacturer_div.text.strip()
        description = description_paragraph.text.strip()

        return product_number,manufacturer,description


    def scrape_stock_and_prices(self):
        stock_table = self.soup.find("table")
        stock_thead=stock_table.find("thead")
        stock_thead.decompose()
        stock_dist = {}

        if not stock_table:
            return None

        rows = stock_table.find_all("tr")

        for row in rows:
            part_url_a = row.select_one("td:nth-child(1) a")

            parts_number_additional_description = row.select_one("td:nth-child(1) span.td-desc-distributor")

            if parts_number_additional_description is None:
                combined_description = None
            else:
                combined_description = " ".join(
                    [span.text.strip() for span in parts_number_additional_description.find_all("span")]
                )

            part_url = part_url_a["href"]
            part_name = part_url_a.text.strip()

            distributor_url_a = row.select_one("td:nth-child(2) a")
            dist_url = distributor_url_a["href"]
            dist_name = distributor_url_a.text.strip()

            stock_dist["dist_url"] = dist_url
            stock_dist["dist_name"] = dist_name
            stock_dist["part_url"] = part_url
            stock_dist["part_name"] = part_name
            stock_dist["combined_description"] = combined_description

            part_descrition_span = row.select_one("td:nth-child(3) span")
            part_descrition = part_descrition_span.text.strip()
            stock_dist["part_descrition"] = part_descrition


            title_value_pairs = []

            
            title_value_div=row.select("td:nth-child(3) span.additional-description")


            for span_element in title_value_div:
                span_title = span_element.select_one("span:first-child")
                span_value = span_element.select_one("span:last-child")

                if span_title and span_value:
                        title_value_pairs.append({
                            'title': span_title.text.strip(), 
                            'value': span_value.text.strip()  
                        })
            stock_dist["title_value"]=title_value_pairs

            prices_list = []

            prices_quantity_div = row.select("td:nth-child(5) ul > li.price-item")

            for span_element in prices_quantity_div:
                span_quantity = span_element.select_one("span:first-child")
                span_price= span_element.select_one("span:last-child")


                if span_quantity and span_price:
                        prices_list.append({
                            'quantity': span_quantity.text.strip(), 
                            'price': span_price.text.strip()  
                        })

            stock_dist["price_quantity"]=prices_list


        
            seller_url_a=row.select_one("td:nth-child(7) a")
            seller_url=seller_url_a["href"]
            stock_dist["seller_url"]=seller_url


            stock_dist.update({
                "dist_url": dist_url,
                "dist_name": dist_name,
                "part_url": part_url,
                "part_name": part_name,
                "combined_description": combined_description,
                "part_descrition": part_descrition,
                "title_value": title_value_pairs,
                "price_quantity": prices_list,
                "seller_url": seller_url
            })

            print("stock_dist",stock_dist)


            return stock_dist

    def scrape_parts_detail(self):
        parts_table = self.soup.find("div", class_="part-compare-content").find("table")

        parts={}
        
        if not parts_table:
            return None
    
        header_tr=self.soup.find("tr", class_="header-row")


        if header_tr:
            header_tr.decompose()

        
        empty_row=parts_table.find("tr",class_="data-row new-row template-row")
        if empty_row:
            empty_row.decompose()

        rows=parts_table.find_all("tr",class_="data-row")


        if not rows:
            return None
        
        
        for row in rows: 
        
            part_title_row = row.select_one("td:nth-child(1)")
            part_title = part_title_row.text.strip() if part_title_row else None

          
            part_value_row = row.select_one("td:nth-child(2)")
            part_value = part_value_row.text.strip() if part_value_row else None

            parts[part_title] = part_value

        return parts
    
    def scrape_related_parts(self):
        related_part_section = self.soup.find("section", id="relatedParts")

        if not related_part_section:
            return None

        recommended_list = related_part_section.select("ul.recommend-list div.recommend-list-item-info")
        print("recommended list", recommended_list)

        if not recommended_list:
            return None

        parts_data = {}

        for item in recommended_list:
            name=item.select("span:first-child")
            desc_category = item.select("span:last-child")
            print("name", name, desc_category)

            if name and  desc_category:
               
                name = name[0].get("title")  
                description =  desc_category[0].get_text(strip=True)  

                parts_data["related_parts"] = {
                    "name": name,
                    "description": description,
                }
        print("parts data",parts_data)

        return parts_data




                
            

        
         
          


            

     
      
            
                
        


        