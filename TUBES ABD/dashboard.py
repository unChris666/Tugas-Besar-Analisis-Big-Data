import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("output.csv", low_memory=False)

# Create a Streamlit app
st.title("Traffic Accident Analysis")

# Time Analysis
time_analysis_hour = df.groupby("HOUR").count().sort_values("HOUR", ascending=False)
time_analysis_year = df.groupby("YEAR").count().sort_values("YEAR", ascending=False)
time_analysis_month = df.groupby("MONTH").count().sort_values("MONTH", ascending=False)
hotspots = df.groupby("BOROUGH").count().sort_values("BOROUGH", ascending=False)
causes = df.groupby("CONTRIBUTING FACTOR VEHICLE 1").count().sort_values("CONTRIBUTING FACTOR VEHICLE 1", ascending=False)
# vehicle_types = df.groupby('VEHICLE TYPE CODE 1').count().sort_values('VEHICLE TYPE CODE 1', ascending=False)
# cause_vehicle_relation = df.groupby(['CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1']).count().sort_values('CONTRIBUTING FACTOR VEHICLE 1', ascending=False)

col1, col2 = st.columns(2)
with col1:
    st.header("Time Analysis")
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    with tab1:
        st.write("Hourly Analysis:")
        # sns.barplot(x='HOUR', y='total_bill', data=time_analysis_hour);
 
    with tab2:
        st.write("Monthly Analysis:")
        st.write(time_analysis_month)
        
    with tab3:
        st.write("Yearly Analysis:")
        st.write(time_analysis_year)
        
with col2:
    st.header("Location Analysis")
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    with tab1:
        st.write("Hotspots")
        st.write(hotspots)
 
    with tab2:
        st.write("Causes")
        st.write(causes)
        
    with tab3:
        st.write("Vehicle Types")
        # st.write(vehicle_types)


# Cause-Vehicle Relation
# st.header("Cause-Vehicle Relation")
# st.write(cause_vehicle_relation)
st.header("Clustering")
output = pd.DataFrame({"Total Killed": df["TOTAL KILLED"], "Total Injured": df["TOTAL INJURED"], "prediction": df["prediction"]})
plt.title('Clustering')
sns.scatterplot(x='Total Killed', y='Total Injured', hue='prediction', s=100, data=output)
st.pyplot(plt)