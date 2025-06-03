import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load dataset
csv_file = "addiction_population_data.csv"  # Change this to your actual CSV file
df = pd.read_csv(csv_file)

# Initialize Graph
G = nx.Graph()

# Define attributes for relationships
attributes = ["country", "city", "education_level", "employment_status",
              "mental_health_status", "smokes_per_day", "drinks_per_week",
              "has_health_issues", "therapy_history"]

# Add Nodes (Individuals and Attributes)
for _, row in df.iterrows():
    person_id = row["id"]
    
    # Add person as node
    G.add_node(person_id, label=row["name"])  
    
    # Connect person to attributes
    for attr in attributes:
        if pd.notna(row[attr]):  # Avoid NaN values
            G.add_node(row[attr])
            G.add_edge(person_id, row[attr])

# Generate graph layout
pos = nx.spring_layout(G)  # Adjusts node placement nicely

# Draw graph
plt.figure(figsize=(15, 15))
nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", 
        font_size=10, edge_color="gray")

# Save as JPG
plt.savefig("knowledge_graph.jpg", dpi=300)
plt.show()

print("Knowledge Graph saved successfully as 'knowledge_graph.jpg'!")