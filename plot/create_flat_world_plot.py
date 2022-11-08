import warnings
import seaborn as sns
import plotly.tools as tls
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import plotly.offline as py
py.init_notebook_mode(connected=True)
warnings.filterwarnings('ignore')


non_country_list = ['Arab World', 'Central Europe and the Baltics', 'Caribbean small states', 'East Asia & Pacific (excluding high income)',
                    'Early-demographic dividend', 'East Asia & Pacific', 'Europe & Central Asia (excluding high income)',
                    'Europe & Central Asia', 'Euro area', 'European Union', 'Fragile and conflict affected situations', 'High income',
                    'Heavily indebted poor countries (HIPC)', 'IBRD only', 'IDA & IBRD total', 'IDA total', 'IDA blend', 'IDA only',
                    'Latin America & Caribbean (excluding high income)', 'Latin America & Caribbean', 'Least developed countries: UN classification',
                    'Low income', 'Lower middle income', 'Low & middle income', 'Late-demographic dividend', 'Middle East & North Africa',
                    'Middle income', 'Middle East & North Africa (excluding high income)', 'North America', 'OECD members', 'Other small states',
                    'Pre-demographic dividend', 'Post-demographic dividend', 'South Asia', 'Sub-Saharan Africa (excluding high income)',
                    'Sub-Saharan Africa', 'Small states', 'East Asia & Pacific (IDA & IBRD countries)',
                    'Europe & Central Asia (IDA & IBRD countries)', 'Latin America & the Caribbean (IDA & IBRD countries)',
                    'Middle East & North Africa (IDA & IBRD countries)', 'South Asia (IDA & IBRD)',
                    'Sub-Saharan Africa (IDA & IBRD countries)', 'Upper middle income', 'World']


def create_flat_world_plot(year='2010'):
    data = [ dict(
        type = 'choropleth',
        locations = df_country['Country Code'],
        z = df_country[year],
        text = df_country['Country Name'],
        colorscale = 'Reds',
        autocolorscale = False,
        reversescale = False,
        marker = dict(
            line = dict (
                color = 'rgb(180,180,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            title = 'Unemployment (%)'),
    ) ]

    layout = dict(
        title = f'Unemployment around the globe in {year}',
        geo = dict(
            showframe = True,
            showcoastlines = True,
            showocean = True,
            #oceancolor = 'rgb(0,255,255)',
            oceancolor = 'rgb(222,243,246)',
            projection = dict(
                type = 'Mercator'
            )
        )
    )

    fig = dict( data=data, layout=layout )
    py.plot( fig, validate=False,filename=f'./flat_world_plots/flat_world_plot_{year}')


if __name__ == "__main__":
    # read data
    df = pd.read_csv('../data/API_ILO_country_YU.csv')

    # filter the data by noncountry list
    df_non_country = df[df['Country Name'].isin(non_country_list)]
    index = df_non_country.index
    df_country = df.drop(index)

    # create directory to place the scatter plots
    os.mkdir("flat_world_plots")

    year_list = ['2010', '2011', '2012', '2013', '2014']

    for year in year_list:
        create_flat_world_plot(year)