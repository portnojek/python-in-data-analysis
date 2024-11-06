# Import the necessary functions from urllib.request
from urllib.request import urlopen, Request

# Specify the URL
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# Package the request using the Request() function
request = Request(url)

# Send the request and catch the response using urlopen(), assign it to 'response'
response = urlopen(request)

# Extract the response content using the read() method and store it in 'html'
html = response.read()

# Print the extracted HTML content
print(html)

# Be polite and close the response
response.close()