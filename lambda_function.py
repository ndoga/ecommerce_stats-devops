# E-Commerce Data Solutions
# Ver. 1.3 lambda_function.py
# Data recovery from .csv files and analysis

import csv
from datetime import datetime
from collections import Counter
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    
    # prelievo file name
    bucket_name = "prog1b"
    file_name = event["Records"][0]["s3"]["object"]["key"]
    print(file_name)

    s3_object = s3.get_object(Bucket=bucket_name, Key=file_name)
    s3_object_data = s3_object["Body"].read().decode('utf-8').splitlines()
    csv_data = csv.reader(s3_object_data)
    
    # estrazione dati dal file csv
    sales_data = []
    reader = csv.DictReader(s3_object_data, delimiter=',', quotechar='"')
    for row in reader:
        transaction_id = row['event_type']
        product_id = row['product_id']
        quantity = 1
        unit_price = float(row['price'])
        purchase_date = datetime.strptime(row['event_time'], '%Y-%m-%d %H:%M:%S %Z')
        geographic_area = row['user_session'].split('.')[0]
        sales_data.append({'transaction_id': transaction_id, 'product_id': product_id,
                           'quantity': quantity, 'unit_price': unit_price,
                           'purchase_date': purchase_date, 'geographic_area': geographic_area})

    # analisi dati e generazione report in html
    product_sales = Counter(item['product_id'] for item in sales_data)
    area_sales = Counter(item['geographic_area'] for item in sales_data)
    monthly_sales = Counter((item['purchase_date'].year, item['purchase_date'].month) for item in sales_data)

    report_html = '<html><body><h1>Report vendite</h1>'
    report_html += '<h2>Prodotti più venduti</h2><ul>'
    for product_id, sales_count in product_sales.most_common(10):
        report_html += '<li>Prodotto {} - {} vendite</li>'.format(product_id, sales_count)
    report_html += '</ul>'

    report_html += '<h2>Aree geografiche con maggiori entrate</h2><ul>'
    for area, sales_count in area_sales.most_common(10):
        report_html += '<li>Area {} - {} entrate</li>'.format(area, sales_count)
    report_html += '</ul>'

    report_html += '<h2>Mese con maggiori vendite</h2><ul>'
    year, month = monthly_sales.most_common(1)[0][0]
    report_html += '<li>Mese {}-{} - {} vendite</li>'.format(year, month, monthly_sales[(year, month)])
    report_html += '</ul></body></html>'

    # restituzione report in html
    return {'statusCode': 200, 'body': report_html}
