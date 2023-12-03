import requests
from send_email import send_email

topic = "tesla"

api_key = "2f414d3088344788bf61acda0758d369"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=2f414d3088344788bf61acda0758d369"\
      "language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
'''
for article in content["articles"][:20]:
      if article["title"] is not None:
            body = "Subject: Today's news" + body + article["title"] + "\n" \
                  + article["description"] \
                  + "\n" + article["url"] + 2 * "\n"
'''
try:
    for article in content.get("articles", [])[:20]:
        if article.get("title") is not None:
            body = "subject: Today's news" \
                    +"\n" + body + article["title"] + "\n" \
                    + article.get("description", "") \
                    + "\n" + article.get("url", "") + 2 * "\n"

    body = body.encode("utf-8")
    send_email(message=body)

except KeyError:
    print("The 'articles' key was not found in the API response.")


