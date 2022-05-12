
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    df = pd.read_csv('emissions.csv')
    df.drop(['continent', 'population', 'Code'], axis=1, inplace=True)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    #df['lag_emissions'] = pd.Series()

    # for country in df['country'].unique():
    #     for year in df.loc[df['country'] == country]['year']:
    #         df.loc[(df['country'] == country) & (df['year'] == str(int(year)+1))]['lag_emissions'] = df['emissions_per_capita']
    usa = df[df['country'] == 'World'].copy()

    usa['delta_emissions'] = usa['emissions_per_capita'].shift(-1)
    usa['delta_emissions'] = usa['delta_emissions'] - usa['emissions_per_capita']

    usa['delta_gdp'] = usa['gdp_per_capita'].shift(-1)
    usa['delta_gdp'] = usa['delta_gdp'] - usa['gdp_per_capita']
    print(usa)
    usa['slope'] = usa['delta_emissions']/usa['delta_gdp']
    usa.drop(usa.index[usa['slope'] < -0.02], inplace=True)

    print(usa)

    import seaborn as sns

    sns.lmplot(data=usa, x='year', y='slope')
    plt.show()

    sns.lmplot(data=usa, x='gdp_per_capita', y='slope')
    plt.show()


    import plotly.express as px

    fig = px.line(df, x="gdp_per_capita", y="emissions_per_capita", color='country', title='Emissions vs. GDP per capita over time')
    fig.show()






