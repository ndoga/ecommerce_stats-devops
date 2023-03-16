import json
import boto3
import csv
from datetime import datetime
from collections import Counter

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Recupera il nome del bucket S3 e del file CSV dalla variabile event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    print(f'Bucket: {bucket_name}, File: {file_name}')

    # Scarica il file CSV dal bucket s3
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    csv_file = response['Body'].read().decode('utf-8')
    csv_lines = csv_file.split('\n')
    csv_reader = csv.DictReader(csv_lines)

    # Analizza i dati del file CSV
    sales_data = []
    for row in csv_reader:
        transaction_id = row['event_type']
        product_id = row['product_id']
        quantity = 1
        unit_price = float(row['price'])
        purchase_date = datetime.strptime(row['event_time'], '%Y-%m-%d %H:%M:%S %Z')
        geographic_area = row['user_session'].split('.')[0]
        sales_data.append({'transaction_id': transaction_id, 'product_id': product_id,
                           'quantity': quantity, 'unit_price': unit_price,
                           'purchase_date': purchase_date, 'geographic_area': geographic_area})

    # Genera il report in HTML
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

    # Scrive il report HTML nel file index.html nel bucket S3
    s3.put_object(Bucket=bucket_name, Key='index.html', Body=report_html)

    # Restituisce una risposta HTTP con un messaggio di successo
    response = {
        'statusCode': 200,
        'body': json.dumps('Report generato con successo e salvato in S3.')
    }
    return response
