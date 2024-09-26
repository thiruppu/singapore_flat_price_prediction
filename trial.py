import streamlit as st
import pandas as pd
import streamlit_lottie
from streamlit_lottie import st_lottie_spinner
import json
from streamlit_option_menu import option_menu
import pickle
import numpy as np



def input_data(var1, var2, var3, var4, var5, var6, var7, var8, var9, var10):
    # Load the trained model
    with open('rf_model.pkl', 'rb') as file:
        guvi = pickle.load(file)

    # Prepare the input features as a numpy array
    input_features = [var1, var2, var3, var4, var5, var6, var7, var8, var9, var10]
    input_features_reshaped = np.array(input_features).reshape(1, -1)  # Correct reshaping

    # Make prediction
    prediction = guvi.predict(input_features_reshaped)
    
    # Return the predicted value
    return prediction[0]








# Set page layout to wide
st.set_page_config(layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
# Set the background color using CSS
lottie_streamlit = load_lottiefile("Animation - 1726125457200.json")
st.markdown(
    """
    <style>
    .stApp{
        background-color: #12343b;
        
    }
    .custom-text {
    color: #000000; /* Orange red */
    font-size: 20px;
    font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Creating the main menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Title of the menu
        options=["Overview", "Prediction","Contact"],  # Menu options
        icons=["house", "bar-chart","envelope"],  # Icons for each option
        menu_icon="cast",  # Menu icon
        default_index=0,  # Default selected option
        styles={
        "container": {"padding": "0!important", "background-color": "darkcyan"},
        "icon": {"color": "black", "font-size": "12px"},
        "nav-link": {
            "font-family": "serif",
            "font-size": "18px",
            "text-align": "left",
            #"margin": "0px",
            "color": "#d5e3ec",
        },
        "nav-link-selected": {"background-color": "#d5e3ec", "color": "black"},
    }

)
if selected == "Overview":
    st.title("Singapore Resale Flat Prices Prediction ")
    st.write("The aim of this project is to predict the resale prices of Housing Development Board (HDB) flats in Singapore using various machine learning models. Accurate predictions of resale flat prices can benefit homeowners, potential buyers, real estate agents, and policymakers by providing insights into price trends and housing affordability.")
    st.divider()
    #st.write("This is an example with a light blue background!")
    col1_1,col1_2 = st.columns([6,3])
    with col1_1:
        
        st.subheader("Tools Used:")
        a,b,c,d = st.columns(4)
        with a:
            st.image("Python (2).png")
            st.write("    Python")
        with b:
            st.image("scikit-learn (1).png")
            st.write(" Scikit-Learn")
        with c:
            st.image("Pandas (1).png")
            st.write("  Pandas")
        with d:
            st.image("Streamlit (1).png")
            st.write(" Streamlit")
        st.subheader("Model Used: Random Forest Regression")
        st.subheader("Accuracy : 96.92%")
        st.subheader("Application :")
        st.write("For Buyers: The application allows potential buyers to assess the market value of flats based on their preferences, helping them avoid overpaying for a property.")
        st.write("For Sellers: Sellers can use the tool to set competitive pricing for their flats by understanding current market trends and comparable prices.")
        st.write("For Real Estate Agents: The model offers real-time insights into flat prices, assisting agents in providing data-driven guidance to their clients.")
        
    with col1_2:

        st.image("pexels-jovydas-2462015.jpg")
        
    st.divider()
    col1_1, col1_2, col1_3 = st.columns(3)
    with col1_1:
        st.image("linkedin.png")
        st.write("[LinkedIn](https://www.linkedin.com/in/thiruppugazhan-s-277705282/)")
    with col1_2:
        st.image("instagram.png")
        st.write("[Instagram](https://instagram.com/_thiruppugazhan)")
        
    with col1_3:
        st.image("github.png")
        st.write("[GitHub](https://github.com/thiruppu)")

elif selected == "Prediction":
    st.markdown(
    """
    <style>
    .stApp{
        background-color: #d5e3ec;
        font-color: black;
        
    }
    h1, h2, h3, h4, h5, h6 {
        color: black !important; /* Set header text color to black */
    }
    .custom-text {
        color: #000000;
        font-size: 20px;
        font-weight: bold;
    }
    /* Set text color for input widgets */
    div[data-baseweb="input"] > div {
        color: black !important;
    }
    hr {
        border-color: darkblue;
    }
    </style>
    
    """,
    
    unsafe_allow_html=True
    )
    st.title("Prices Prediction part:")
    st.divider()
    col3_1,col3_2 = st.columns([4,6])
    with col3_1:
        st.lottie(lottie_streamlit)
    with col3_2:
        col3_3,col3_4 = st.columns(2)
        with col3_3:
            var1 = st.selectbox("Select Town",options=["ANG MO KIO","BEDOK","BISHAN","BUKIT BATOK","BUKIT MERAH","BUKIT PANJANG","BUKIT TIMAH","CENTRAL AREA","CHOA CHU KANG","CLEMENTI","GEYLANG","HOUGANG","JURONG EAST","JURONG WEST","KALLANG/WHAMPOA","LIM CHU KANG","MARINE PARADE","PASIR RIS","PUNGGOL","QUEENSTOWN","SEMBAWANG","SENGKANG","SERANGOON","TAMPINES","TOA PAYOH","WOODLANDS","YISHUN"])
            if var1 == "ANG MO KIO":
                int_var1 = 0
            if var1 == "BEDOK":
                int_var1 = 1
            if var1 == "BISHAN":
                int_var1 = 2
            if var1 == "BUKIT BATOK":
                int_var1 = 3
            if var1 == "BUKIT MERAH":
                int_var1 = 4
            if var1 == "BUKIT PANJANG":
                int_var1 = 5
            if var1 == "BUKIT TIMAH":
                int_var1 = 6
            if var1 == "CENTRAL AREA":
                int_var1 = 7
            if var1 == "CHOA CHU KANG":
                int_var1 = 8
            if var1 == "CLEMENTI":
                int_var1 = 9
            if var1 == "GEYLANG":
                int_var1 = 10
            if var1 == "HOUGANG":
                int_var1 = 11
            if var1 == "JURONG EAST":
                int_var1 = 12
            if var1 == "JURONG WEST":
                int_var1 = 13
            if var1 == "KALLANG/WHAMPOA":
                int_var1 = 14
            if var1 == "LIM CHU KANG":
                int_var1 = 15
            if var1 == "MARINE PARADE":
                int_var1 = 16
            if var1 == "PASIR RIS":
                int_var1 = 17
            if var1 == "PUNGGOL":
                int_var1 = 18
            if var1 == "QUEENSTOWN":
                int_var1 = 19
            if var1 == "SEMBAWANG":
                int_var1 = 20
            if var1 == "SENGKANG":
                int_var1 = 21
            if var1 == "SERANGOON":
                int_var1 = 22
            if var1 == "TAMPINES":
                int_var1 = 23
            if var1 == "TOA PAYOH":
                int_var1 = 24
            if var1 == "WOODLANDS":
                int_var1 = 25
            if var1 == "YISHUN":
                int_var1 = 26
            var2 = st.selectbox("Flat Type",options=["1 ROOM","2 ROOM","3 ROOM","4 ROOM","5 ROOM","EXECUTIVE","MULTI GENERATION","MULTI-GENERATION"])
            if var2 == "1 ROOM":
                int_var2 = 0
            if var2 == "2 ROOM":
                int_var2 = 1
            if var2 == "3 ROOM":
                int_var2 = 2
            if var2 == "4 ROOM":
                int_var2 = 3
            if var2 == "5 ROOM":
                int_var2 =4 
            if var2 == "EXECUTIVE":
                int_var2 = 5
            if var2 == "MULTI GENERATION":
                int_var2 = 6
            
            var3 = st.selectbox("Flat Model",options=["2-ROOM","3GEN","ADJOINED FLAT","APARTMENT","DBSS","IMPROVED","IMPROVED-MAISONETTE","MAISONETTE","MODEL A","MODEL A-MAISONETTE","MODEL A2","MULTI GENERATION","NEW GENERATION","PREMIUM APARTMENT","PREMIUM APARTMENT LOFT","PREMIUM MAISONETTE","SIMPLIFIED","STANDARD","TERRACE","TYPE S1","TYPE S2"])
            if var3 == "2-ROOM":
                int_var3 =0
            if var3 == "3GEN":
                int_var3 =1
            if var3 == "ADJOINED FLAT":
                int_var3 =2
            if var3 == "APARTMENT":
                int_var3 =3
            if var3 == "DBSS":
                int_var3 =4
            if var3 == "IMPROVED":
                int_var3 =5
            if var3 == "IMPROVED-MAISONETTE":
                int_var3 =6
            if var3 == "MAISONETTE":
                int_var3 =7
            if var3 == "MODEL A":
                int_var3 =8
            if var3 == "MODEL A-MAISONETTE":
                int_var3 =9
            if var3 == "MODEL A2":
                int_var3 =10
            if var3 == "MULTI GENERATION":
                int_var3 =11
            if var3 == "NEW GENERATION":
                int_var3 =12
            if var3 == "PREMIUM APARTMENT":
                int_var3 =13
            if var3 == "PREMIUM APARTMENT LOFT":
                int_var3 =14
            if var3 == "PREMIUM MAISONETTE":
                int_var3 =15
            if var3 == "SIMPLIFIED":
                int_var3 =16
            if var3 == "STANDARD":
                int_var3 =17
            if var3 == "TERRACE":
                int_var3 =18
            if var3 == "TYPE S1":
                int_var3 =19
            if var3 == "TYPE S2":
                int_var3 = 20
            var4 = st.text_input("",placeholder="Block")
            int_var4 = int(var4) if var4 else 0
            var5 = st.text_input("",placeholder="Floor area in sqm")
            int_var5 = float(var5) if var5 else 0
        with col3_4:
            var6 = st.text_input("",placeholder="Lease commense date")
            int_var6 = int(var6) if var6 else 0
            var7 = st.text_input("",placeholder="Year")
            int_var7 = int(var7) if var7 else 0
            var8 = st.text_input("",placeholder="Month")
            int_var8 = int(var8)if var8 else 0
            var9 = st.text_input("",placeholder="Storey range from")
            int_var9 = int(var9)if var9 else 0
            var10 = st.text_input("",placeholder="Storey range to")
            int_var10 = int(var10)if var10 else 0
            prediction_button = st.button("Predict")
            if prediction_button:            
                # Get the prediction
                prediction = input_data(int_var1,int_var2,int_var3,int_var4,int_var5,int_var6,int_var7,int_var8,int_var9,int_var10)
                if prediction_button is not None:
                    st.header(f"Prediction Price:")
                    st.header(f"${prediction}")
    st.divider()
    a,b,c = st.columns(3)
    with b:
        st.write(":grey[Crafted in Mangalore]🐬")
elif selected == "Contact":
        st.markdown(
    """
    <style>
    .stApp{
        background-color: #12343b;
        font-color: black;
        
    }
    h1 {
        color: black; /* Set the title text color to black */
    }
    .custom-text {
        color: #000000;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    
    """,
    
    unsafe_allow_html=True
    )    

        st.header("Drop your details:")
        st.divider()
        st.text_input("Name:")
        st.text_input("E-Mail:")
        st.text_input("Mobile:")
        st.text_input("Feedback:")
        st.button("Submit")
        st.divider()
        a,b,c = st.columns(3)
        with b:
            st.write(":grey[Crafted in Mangalore]🐬")
