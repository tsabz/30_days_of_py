import requests
import datetime
from requests_html import HTML

now = datetime.datetime.now()
year =now.year


def url_to_txt(url, filename="world.html",save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"world-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return ""

url = "https://www.boxofficemojo.com/year/"

html_text = url_to_txt(url)

r_html = HTML(html=html_text)

table_class = ".imdb-scroll-table"

r_table = r_html.find(table_class)

# print(r_table)
table_data = []
header_name = []
if len(r_table) == 1:
    print(r_table[0].text)
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_col = header_row.find("th")
    header_names = [x.text for x in header_col]   
    for row in rows[1:]:
        # print(row.text)
        cols = row.find("td")
        row_data = []
        for i, col in enumerate(cols): 
            # print(i, col.text, '\n\n')
            row_data.append(col.text)
        table_data.append(row_data)


print(header_name)
print(table_data)