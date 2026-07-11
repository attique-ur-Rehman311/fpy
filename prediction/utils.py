import csv
from .models import CarData

def import_csv():
    with open('data\data_sales.csv ', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            CarData.objects.create(
                model=row['Model'],
                year=int(row['Year']),
                region=row['Region'],
                color=row['Color'],
                fuel_type=row['Fuel_Type'],
                transmission=row['Transmission'],
                engine_size_l=float(row['Engine_Size_L']),
                mileage_km=int(row['Mileage_KM']),
                price_usd=float(row['Price_USD']),
                sales_volume=int(row['Sales_Volume']),
                sales_classification=row['Sales_Classification']
            )
