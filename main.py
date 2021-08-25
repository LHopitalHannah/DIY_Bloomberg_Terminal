""" Create a DIY Bloomberg Terminal for Google"""

import requests
import json
import os
from twilio.rest import Client

# STEP 1: Use https://www.alphavantage.co, Alpha Vantage API to collect stock data
STOCK = "GOOGL"
COMPANY_NAME = "Google"
message = ""

stock_api_key = YOUR_STOCK_API_KEY
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
response.raise_for_status()
data = response.json()
times_dict = data["Time Series (Daily)"]
times_list = [value for (key, value) in times_dict.items()]
yesterday = float(times_list[0]["4. close"])
day_before_yesterday = float(times_list[1]["4. close"])
stock_change = ((yesterday - day_before_yesterday) / yesterday) * 100
if stock_change > 2 or stock_change < -2:
    message = [f"{STOCK}: {round(stock_change, 2)}%\n"]
    # STEP 2: # When STOCK price increase/decreases by 2% between yesterday and the day before yesterday, then
    # use https://newsapi.org to get the first 3 news pieces for Google.
    news_api_key = YOUR_NEWS_API_KEY
    news_parameters = {"apiKey": news_api_key,
                       "qInTitle": COMPANY_NAME,
                       }
    response = requests.get(url="https://newsapi.org/v2/everything?", params=news_parameters)
    news_data = response.json()
    articles_list = news_data["articles"][:3]
    for _ in range(len(articles_list)):
        article_headline = f"{articles_list[_]['title']}\n"
        message.append(article_headline)
        article_brief = f"{articles_list[_]['description']}\n"
        message.append(article_brief)
        with open("message.txt", "w") as file_write:
            file_write.writelines(message)
    with open("message.txt", "r") as file:
        contents = file.read()

        ## STEP 3: Use https://www.twilio.com, the Twilio API, to send a message including the variation in stock for Google,
        # and the 3 first  news articles from NEWS API to your phone number.
        account_sid = YOUR_ACCOUNT_SID
        auth_token = YOUR_AUTH_TOKEN

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to= YOUR_TO_PHONE_NUMBER,
            from_=YOUR_TWILIO_FROM_PHONE_NUMBER,
            body=contents)
