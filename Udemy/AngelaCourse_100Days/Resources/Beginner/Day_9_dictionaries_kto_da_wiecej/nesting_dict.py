#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a List in a Dictionary

travel_log = {
    "France": {"cities_visited_France: ": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited_Germany: ": ["Berlin", "Hamburg", "Stuttgart"], "total_visits: ": 10},
}

print(travel_log)

#Nesting Dictionary in a List

travel_log2= [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },

    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    }

]

print(travel_log2)