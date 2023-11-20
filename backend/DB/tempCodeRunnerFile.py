data = supabase.table('r_history').select('*').eq('user', "Ana").filter('actor', 'eq', "Bill Skarsgård").filter('genre', 'eq', "Terror").filter('interaction', 'eq', 1).execute()
