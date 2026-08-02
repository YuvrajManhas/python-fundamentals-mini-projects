import requests

def get_profile(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 404:
            print("No such profile exists.")
            return

        response.raise_for_status()

        data = response.json()

        name = data.get("name", "N/A")
        login = data.get("login", "N/A")
        bio = data.get("bio", "N/A")
        followers = data.get("followers", 0)
        following = data.get("following", 0)
        repos = data.get("public_repos", 0)
        company = data.get("company", "N/A")
        location = data.get("location", "N/A")
        blog = data.get("blog", "N/A")
        created = data.get("created_at", "N/A")

        print("=" * 40)
        print("GitHub Profile")
        print("=" * 40)
        print("Name:", name)
        print("Username:", login)
        print("Bio:", bio)
        print("Followers:", followers)
        print("Following:", following)
        print("Repositories:", repos)
        print("Company:", company)
        print("Location:", location)
        print("Website:", blog)
        print("Created:", created)

    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.ConnectionError:
        print("No Internet!")
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except Exception as e:
        print(e)

get_profile("YuvrajManhas")