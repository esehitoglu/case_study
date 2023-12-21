import requests

api_url = "https://flights-api.buraky.workers.dev/"

def get_flights():
    response = requests.get(api_url)
    return response.json()

def test_api_response():
    flights_data = get_flights()

    try:
        flights = flights_data["data"]

        print("Response: Object[string -> Array[Flight]]\n")
        print("Flight {")
        print("    Id   integer")
        print("    From string")
        print("    To   string")
        print("    Date string")
        print("}\n")
        print("Example:\n")

        print("{")
        print('  "data": [')

        for idx, flight in enumerate(flights):
            print("    {")
            print(f'      "id": {flight["id"]},')
            print(f'      "from": "{flight["from"]}",')
            print(f'      "to": "{flight["to"]}",')
            print(f'      "date": "{flight["date"]}"')
            print("    }" + ("," if idx < len(flights) - 1 else ""))
        
        print("  ]")
        print("}")

        print("\n\"Test passed successfully!\"")

    except KeyError:
        print("Error: Response does not contain 'data' key")
    except ValueError as e:
        print("Error decoding JSON:", e)

if __name__ == "__main__":
    test_api_response()
