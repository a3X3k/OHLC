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

</br>

## Directory Structure

</br>

```
├── RSI Code
│   ├── RSI.py
│
└── README.md
```

</br>

## About

- This Project is about creating a **Dashboard** based on which User would be able to analyze the sentiment of the specific 
stock. 
- Analytical Server **OHLC (Open/High/Low/Close)** time series based on the **Stock List** dataset is created which is imported from the **JSON** file.
- An **OHLC** chart is a type of bar chart that shows open, high, low, and closing prices for each period. 
- **OHLC** charts are useful since they show the four major data points over a period, with the closing price being considered the most important by many traders.
- The final output will be displayed in a report printed in **Charts**. 
	
	
## Input

- The **Stock List** dataset which is provided in **JSON** format comprise of certain attributes, following is the associated meanings of some of the attributes.

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

pip install yfinance
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
	* [Pandas](#Libraries)
	* [Pandas Datareader](#Libraries)
	* [Numpy](#Libraries)
	* [Seaborn](#Libraries)
	* [yfinance](#Libraries)
	* [Pickle](#Libraries)


## Project Outcome


![image](https://user-images.githubusercontent.com/52845731/132575365-5b5e8804-5bfb-4735-9cdc-407ee13af2cf.png)


<img src="https://user-images.githubusercontent.com/52845731/132575424-490b4ba1-1601-4670-bdf6-b17606b07d94.png" alt="drawing" width="600"/>

![image](https://user-images.githubusercontent.com/52845731/132575480-a44c00f3-012d-4abe-8527-d9f6aff35363.png)
![image](https://user-images.githubusercontent.com/52845731/132562513-69e72af2-7582-4507-8566-1e4ef5d8c68c.png)
![image](https://user-images.githubusercontent.com/52845731/132563454-d65e10dd-dc31-45f9-a6ef-3ced6da7b1ec.png)


<div align = "center">
	
## Members
	
</br>

| Adheena B | Karthik Shriram G S| Lavanya Ratna Sirisha Munduri | Peddu Sai Harika | S Abhishek |
|----------------|----------------|----------------|----------------|----------------|
	
</div>
