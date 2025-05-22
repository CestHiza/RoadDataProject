# generate_roads.py
import pandas as pd
import random

# Generate synthetic road data
data = {
    "road_id": [f"RD{str(i).zfill(3)}" for i in range(1, 101)],
    "name": [f"Road {chr(65 + i % 26)}{i // 26 if i // 26 > 0 else ''}" for i in range(100)], # Unique road names
    "length_km": [round(random.uniform(1.0, 50.0), 1) for _ in range(100)],
    "condition": [random.choice(["Good", "Fair", "Poor"]) for _ in range(100)],
    # Generate simple WKT LINESTRING data for QGIS compatibility
    # LINESTRING(x1 y1, x2 y2)
    "geometry": [
        f"LINESTRING({random.randint(0, 90)} {random.randint(0, 90)}, {random.randint(0, 90)} {random.randint(0, 90)})"
        for _ in range(100)
    ]
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("roads.csv", index=False)

print("roads.csv generated successfully with 100 roads.")
print("Each road has a simple WKT LINESTRING geometry, e.g., LINESTRING(x1 y1, x2 y2).")