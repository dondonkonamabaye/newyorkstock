import time
from tracemalloc import start

import pandas as pd
import numpy as np

import datetime as dt

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.backends.backend_agg import FigureCanvas  # not needed for mpl >= 3.1

import mplleaflet
from IPython.display import IFrame

import base64
from PIL import Image
import io

import hvplot.pandas

import requests # Pour effectuer la requête
import pandas as pd # Pour manipuler les données
import datetime as dt

import param
import panel as pn

import holoviews as hv
import holoviews.plotting.bokeh

import seaborn as sns

import text_exchange as exchange_stock

pn.extension()
pn.extension('tabulator')

new_york_exchange = exchange_stock.NewYorkStockExchange
text = new_york_exchange.textName()

df_stockexchange  = pd.read_csv('stockexchange.csv')

unique_month_name_list = list(df_stockexchange['Month Name'].unique())

month_name_list = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',  'November', 'December']
select_month_name_line = pn.widgets.Select(name = 'Month Name', options = month_name_list)

unique_segment = list(df_stockexchange['Segment'].unique())
select_segment = pn.widgets.Select(name = 'Segment', options = unique_segment)

unique_segment_with_int = list(df_stockexchange['Segment'].unique())
select_segment_with_int = pn.widgets.Select(name = 'Segment', options = unique_segment_with_int)

unique_month_name = list(df_stockexchange['Month Name'].unique())
select_month_name = pn.widgets.Select(name = 'Month Name', options = unique_month_name)

max_units_sold = df_stockexchange['Units Sold'].max()
min_units_sold = df_stockexchange['Units Sold'].min()
avg_units_sold = df_stockexchange['Units Sold'].mean()

int_slider_units_sold = pn.widgets.IntSlider(name='Units Sold', start=int(min_units_sold), end=int(max_units_sold), step=10, value=int(avg_units_sold))
int_slider_units_sold_month_name = pn.widgets.IntSlider(name='Units Sold', start=int(min_units_sold), end=int(max_units_sold), step=10, value=int(avg_units_sold))

idf_stockexchange  = df_stockexchange.interactive()

idf_stockexchange = (
    idf_stockexchange[
            (idf_stockexchange['Segment'] == select_segment)
        ]
        .groupby(['Segment', 'Country', 'Product', 'Discount Band', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 'COGS', 'Profit', 'Month Name'])['Units Sold'].mean()
        .to_frame()
        .reset_index()
        .sort_values(by='Segment')
        .reset_index(drop=True)
        )


idf_stockexchange_month_name  = df_stockexchange.interactive()

idf_stockexchange_month_name = (
    idf_stockexchange_month_name[
            (idf_stockexchange_month_name['Month Name'] == select_month_name)
            &
            (idf_stockexchange_month_name['Units Sold'] <= int_slider_units_sold_month_name)
        ]
        .groupby(['Month Name','Segment', 'Country', 'Product', 'Discount Band', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 'COGS'])['Units Sold'].mean()
        .to_frame()
        .reset_index()
        .sort_values(by= 'Month Name')
        .reset_index(drop=True)
        )


idf_stockexchange_bar  = df_stockexchange.interactive()

idf_stockexchange_bar = (
    idf_stockexchange_bar[
            (idf_stockexchange_bar['Segment'] == select_segment_with_int)
            &
            (idf_stockexchange_bar['Units Sold'] <= int_slider_units_sold)
        ]
        .groupby(['Segment', 'Country', 'Product', 'Discount Band', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 'COGS', 'Profit', 'Month Name'])['Units Sold'].mean()
        .to_frame()
        .reset_index()
        .sort_values(by='Segment')
        .reset_index(drop=True)
        )


idf_stockexchange_line  = df_stockexchange.interactive()

