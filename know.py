import pandas as pd
import pickle

import networkx as nx

# Load dataset
csv_file = "addiction_population_data.csv"  # Ensure this is the correct path
df = pd.read_csv(csv_file)

# Initialize Graph
G = nx.Graph()

# Add Nodes (Individuals)
for _, row in df.iterrows():
    person_id = row["id"]
    
    # Add person as node
    G.add_node(person_id, name=row["name"], age=row["age"], gender=row["gender"])

    # Add relationships based on relevant attributes
    attributes = ["country", "city", "education_level", "employment_status",
                  "mental_health_status", "smokes_per_day", "drinks_per_week"]

    for attr in attributes:
        if pd.notna(row[attr]):  # Avoid NaN values
            G.add_node(row[attr], type="attribute")
            G.add_edge(person_id, row[attr], relationship=attr)

# Save graph (optional)
with open("knowledge_graph.gpickle", "wb") as f:
    pickle.dump(G, f)

print("Knowledge Graph saved successfully!")
