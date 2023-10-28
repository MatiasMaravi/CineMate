import json
from supabase import create_client

url = "https://inlhowinxzuskmodrpix.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlubGhvd2lueHp1c2ttb2RycGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY5NjI5ODYsImV4cCI6MjAxMjUzODk4Nn0.jII7SbPyktiAuUrKirqQ6eD7_2uu-Mb8crpnT0MkMfo"
supabase = create_client(url, key)

table_1 = 'usuario'
table_2 = 'preference_actor'


# consulta a la tabla usuario

data_usuario = supabase.table(table_1).select("*").execute()
data_usuario = data_usuario.data

data_preference = {}

for i in data_usuario:
    #consultamos por cada usuario sus preferencias
    preferencia_usuario=supabase.table(table_2).select("*").eq('id_usuario', i['id']).execute()
    data_preference[i] = preferencia_usuario.data
    data_preference[i] = data_preference[i][:,5]

print(data_preference)
