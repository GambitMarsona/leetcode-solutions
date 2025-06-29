
"""
Skrypt do pobrania zadań z LeetCode użytkownika i zliczenia liczby rozwiązań AC według poziomu trudności:
- Easy
- Medium
- Hard
"""

import requests
import sys

# Wprowadź swoją nazwę użytkownika LeetCode:
USERNAME = "0JpRJWgg8O"

GRAPHQL_URL = "https://leetcode.com/graphql"
QUERY = """
query getUserStats($username: String!) {
    matchedUser(username: $username) {
        submitStats {
            acSubmissionNum {
                difficulty
                count
            }
        }
    }
}
"""


def fetch_solution_counts(username):
    """Pobiera dane z LeetCode GraphQL API i zwraca słownik z liczbą rozwiązań AC dla każdego poziomu trudności."""
    variables = {"username": username}
    try:
        resp = requests.post(GRAPHQL_URL, json={"query": QUERY, "variables": variables})
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print(f"Błąd podczas pobierania danych z LeetCode: {e}", file=sys.stderr)
        sys.exit(1)

    stats = data.get("data", {}).get("matchedUser", {}).get("submitStats", {}).get("acSubmissionNum", [])
    counts = {"Easy": 0, "Medium": 0, "Hard": 0}
    for entry in stats:
        diff = entry.get("difficulty")
        if diff in counts:
            counts[diff] = entry.get("count", 0)
    return counts


def main():
    if USERNAME == "TwojaNazwaUzytkownika":
        print("Proszę ustawić zmienną USERNAME na swoją nazwę użytkownika LeetCode.", file=sys.stderr)
        sys.exit(1)

    counts = fetch_solution_counts(USERNAME)
    print("LeetCode solutions count by difficulty for user:")
    for level in ("Easy", "Medium", "Hard"):
        print(f"{level}: {counts[level]}")


if __name__ == "__main__":
    main()
