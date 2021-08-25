# DIY_Bloomberg_Terminal
Use this DIY Bloomberg Terminal to have a text message be sent directly to your phone number if a stock you have your eyes on, makes a drastic change, without having to manually check the stock market.

# What is needed to run the code?
- Firstly, you must use the Alpha Vantage API to access data on stock market changes. You will choose a stock and then using the API documentation, fill in the appropriate values for variables STOCK and COMPANY_NAME. You will also need to access your own personal API key, and replace it's value with YOUR_STOCK_API_KEY in the variable stock_api_key.  
- Secondly, you must use the NEWS API(https://newsapi.org, find it through here) to access the first 3 news articles surrounding your stock of choice. As with the Alpha Vantage API, you must access your personal API key for NEWS API. Replace it's value with YOUR_NEWS_API_KEY in the variable of news_api_key. 
- Thirdly, create a Twilio account, so that you can send yourself text messages. They will give you a phone number. Replace YOUR_TWILIO_FROM_PHONE_NUMBER with the phone number they give you as the Twilio phone number. Replace YOUR_TO_PHONE_NUMBER with the phone number you wish the message to be sent to. You will also create your own account_sid and auth_token through Twilio.





