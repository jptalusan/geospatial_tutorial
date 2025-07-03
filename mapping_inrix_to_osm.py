import os
from geo_mapper_api import inrix_to_osm
# Dealing with inrix, maps inrix segment data to OSM nodes, this will take a while.
if 'geo_work' not in os.getcwd():
    os.chdir(os.path.join(os.getcwd(), 'geo_work'))
if __name__ == '__main__':
    DATA_DIR = "./data"
    geojson_path = os.path.join(DATA_DIR, 'USA_Tennessee.geojson')
    csv_path = os.path.join(DATA_DIR, 'USA_Tennessee.csv')
    county_name = ['WILLIAMSON']
    # you can use parallel if not in a notebook (seems serial is broken so dont use a notebook)
    df = inrix_to_osm.parallel(geojson_path, csv_path, county_name, threshold_distance=25)
    df.to_csv(f"{DATA_DIR}/williamson_county_tn_inrix_osm.csv", index=False)
    print(df)