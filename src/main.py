from serp import google_search

query = input("Enter the term you want to search on google:")
results = google_search(query)
for i in results:
    print(i)