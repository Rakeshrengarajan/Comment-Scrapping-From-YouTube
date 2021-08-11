# Comment-Scrapping-From-YouTube

This is a program which retrieve the comments from a particular YouTube Video useing the YouTube Data Api V3.

Requirements:

Python 3.4+ (PyPy supported)
Make you have installed the following libraries:
    1.dotenv
    
Usage:

To start you will have to first register your application in Google Cloud Console. To register check https://console.cloud.google.com.

Here I have used YouTUbe Data API V3 to fetch the comments.

Generate the API key in the Google Cloud Console.

Create a .env file, which is a environment file. This file should contain the following variables:

    API_Key - Your API key which is generated in the console
    video_ID - The particular video whose comment you need to retrieve. 
    
If you have any doubt please read the API documentation https://developers.google.com/youtube/v3.

