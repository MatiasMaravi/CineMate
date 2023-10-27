# Peliculas que le gustan al usuario

data={
    "USU1": ["Rey Leon", "Toy Story", "Dumbo", "Cars"],
    "USU2": ["Titanic", "Toy Story", "Libro de la Selva", "Dumbo"],
    "USU3": ["Toy Story", "Cars", "", "Libro de la Selva"],
}

import json
from supabase import create_client

url = "https://inlhowinxzuskmodrpix.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"
supabase = create_client(url, key)

table_1 = 'preference_actor'

# insertar peliculas que le gustan al usuario

for i in data:
    for j in data[i]:
        if j != "":
            supabase.table(table_1).insert({"id_usuario": i, "peliculas": j}).execute()