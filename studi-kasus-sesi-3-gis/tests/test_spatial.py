import unittest
import pandas as pd
import os
from shapely.geometry import Point
import geopandas as gpd

class TestSpatialDataQuality(unittest.TestCase):
    def setUp(self):
        self.file_path = "data/assets_data.csv"
        
    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.file_path), "File dataset assets_data.csv tidak ditemukan!")
        
    def test_no_missing_values(self):
        if os.path.exists(self.file_path):
            df = pd.read_csv(self.file_path)
            self.assertFalse(df.isnull().values.any(), "Terdapat missing values pada dataset spasial!")
            
    def test_geometry_conversion(self):
        df = pd.DataFrame({
            'latitude': [-3.799],
            'longitude': [102.259]
        })
        geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry)
        self.assertEqual(len(gdf), 1)
        self.assertIsInstance(gdf.geometry.iloc[0], Point)

if __name__ == 'main':
    unittest.main()
