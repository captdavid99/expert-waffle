import requests

# Replace 'your-username' with your actual GitHub username
GITHUB_USERNAME = 'your-username'

def fetch_github_profile(username):
    """Fetches and displays GitHub profile information for the given username."""
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        profile_data = response.json()
        # Display some profile details
        print("GitHub Profile Information:")
        print(f"Username: {profile_data['login']}")
        print(f"Name: {profile_data.get('name', 'Not available')}")
        print(f"Bio: {profile_data.get('bio', 'Not available')}")
        print(f"Public Repos: {profile_data['public_repos']}")
        print(f"Followers: {profile_data['followers']}")
        print(f"Following: {profile_data['following']}")
        print(f"Profile URL: {profile_data['html_url']}")
        print(f"Avatar URL: {profile_data['avatar_url']}")
    else:
        print(f"Failed to fetch profile for username: {username}. Status Code: {response.status_code}")

# Call the function to fetch and display GitHub profile information
fetch_github_profile(GITHUB_USERNAME)
