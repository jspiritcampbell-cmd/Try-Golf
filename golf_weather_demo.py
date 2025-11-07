import streamlit as st
from datetime import datetime, timedelta
import random

# Page configuration
st.set_page_config(
    page_title="Golf Weather Forecast",
    page_icon="⛳",
    layout="wide"
)

# Title and description
st.title("⛳ Golf Weather Forecast")
st.markdown("Find the best days for your golf game in the next 5 days!")
st.info("🔧 Demo Mode: Using simulated weather data")

# Sidebar for location input
st.sidebar.header("📍 Location Settings")
city = st.sidebar.text_input("Enter City Name", value="Nashville")

st.sidebar.markdown("---")
st.sidebar.markdown("### Optimal Golf Conditions")
st.sidebar.markdown("""
- Temperature: 60-85°F
- Wind Speed: < 15 mph
- No precipitation
- Low humidity
""")

def generate_mock_weather_data(city):
    """Generate realistic mock weather data"""
    weather_conditions = [
        "clear sky",
        "few clouds",
        "scattered clouds",
        "partly cloudy",
        "overcast clouds",
        "light rain",
        "sunny"
    ]
    
    daily_forecasts = {}
    
    for i in range(5):
        date = (datetime.now() + timedelta(days=i+1)).date()
        
        # Generate realistic weather variations
        base_temp = random.uniform(55, 85)
        temp = round(base_temp, 1)
        wind_speed = round(random.uniform(3, 20), 1)
        humidity = random.randint(30, 85)
        rain = 0 if random.random() > 0.2 else round(random.uniform(0.1, 5), 1)
        description = random.choice(weather_conditions)
        
        daily_forecasts[date] = {
            'temp': temp,
            'wind': wind_speed,
            'humidity': humidity,
            'rain': rain,
            'description': description
        }
    
    return daily_forecasts

def calculate_golf_score(temp, wind_speed, humidity, rain):
    """Calculate golf-friendliness score (0-100)"""
    score = 100
    
    # Temperature scoring (optimal: 65-80°F)
    if 65 <= temp <= 80:
        score += 0
    elif 60 <= temp < 65 or 80 < temp <= 85:
        score -= 10
    elif 55 <= temp < 60 or 85 < temp <= 90:
        score -= 20
    else:
        score -= 40
    
    # Wind scoring
    if wind_speed < 10:
        score += 0
    elif wind_speed < 15:
        score -= 15
    else:
        score -= 30
    
    # Humidity scoring
    if humidity < 60:
        score += 0
    elif humidity < 75:
        score -= 10
    else:
        score -= 20
    
    # Rain penalty
    if rain > 0:
        score -= 50
    
    return max(0, min(100, score))

def get_rating(score):
    """Convert score to rating"""
    if score >= 80:
        return "🏌️ Excellent", "green"
    elif score >= 60:
        return "👍 Good", "lightgreen"
    elif score >= 40:
        return "😐 Fair", "orange"
    else:
        return "❌ Poor", "red"

# Main app logic
if st.button("🔍 Get Forecast", type="primary"):
    with st.spinner("Generating weather forecast..."):
        # Generate mock data
        daily_forecasts = generate_mock_weather_data(city)
        
        st.success(f"Weather forecast for {city}")
        
        # Calculate scores for each day
        for date in daily_forecasts:
            forecast = daily_forecasts[date]
            score = calculate_golf_score(
                forecast['temp'], 
                forecast['wind'], 
                forecast['humidity'], 
                forecast['rain']
            )
            rating, color = get_rating(score)
            daily_forecasts[date]['score'] = score
            daily_forecasts[date]['rating'] = rating
            daily_forecasts[date]['color'] = color
        
        # Display forecast cards
        st.markdown("### 📅 5-Day Forecast")
        
        cols = st.columns(5)
        for idx, (date, forecast) in enumerate(daily_forecasts.items()):
            with cols[idx]:
                st.markdown(f"**{date.strftime('%a, %b %d')}**")
                st.markdown(
                    f"<div style='background-color:{forecast['color']}; padding:10px; border-radius:5px; text-align:center;'>"
                    f"<b>{forecast['rating']}</b><br>Score: {forecast['score']}/100</div>", 
                    unsafe_allow_html=True
                )
                st.metric("Temperature", f"{forecast['temp']:.0f}°F")
                st.metric("Wind", f"{forecast['wind']:.1f} mph")
                st.metric("Humidity", f"{forecast['humidity']}%")
                if forecast['rain'] > 0:
                    st.metric("Rain", f"{forecast['rain']:.1f} in")
                st.caption(forecast['description'].title())
        
        # Best day recommendation
        best_day = max(daily_forecasts.items(), key=lambda x: x[1]['score'])
        st.markdown("---")
        st.markdown(f"### 🏆 Best Day to Golf: **{best_day[0].strftime('%A, %B %d')}**")
        st.markdown(f"Golf Score: **{best_day[1]['score']}/100** - {best_day[1]['rating']}")
        
        # Show scoring breakdown for best day
        with st.expander("📊 See scoring details for best day"):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Temperature", f"{best_day[1]['temp']:.0f}°F")
            with col2:
                st.metric("Wind Speed", f"{best_day[1]['wind']:.1f} mph")
            with col3:
                st.metric("Humidity", f"{best_day[1]['humidity']}%")
            with col4:
                rain_val = f"{best_day[1]['rain']:.1f} in" if best_day[1]['rain'] > 0 else "None"
                st.metric("Rain", rain_val)

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. Enter your city name in the sidebar
    2. Click "Get Forecast" to see the 5-day golf weather forecast
    3. Each day is scored from 0-100 based on golf-friendly conditions
    4. Green days are excellent for golf, while red days are poor
    
    **Note:** This is a demo version using simulated data. For real weather data, 
    use the main app with an OpenWeatherMap API key.
    """)

# Footer
st.markdown("---")
st.markdown("*Demo mode: Using simulated weather data*")