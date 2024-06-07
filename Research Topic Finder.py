import requests
from urllib.parse import urlencode


def get_url(title, authors, journal):
    query = f"{title} {authors} {journal}"
    params = {'query': query}
    url = f"https://api.crossref.org/works?{urlencode(params)}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["message"]["items"]:
            paper = data["message"]["items"][0]
            if "URL" in paper:
                pub_url = paper["URL"]
                print(f"URL: {pub_url}")
            else:
                print("No URL found for the provided details.")
        else:
            print("No results found for the provided details.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def main():
    title = input("Enter the title: ")
    authors = input("Enter the authors: ")
    journal = input("Enter the journal: ")

    get_url(title, authors, journal)


if __name__ == "__main__":
    main()
