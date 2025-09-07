import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

# cd /home/pants/Documents/streamlit_tutorial

### **Activate your virtual environment**
# In your project directory, run:

# `source .venv/bin/activate`

### You'll need to do this each time you open a new terminal.

### **Run the demo app**
#### Once your virtual environment is active, type:

# `streamlit run streamlit_app.py`


# read in file
df = pd.read_csv("state_data.csv")

# Create a graph of median household income
df.sort_values(['State', 'Year'], ascending=[True, True], inplace=True)
df['Pct Change in Median Income'] = df.groupby('State')['Median Household Income'].transform(lambda x: x.pct_change())

# page header
st.header("Changes in US State Demographics Over Time")

# Let user select which state to graph
state = st.selectbox("State:", df["State"].unique())

# let user select which demographic to display
demographic = st.selectbox("Select Demographic:"
, ("Pct Change in Median Income", "Total Population"))

# show charts
tab1, tab2 = st.tabs(["graphs", "table"])

with tab1:
    df_state = df[df["State"] == state]
    if demographic == "Total Population":
        fig = px.line(
            df_state
            , x="Year"
            , y="Total Population"
            , color="red"
            , title=f"Total Population of {state}"
            )
    elif demographic == "Pct Change in Median Income":
        fig = px.line(
            df_state
            , x="Year"
            , y="Pct Change in Median Income"
            , title=f"Change in Median Household Income of {state}"
            )
    else:
        raise ValueError("missing demographic")
    st.plotly_chart(fig)
with tab2:
    st.write("All Data")
    st.dataframe(df)
