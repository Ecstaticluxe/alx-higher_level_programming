#!/usr/bin/node
def get_movie_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        movie_data = response.json()
        characters = movie_data['characters']
        for character_url in characters:
            character_data = requests.get(character_url).json()
            print(character_data['name'])
    else:
        print(f"Failed to retrieve movie data. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <movie_id>")
        sys.exit(1)
movie_id = sys.argv[1]
    get_movie_characters(movie_id)

