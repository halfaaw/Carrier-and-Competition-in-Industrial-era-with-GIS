import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import os

def main():
    print("Memulai proses analisis spasial GIS...")
    
    # 1. SETUP DIREKTORI OUTPUT
    os.makedirs("outputs/charts", exist_ok=True)
    
    # 2. LOAD DATA
    try:
        df = pd.read_csv("data/assets_data.csv")
    except FileNotFoundError:
        print("Error: File data/assets_data.csv tidak ditemukan.")
        return

    # 3. PREPROCESSING & GEOMETRY CONVERSION
    geometry = [Point(xy) for xy in zip(df['longitude'], df['latitude'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry)
    
    hub_point = gdf[gdf['category'] == 'Hub'].geometry.iloc[0]
    hub_gdf = gpd.GeoDataFrame(index=[0], geometry=[hub_point])
    
    radius_area = hub_gdf.buffer(0.05)
    
    # 4. ANALISIS SPASIAL
    gdf['within_radius'] = gdf.geometry.within(radius_area.geometry.iloc[0])
    
    print("\n=== Ringkasan Analisis Spasial ===")
    print(gdf[['asset_id', 'category', 'within_radius']])
    
    # 5. OUTPUT GENERATION & VISUALIZATION
    with open("outputs/laporan_spasial.txt", "w") as f:
        f.write("=== LAPORAN ANALISIS SPASIAL GIS ===\n")
        f.write(f"Total Aset Dianalisis: {len(gdf)}\n")
        f.write(f"Aset Dalam Radius Layanan: {gdf['within_radius'].sum()}\n")
        f.write(f"Aset Di Luar Radius: {len(gdf) - gdf['within_radius'].sum()}\n")
        
    fig, ax = plt.subplots(figsize=(8, 8))
    
    gpd.GeoSeries(radius_area).plot(ax=ax, color='blue', alpha=0.2, edgecolor='blue', label='Radius Pelayanan (Buffer)')
    hub_gdf.plot(ax=ax, color='blue', marker='*', markersize=200, label='Hub Pusat')
    
    gdf[gdf['within_radius'] == True].plot(ax=ax, color='green', markersize=60, label='Aset Terlayani (Dalam Radius)')
    gdf[gdf['within_radius'] == False].plot(ax=ax, color='red', markersize=60, label='Aset Luar Jangkauan')
    
    plt.title('Pemetaan Radius Pelayanan Aset (GIS Automation)')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    output_chart_path = "outputs/charts/spatial_map.png"
    plt.savefig(output_chart_path)
    plt.close()
    
    print(f"\nAnalisis selesai! Peta spasial disimpan di '{output_chart_path}'.")

if __name__ == "__main__":
    main()
