import requests

from send_email import send_email

api_key = "2f414d3088344788bf61acda0758d369"
url = "https://newsapi.org/v2/everything?q=tesla" \
      "&from=2023-11-03&sortBy=publishedAt&apiKey=" \
      "2f414d3088344788bf61acda0758d369"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"]:
      if article["title"] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
