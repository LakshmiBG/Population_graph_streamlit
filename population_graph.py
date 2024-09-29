import pandas as pd
url = "https://raw.githubusercontent.com/LakshmiBG/Population_graph_streamlit/refs/heads/main/population.csv"
df = pd.read_csv(url)
df = df.drop(columns =['Unnamed: 0'])
df.head()

#Let's define the list of column headersc(country names) (expect the firsst column which)

unique_names = df['country'].unique().tolist()

#Let's define the years (the first column)
years = df['year'].unique()

#Then create teh first column of dataframe
df_visu = pd.DataFrame(years,columns= ['year'])
#display(df_visu.head())

#What should we have in the other columns? Population by country
#For example Sweden
#df[df['country']=='Sweden']['pop'].values

#For all teh countries
for country_name in unique_names:
    df_visu[country_name] = df[df['country']==country_name]['pop'].values

#Make graphics

import streamlit as st
#define the figure title
st.title('Population Plot')

#define a selector(columns to draw)
columns = st.multiselect('Countries: ', unique_names)

#Plot the line chart
st.line_chart(df_visu, x = 'year', y = columns, y_label = 'Population', x_label = 'Year')
