import streamlit as st
import requests
import pycountry
import folium
from streamlit_folium import folium_static

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[0]
    else:
        return None

def display_country_info():
    st.title("🌍 Country Information Finder")
    country_name = st.text_input("Enter country name:").strip()
    
    if st.button("Get Info") and country_name:
        country_data = get_country_info(country_name)
        
        if country_data:
            st.subheader(f"Country: {country_data['name']['common']}")
            st.write(f"**Capital:** {country_data.get('capital', ['N/A'])[0]}")
            st.write(f"**Population:** {country_data.get('population', 'N/A'):,}")
            st.write(f"**Region:** {country_data.get('region', 'N/A')}")
            st.write(f"**Subregion:** {country_data.get('subregion', 'N/A')}")
            st.write(f"**Timezone(s):** {', '.join(country_data.get('timezones', ['N/A']))}")
            
            # Show flag
            flag_url = country_data['flags']['png']
            st.image(flag_url, caption=f"Flag of {country_data['name']['common']}", width=200)
            
            # Show map
            latlng = country_data.get('latlng', [0, 0])
            st.subheader("🌍 Map Location")
            country_map = folium.Map(location=latlng, zoom_start=4)
            folium.Marker(latlng, tooltip=country_data['name']['common']).add_to(country_map)
            folium_static(country_map)
        else:
            st.error("Country not found! Please check the name and try again.")

if __name__ == "__main__":
    display_country_info()
