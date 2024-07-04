import dashboard as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("output.csv")

# Create a Streamlit app
st.title("Traffic Accident Analysis")

# # Hotspots
# st.header("Hotspots")
# hotspots = df.groupBy("BOROUGH").count().orderBy(count("BOROUGH").desc())
# st.write(hotspots)

# # Time Analysis
# st.header("Time Analysis")
# time_analysis_hour = df.groupBy("HOUR").count().orderBy(count("HOUR").desc())
# time_analysis_year = df.groupBy("YEAR").count().orderBy(count("YEAR").desc())
# time_analysis_month = df.groupBy("MONTH").count().orderBy(count("MONTH").desc())

# st.write("Hourly Analysis:")
# st.write(time_analysis_hour)

# st.write("Yearly Analysis:")
# st.write(time_analysis_year)

# st.write("Monthly Analysis:")
# st.write(time_analysis_month)

# # Causes
# st.header("Causes")
# causes = df.groupBy("CONTRIBUTING FACTOR VEHICLE 1").count().orderBy(count('CONTRIBUTING FACTOR VEHICLE 1').desc())
# st.write(causes)

# # Vehicle Types
# st.header("Vehicle Types")
# vehicle_types = df.groupBy('VEHICLE TYPE CODE 1').count().orderBy(count('VEHICLE TYPE CODE 1').desc())
# st.write(vehicle_types)

# # Cause-Vehicle Relation
# st.header("Cause-Vehicle Relation")
# cause_vehicle_relation = df.groupBy('CONTRIBUTING FACTOR VEHICLE 1', 'VEHICLE TYPE CODE 1').count().orderBy(count('CONTRIBUTING FACTOR VEHICLE 1').desc())
# st.write(cause_vehicle_relation)

# # Clustering
# st.header("Clustering")
# output = pd.DataFrame({"Total Killed": df["TOTAL KILLED"], "Total Injured": df["TOTAL INJURED"], "prediction": df["prediction"]})
# plt.title('Clustering')
# sns.scatterplot(x='Total Killed', y='Total Injured', hue='prediction', s=100, data=output)
# st.pyplot(plt)