idf_stockexchange_line = (
    idf_stockexchange_line[
            (idf_stockexchange_line['Segment'] == select_segment_with_int)
            &
            (idf_stockexchange_line['Units Sold'] <= int_slider_units_sold)
        ]
        .groupby(['Segment', 'Country', 'Product', 'Discount Band', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 'COGS', 'Profit', 'Month Name'])['Units Sold'].mean()
        .to_frame()
        .reset_index()
        .sort_values(by='Segment')
        .reset_index(drop=True)
        )


nyse_stockexchange_table = idf_stockexchange.pipe(pn.widgets.Tabulator, pagination='remote', page_size = 6, width=1300)
nyse_stockexchange_product_bar = idf_stockexchange.hvplot(x = 'Country', y = "Units Sold", by = 'Product', kind = "barh", rot = 45, height = 350,  width = 620, stacked = True)
nyse_stockexchange_country_bar = idf_stockexchange.hvplot(x = 'Product', y = "Units Sold", by = 'Country', kind = "barh", rot = 45, height = 350,  width = 620, stacked = True)

nyse_stockexchange_table_bar = idf_stockexchange_bar.pipe(pn.widgets.Tabulator, pagination='remote', page_size = 6, width=1300)
nyse_stockexchange_product_barh = idf_stockexchange_bar.hvplot(x = 'Country', y = "Units Sold", by = 'Discount Band', kind = "barh", rot = 45, height = 350,  width = 620, stacked = True)
nyse_stockexchange_country_barh = idf_stockexchange_bar.hvplot(x = 'Product', y = "Units Sold", by = 'Discount Band', kind = "barh", rot = 45, height = 350,  width = 620, stacked = True)

nyse_stockexchange_table_month_name = idf_stockexchange_month_name.pipe(pn.widgets.Tabulator, pagination='remote', page_size = 6, width=1300)
nyse_stockexchange_product_month_name_bar = idf_stockexchange_month_name.hvplot(x = 'Country', y = "Units Sold", by = 'Discount Band', kind = "barh", rot = 45, height = 350,  width = 620, stacked = True)
nyse_stockexchange_country_month_name_bar = idf_stockexchange_month_name.hvplot(x = 'Product', y = "Units Sold", by = 'Discount Band', kind = "barh", rot = 45, height = 350,  width = 620, stacked = True)

nyse_stockexchange_table_line = idf_stockexchange_line.pipe(pn.widgets.Tabulator, pagination='remote', page_size = 6, width=1300)
nyse_stockexchange_country_line = idf_stockexchange_line.hvplot(x = 'Month Name', y = "Units Sold", by = 'Discount Band', kind = "bar", rot = 45, height = 350,  width = 1300, stacked = True)


Login_Template = pn.template.VanillaTemplate(
title = 'New York Stock Exchange Financial Data Visualization',
sidebar =  [ 
             pn.pane.PNG("dondonedmond.png"),
             pn.Row(pn.Column(pn.pane.Alert(text)))
           ],
main    =  [
            pn.Tabs
            (  
                pn.Column
                (
                    pn.Row(pn.Column(nyse_stockexchange_table_line), pn.Column()),
                    pn.Row(pn.Column(nyse_stockexchange_country_line), pn.Column()),
                ),

                pn.Column
                (
                    pn.Row(pn.Column(nyse_stockexchange_table), pn.Column()),
                    pn.Row(pn.Column(nyse_stockexchange_product_bar), pn.Column(nyse_stockexchange_country_bar)),
                ),

                pn.Column
                (
                    pn.Row(pn.Column(nyse_stockexchange_table_bar), pn.Column()),
                    pn.Row(pn.Column(nyse_stockexchange_product_barh), pn.Column(nyse_stockexchange_country_barh)),
                ),

                pn.Column
                (
                    pn.Row(pn.Column(nyse_stockexchange_table_month_name), pn.Column()),
                    pn.Row(pn.Column(nyse_stockexchange_product_month_name_bar), pn.Column(nyse_stockexchange_country_month_name_bar)),
                ),
            ),
    ],
)

Login_Template.servable();