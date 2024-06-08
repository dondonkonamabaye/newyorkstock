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

# import mysql.connector
import seaborn as sns

pn.extension()
pn.extension('tabulator')

import panel as pn


class NewYorkStockExchange:

    def textName():
        df_stockexchange = pd.read_csv('stockexchange.csv')

        stockexchange_max = df_stockexchange.at[df_stockexchange['Units Sold'].idxmax(), 'Country']
        stockexchange_min = df_stockexchange.at[df_stockexchange['Units Sold'].idxmin(), 'Country']

        stockexchange_product_max = df_stockexchange.at[df_stockexchange['Units Sold'].idxmax(), 'Product']
        stockexchange_product_min = df_stockexchange.at[df_stockexchange['Units Sold'].idxmin(), 'Product']

        stockexchange_segment_max = df_stockexchange.at[df_stockexchange['Units Sold'].idxmax(), 'Segment']
        stockexchange_segment_min = df_stockexchange.at[df_stockexchange['Units Sold'].idxmin(), 'Segment']

        stockexchange_month_name_max = df_stockexchange.at[df_stockexchange['Units Sold'].idxmax(), 'Month Name']
        stockexchange_month_name_min = df_stockexchange.at[df_stockexchange['Units Sold'].idxmin(), 'Month Name']

        country_units_sold = df_stockexchange[['Country', 'Units Sold']]
        max_country_units_sold =  country_units_sold['Units Sold'].max()
        min_country_units_sold =  country_units_sold['Units Sold'].min()

        segment_units_sold = df_stockexchange[['Segment', 'Units Sold']]
        max_segment_units_sold =  segment_units_sold['Units Sold'].max()
        min_segment_units_sold =  segment_units_sold['Units Sold'].min()

        product_units_sold = df_stockexchange[['Product', 'Units Sold']]
        max_product_units_sold =  product_units_sold['Units Sold'].max()
        min_product_units_sold =  product_units_sold['Units Sold'].min()

        month_name_units_sold = df_stockexchange[['Month Name', 'Units Sold']]
        max_month_name_units_sold =  month_name_units_sold['Units Sold'].max()
        min_month_name_units_sold =  month_name_units_sold['Units Sold'].min()

        #print(f'The Maximum Volume is {google_volume_max} and Minimum Volume is {google_volume_min}')
        size = len(df_stockexchange)

        text_alert = """
                <h1><center>WEB APPLICATION</center></h1>

                <hr>
            """
        text_nyse_size =  f"The number of records is <b>{size}</b><hr>"
        text_stockexchange_max  =  f"The Maximum Units Sold Prices per Country is in <b>{stockexchange_max}</b> with a price of {max_country_units_sold}.<hr>"
        text_stockexchange_min  =  f"The Minimum Units Sold Prices per Country is in <b>{stockexchange_min}</b> with a price of {min_country_units_sold}.<hr>"

        text_stockexchange_segment_max     =  f"The Maximum Units Sold Prices per Segment is the <b>{stockexchange_segment_max}</b>.<hr>"
        text_stockexchange_segment_min     =  f"The Minimum Units Sold Prices per Segment is the <b>{stockexchange_segment_min}</b>.<hr>"

        text_stockexchange_product_max     =  f"The Maximum Units Sold Prices per Product is <b>{stockexchange_product_max}</b>.<hr>"
        text_stockexchange_product_min     =  f"The Minimum Units Sold Prices per Product is <b>{stockexchange_product_min}</b>.<hr>"

        text_stockexchange_month_name_max  =  f"The Maximum Units Sold Prices per Month is <b>{stockexchange_month_name_max}</b>.<hr>"
        text_stockexchange_month_name_min  =  f"The Minimum Units Sold Prices per Month is <b>{stockexchange_month_name_min}</b>.<hr>"

        text_stockexchange = text_stockexchange_max + text_stockexchange_min + text_stockexchange_segment_max + text_stockexchange_segment_min + text_stockexchange_product_max + text_stockexchange_product_min + text_stockexchange_month_name_max + text_stockexchange_month_name_min

        text_alert = text_nyse_size + text_stockexchange

        return text_alert