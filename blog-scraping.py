# imports dependencies
import requests
from bs4 import BeautifulSoup
from csv import writer

# Saves the content of the web page into a variable
response = requests.get('https://www.rithmschool.com/blog')

# Creates a new instance of beautiful soup
soup = BeautifulSoup(response.text, 'html.parser')

# finds elements in bs
articles = soup.select("article")

# Creates a vriable file to open and modify
with open("blog_data.csv", "w") as csv_file:
  # Creates a new writer object to modify the file
  csv_writer = writer(csv_file)
  # Writes the headers
  csv_writer.writerow(["titie", "link", "data"])

  # Loops through each article and writes it as a row in the csv file
  for article in articles:
    # Finds first anchor tag
    anchor = article.find("a")
    # Finds the texe of the first a tag in each post
    title = anchor.getText()
    # Finds the link to each post
    href = anchor["href"]
    # Finds the time each post was posted
    time = article.find("time")["datetime"]
    csv_writer.writerow([title, href, time])
