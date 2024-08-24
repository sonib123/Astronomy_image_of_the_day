# NASA APOD Streamlit Application

This Streamlit application fetches and displays NASA's Astronomy Picture of the Day (APOD) using the NASA API.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Requests

### Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required Python packages:
    ```sh
    pip install streamlit requests
    ```

3. Obtain a NASA API key from NASA API.

4. Replace the placeholder API key in the script with your actual API key:
    ```python
    api_key = "your_actual_api_key"
    ```

### Running the Application

1. Run the Streamlit application:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the application.

## Code Explanation

- **Importing Libraries:**
    ```python
    import streamlit as st
    import requests
    ```

- **Setting the API Key and URL:**
    ```python
    api_key = "your_actual_api_key"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    ```

- **Fetching Data from NASA API:**
    ```python
    request = requests.get(url)
    content = request.json()
    ```

- **Extracting and Displaying Data:**
    ```python
    title = content["title"]
    description = content["explanation"]
    picture_url = content["hdurl"]

    picture = requests.get(picture_url)
    with open("image.jpg", "wb") as file:
        file.write(picture.content)

    st.title(title)
    st.image("image.jpg")
    st.write(description)
    ```


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NASA API documentation: NASA API
- Streamlit documentation: Streamlit
- Requests documentation: Requests


