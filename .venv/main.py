import streamlit as st
import requests

api_key = "hMheE6K39lAzAAvFnXdRdPlVYUqz6OdmfdLl8L8S"

url = "https://api.nasa.gov/planetary/apod?api_key=hMheE6K39lAzAAvFnXdRdPlVYUqz6OdmfdLl8L8S"

request = requests.get(url)

# Get a dictionary of the data
content = request.json()

# Extract the image title, url and explanation
title = content["title"]
description = content["explanation"]
picture_url = content["hdurl"]

# Download the image
picture = requests.get(picture_url)
with open("image.jpg", "wb") as file:
    file.write(picture.content)

# Making the site
st.title(title)
st.image("image.jpg")
st.write(description)