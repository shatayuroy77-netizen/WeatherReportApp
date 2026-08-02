import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# WEATHER_API_KEY = st.secrets["WEATHER_API_KEY"]
WEATHER_API_KEY =os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    WEATHER_API_KEY = st.secrets["WEATHER_API_KEY"]
    # print("API_KEY is missing. Please add it to your .env file.")
if not WEATHER_API_KEY:
    # If API_KEY is found, print the value.
    st.error("WEATHER_API_KEY not found.")
    st.stop

st.title("🌦️ Weather App")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):

    if city:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:

            # Weather Details
            temperature = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]

            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            condition = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]

            wind_speed = data["wind"]["speed"]
            wind_degree = data["wind"]["deg"]

            visibility = data["visibility"] / 1000
            clouds = data["clouds"]["all"]

            country = data["sys"]["country"]
            city_name = data["name"]

            # Weather Icon
            icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
            st.image(icon_url, width=100)

            st.subheader(f"📍 Weather for {city_name}, {country}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("🌡️ Temperature", f"{temperature} °C")
                st.metric("🥵 Feels Like", f"{feels_like} °C")
                st.metric("🔻 Min Temp", f"{temp_min} °C")
                st.metric("🔺 Max Temp", f"{temp_max} °C")
                st.metric("💧 Humidity", f"{humidity}%")

            with col2:
                st.metric("💨 Wind Speed", f"{wind_speed} m/s")
                st.metric("🧭 Wind Direction", f"{wind_degree}°")
                st.metric("☁️ Clouds", f"{clouds}%")
                st.metric("👁️ Visibility", f"{visibility} km")
                st.metric("📈 Pressure", f"{pressure} hPa")

            st.success(f"🌥️ Condition: {condition.title()}")

        else:
            st.error("❌ City not found or API error.")

    else:
        st.warning("⚠️ Please enter a city name.")