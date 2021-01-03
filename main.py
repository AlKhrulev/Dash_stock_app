import pandas as pd
import numpy as np
import dash
import pandas_datareader as pdr
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import os

def read_stocks_from_file(filename="stock_list.txt"):
    stocks=[]
    with open(filename,'r') as file:
        for line in file.readlines():
            stocks.append(line[:-1]) # removing newlines
        print(stocks)

    return stocks

def get_stock_data(stocks,source="stooq",period=6):
    #a dict to hold stock data for the required period
    stocks_dict={}

    #for stooq, all US stocks have a .US extension, so we have to account for that
    if source=="stooq":
        stocks=list(map(lambda stock:stock+".US",stocks))

    for stock in stocks:
        f = web.DataReader(stock, 'stooq')
        stocks_dict[stock]=f[:period]
        
    return stocks_dict

def save_plots_for_debugging(data,dir_name="graphs"):
    os.makedirs(dir_name,mode=755,exist_ok=True)

    fig=plt.figure()
    ax1=fig.add_subplot(1,1,1)
    for stock_name,df in data.items():
        ax1.set_title(stock_name)
        stock_data=df['Close']
        df.plot(ax=ax1,style='k--')
        plt.savefig(fname=dir_name+"/"+stock_name+"_close.png") # save fig in the new dir
        plt.cla() #clear axes before new plot


if __name__=='__main__':
    stocks=read_stocks_from_file()
    data=get_stock_data(stocks)
    save_plots_for_debugging(data)
