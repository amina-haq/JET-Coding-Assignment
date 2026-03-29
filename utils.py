import requests

def fetch_restaurants(postcode):
    # builds API url 
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

    # makes a GET request to API, adding user-agent to avoid being blocked
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    # if request fails an empty list is returned
    if response.status_code != 200:
        return []

    # convert JSON response to a python dictionary
    data = response.json()
    restaurants = data.get("restaurants", [])[:10] # first 10 restaurants

    result = []
    for r in restaurants:
        # combinds cusine name into string
        cuisines = ", ".join([c.get("name") for c in r.get("cuisines", [])])

        # gets restaurant rating
        rating = r.get("rating", {}).get("starRating")

        # formats the address
        addr = r.get("address", {})
        address = f"{addr.get('firstLine')}, {addr.get('city')}, {addr.get('postalCode')}"

        # adds the restaurant data into a list
        result.append({
            "name": r.get("name"),
            "cuisines": cuisines,
            "rating": rating,
            "address": address
        })

    return result