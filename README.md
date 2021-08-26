# DIY_Bloomberg_Terminal
Use this DIY Bloomberg Terminal to have a text message be sent directly to your phone number if a stock you have your eyes on, makes a drastic change, without having to manually check the stock market.

# What is needed to run the code?
- Firstly, you must use the Alpha Vantage API to access data on stock market changes. You will choose a stock and then using the API documentation, fill in the appropriate values for variables STOCK and COMPANY_NAME. You will also need to access your own personal API key, and replace it's value with YOUR_STOCK_API_KEY in the variable stock_api_key.  
- Secondly, you must use the NEWS API(https://newsapi.org, find it through here) to access the first 3 news articles surrounding your stock of choice. As with the Alpha Vantage API, you must access your personal API key for NEWS API. Replace it's value with YOUR_NEWS_API_KEY in the variable of news_api_key. 
- Thirdly, create a Twilio account, so that you can send yourself text messages. They will give you a phone number. Replace YOUR_TWILIO_FROM_PHONE_NUMBER with the phone number they give you as the Twilio phone number. Replace YOUR_TO_PHONE_NUMBER with the phone number you wish the message to be sent to. You will also create your own account_sid and auth_token through Twilio.
- If you wish to automate this code, such that it is run everyday at a certain time(probably in the morning right after you wake up), you would need to use PythonAnywhere, or some other form of online IDE. 

# Learning Concepts
- HTTP Requests, such as requests.get(url=api_endpoint), in order to retrieve from an external database
- parameters that are often required to be inside the requests.get(params=parameters) in order to retrieve certain data
- How to convert retrieved information into a JSON format
- list comprehension
- How to use different API's to retrieve different types of information

# Conclusion
So far, this has been my favorite project, and probably most useful. I am excited to see what I can do with API's!





