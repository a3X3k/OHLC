<div align = "center">

# [OHLC Engine](#)

</br>
	
## Table of Contents

</br>

| | Table Of Contents |
|--|----------------|
| 1 | [About](#About)  |
| 2 | [Input](#Input)  |
| 3 | [Setup](#setup)  | 
| 4 | [Libraries](#Libraries) |
| 5 | [Members](#Members) | 

	
</div>



## About

- This Project is about creating a **Dashboard** based on which User would be able to analyze the sentiment of the specific 
stock. 
- Analytical Server `OHLC (Open/High/Low/Close)` time series based on the **Stock List** dataset is created which is imported from the **JSON** file.
- An **OHLC** chart is a type of bar chart that shows open, high, low, and closing prices for each period. 
- **OHLC** charts are useful since they show the four major data points over a period, with the closing price being considered the most important by many traders.
- The final output will be displayed in a report printed in **Charts**. 
	
	
## Input

- The ‘Stock List’ dataset which is provided in JSON format comprise of certain attributes, following is the associated meanings of some of the attributes.

```
struct OHLC
{
	symbol : Stock Ticker string
	open : opening price Double
	high : highest price Double
	low : lowest price Double
	close : closed price Double
	date : date of transaction Date
}
```

- Rest all attributes can be ignored for generating the OHLC Bar charts
	
	
## Setup

- To run this project, install and setup the following Libraries,

```py
pip install dash   
pip install dash-html-components                                         
pip install dash-core-components                                     
pip install plotly

pip install dash-bootstrap-components
pip install stockstats
pip install mpl_finance
```


## Libraries

- Project is created with,
		
	* [JSON](#Libraries)
	* [Dash](#Libraries)
	* [Dash Core Components](#Libraries)
	* [Dash Html Components](#Libraries)
	* [Dash Dependencies](#Libraries)
	* [Dash Bootstrap Components](#Libraries)
	* [Dash Table](#Libraries)
	* [Plotly](#Libraries)
	* [Datetime](#Libraries)
	* [Stockstats](#Libraries)
	* [Matplotlib](#Libraries)


<div align = "center">
	
## Members
	
</br>

| Adheena B | Karthik Shriram G S| Lavanya Ratna Sirisha Munduri | Peddu Sai Harika | S Abhishek |
|----------------|----------------|----------------|----------------|----------------|
	
</div>
