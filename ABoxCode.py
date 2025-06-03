import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, XSD, URIRef

# Load the CSV data
df = pd.read_csv("addiction_population_data.csv")

# Define namespaces
EX = Namespace("http://example.org/ns#")
QB = Namespace("http://purl.org/linked-data/cube#")

# Create RDF graph
g = Graph()
g.bind("ex", EX)
g.bind("qb", QB)

# Iterate over each row and add triples
for index, row in df.iterrows():
    person_uri = URIRef(f"http://example.org/ns#obs{row['id']}")
    g.add((person_uri, RDF.type, QB.Observation))

    g.add((person_uri, EX.personID, Literal(int(row['id']), datatype=XSD.integer)))
    g.add((person_uri, EX.name, Literal(row['name'])))
    g.add((person_uri, EX.age, Literal(int(row['age']), datatype=XSD.integer)))
    g.add((person_uri, EX.gender, Literal(row['gender'])))
    g.add((person_uri, EX.country, Literal(row['country'])))
    g.add((person_uri, EX.city, Literal(row['city'])))
    g.add((person_uri, EX.educationLevel, Literal(row['education_level'])))
    g.add((person_uri, EX.employmentStatus, Literal(row['employment_status'])))
    g.add((person_uri, EX.annualIncomeUSD, Literal(float(row['annual_income_usd']), datatype=XSD.decimal)))
    g.add((person_uri, EX.maritalStatus, Literal(row['marital_status'])))
    g.add((person_uri, EX.childrenCount, Literal(int(row['children_count']), datatype=XSD.integer)))
    g.add((person_uri, EX.smokesPerDay, Literal(int(row['smokes_per_day']), datatype=XSD.integer)))
    g.add((person_uri, EX.drinksPerWeek, Literal(int(row['drinks_per_week']), datatype=XSD.integer)))
    g.add((person_uri, EX.ageStartedSmoking, Literal(int(row['age_started_smoking']), datatype=XSD.integer)))
    g.add((person_uri, EX.ageStartedDrinking, Literal(int(row['age_started_drinking']), datatype=XSD.integer)))
    g.add((person_uri, EX.attemptsToQuitSmoking, Literal(int(row['attempts_to_quit_smoking']), datatype=XSD.integer)))
    g.add((person_uri, EX.attemptsToQuitDrinking, Literal(int(row['attempts_to_quit_drinking']), datatype=XSD.integer)))
    g.add((person_uri, EX.hasHealthIssues, Literal(bool(row['has_health_issues']))))
    g.add((person_uri, EX.mentalHealthStatus, Literal(row['mental_health_status'])))
    g.add((person_uri, EX.exerciseFrequency, Literal(row['exercise_frequency'])))
    g.add((person_uri, EX.dietQuality, Literal(row['diet_quality'])))
    g.add((person_uri, EX.sleepHours, Literal(float(row['sleep_hours']), datatype=XSD.decimal)))
    g.add((person_uri, EX.bmi, Literal(float(row['bmi']), datatype=XSD.decimal)))
    g.add((person_uri, EX.socialSupport, Literal(row['social_support'])))
    g.add((person_uri, EX.therapyHistory, Literal(row['therapy_history'])))

# Serialize to Turtle file
g.serialize(destination="abox.ttl", format="turtle")

print("✅ ABox TTL file 'abox.ttl' generated for all individuals.")
