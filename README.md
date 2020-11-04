# Fake News Detector

**An actual real life application to check the news you come across and want to check out its authenticity.** 

## What makes it one of a kind!

  - ##### A actual real life news checker anytime,anywhere.
  - ##### Complete privacy , messages checked by machine learning no actual human would read your message.
  - ##### As of now, Available on two platforms Whatsapp and Telegram. Soon more to come.
  - ##### Check out our website to know everthing in detail.(https://shagun0915.github.io/FakeNewsDetector/index.html)
## Wanna try it for yourself ?
The user needs to save the official twilio number i.e(+1 415 523 8886),  After saving this number they need to send a code to this number. For this project it is "join wet-forgot" .To redirect their messages to our servers hosted on heroku .(https://thawing-springs-11284.herokuapp.com/) .
After this is done now the user just needs to forward /share any news they receive on whatsapp and
they will get a message , telling them whether the news is real or fake .


### Tech Stack:-

Our Detector  uses a number of frameworks to work properly:

* ##### Flask 
* ##### Jsonify
* ##### NLTK
* ##### Tensorflow
* ##### Pandas
* ##### Pickle
* ##### Numpy
* ##### Regex

### Wanna See for yourself how it runs? 

**Fake news Detector requires Tensorflow v2+ to run.**

Install the dependencies  using ``` $ pip install -r requirements.txt ```

```sh
$ cd Fakenews
$ python3 flask_server.py 
```

* Also if you wanna retrain the model it is super simple take few news item and use the train_model function in model.py
* You can save the incoming messages as well

### How it looks 
we know it looks simple but that was intentional :)
![screenshot of whatsapp ](https://github.com/KartikKapil/Fakenews/blob/master/whatsapp%20.png)
![screeenshot of telegram](https://github.com/KartikKapil/Fakenews/blob/master/telegram.png)
![screenshot of our servers](https://github.com/KartikKapil/Fakenews/blob/master/server.png)
