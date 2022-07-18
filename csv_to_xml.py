#!python3 

# A Python3 script that converts csv file into a Google Merchangs xml schema

import csv
from pathlib import Path


p = Path.home() / 'Code' / 'january_2022.csv'
f = open(p)
csv_f = csv.reader(f)
data=[]
for row in csv_f:
    data.append(row)
f.close()
print(data)
print(len(data))
def convert_row(row):
    return """<reviews>
    <review>
        <products>
            <product>
                <product_ids>
                    <gtins>
                        <gtin>%s</gtin>
                    </gtins>
                    <mpns>
                        <mpn>%s</mpn>
                    </mpns>
                    <skus>
                        <sku>%s</sku>
                    </skus>
                    <brands>
                        <brand>%s</brand>
                    </brands>
                </product_ids>
                <product_name>%s</product_name>
                <product_url>%s</product_url>
            </product>
        </products>
        <review_url type="singleton">%s</review_url>
        <content>%s</content>
        <ratings>
            <overall min="1" max="5">%s</overall>
        </ratings>
        <title>%s</title>
        <reviewer>
            <name is_anonymous="false">%s</name>
        </reviewer>
        <review_timestamp>%sT00:00:00.000Z</review_timestamp>
    </review>
</reviews>""" % (row[11], row[12], row[13], row[14], row[1], row[2],
        row[8],row[3],row[4], row[5], row[6], row[9])

with open('output.xml', 'w') as f:
    f.write('\n'.join([convert_row(row) for row in data]))
