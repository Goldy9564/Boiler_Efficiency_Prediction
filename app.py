import streamlit as st
import pandas as pd
import joblib

# Load model

model = joblib.load(
    "models/boiler_efficiency_model.pkl"
)


# Page title

st.set_page_config(
    page_title="Boiler Efficiency Prediction",
    page_icon="⚙️",
    layout="wide"
)


st.title(
    "⚙️ Boiler Efficiency Prediction System"
)

st.write(
    "Machine Learning Based Performance Monitoring System"
)


# Input section

col1, col2 = st.columns(2)


with col1:

    unit_load = st.number_input(
        "Unit Load (MW)",
        value=350.0
    )

    coal_feed_rate = st.number_input(
        "Coal Feed Rate (Ton/hr)",
        value=165.0
    )

    main_steam_pressure = st.number_input(
        "Main Steam Pressure (bar)",
        value=170.0
    )

    main_steam_temperature = st.number_input(
        "Main Steam Temperature (°C)",
        value=540.0
    )

    feedwater_temperature = st.number_input(
        "Feedwater Temperature (°C)",
        value=245.0
    )


with col2:

    feedwater_flow = st.number_input(
        "Feedwater Flow (Ton/hr)",
        value=1100.0
    )

    flue_gas_temperature = st.number_input(
        "Flue Gas Temperature (°C)",
        value=145.0
    )

    oxygen_level = st.number_input(
        "Oxygen Level (%)",
        value=4.5
    )

    furnace_temperature = st.number_input(
        "Furnace Temperature (°C)",
        value=1250.0
    )

    ambient_temperature = st.number_input(
        "Ambient Temperature (°C)",
        value=30.0
    )


# Create engineered features

coal_per_mw = (
    coal_feed_rate /
    unit_load
)

steam_feedwater_difference = (
    main_steam_temperature -
    feedwater_temperature
)


# Prediction button

if st.button(
    "Predict Boiler Efficiency"
):

    input_data = pd.DataFrame([{

        "Unit_Load_MW":
            unit_load,

        "Coal_Feed_Rate_tph":
            coal_feed_rate,

        "Main_Steam_Pressure_bar":
            main_steam_pressure,

        "Main_Steam_Temperature_C":
            main_steam_temperature,

        "Feedwater_Temperature_C":
            feedwater_temperature,

        "Feedwater_Flow_tph":
            feedwater_flow,

        "Flue_Gas_Temperature_C":
            flue_gas_temperature,

        "Oxygen_Level_percent":
            oxygen_level,

        "Furnace_Temperature_C":
            furnace_temperature,

        "Ambient_Temperature_C":
            ambient_temperature,

        "Coal_per_MW":
            coal_per_mw,

        "Steam_Feedwater_Temp_Difference":
            steam_feedwater_difference
    }])


    prediction = model.predict(
        input_data
    )[0]


    st.success(
        f"Predicted Boiler Efficiency: {prediction:.2f}%"
    )


    # Performance message

    if prediction >= 90:

        st.success(
            "Performance Status: Excellent"
        )

    elif prediction >= 85:

        st.warning(
            "Performance Status: Normal"
        )

    else:

        st.error(
            "Performance Status: Low Efficiency"
        )
