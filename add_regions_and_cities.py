import pandas
from helps_app.models import City, Region

def cities():
    panda = pandas.read_excel('regions_cities.xlsx', sheet_name='goods')

    for row in panda.itertuples():
        a = Region(id=row[1],region_name=row[2])
        a.save()
        for city in row[3].split():
            if '_' in city:
                city = city.replace('_', ' ')
            b = City(region_id=row[1], city_name=city)
            b.save()

if __name__ == '__main__':
    cities()
