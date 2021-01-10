This project was done by Gomes Teixeira Filipe from DIA 2.

The goal of this project was to work with the data Online Video Characteristics and Transcoding Time Dataset Data Set
dataset link : https://archive.ics.uci.edu/ml/datasets/Online+Video+Characteristics+and+Transcoding+Time+Dataset

in order to work this dataset, i had to explore the data, create graph to analyze the features and understand
how to generally use the machine learning.

I use the first dataset for the insight of the youtube videos, then I made my models work on the second dataset
which possess the data on the transcoding of the youtube videos.

The final goal that i had to achieve is get a model with a very good accuracy.


# Content

in the github you can find :

  1. the pdf of the powerpoint
  2. the datasets
  3. the django api
  4. the jupyter notebook used in order to create the models
  
# API

In order to start the django api, you will need to possess python and django installed
in order to install django : https://www.djangoproject.com/download/

to start the api, you have to go to the folder PDA then run the following command:
python ./manage.py runserver 0.0.0.0:8000

once you have used the command, you will be able to communicate with the API.
The url path to ask a prediction from the api is 0.0.0.0:8000/api/prediction or localhost:8000/api/prediction

there is an exemple of the json that the api accept:
{
    "duration" : [130.35667],
    "codec" : ["mpeg4"],
    "width" : [176],
    "height" : [144],
    "bitrate" : [54590],
    "framerate" : [12.00000],
    "i" : [27],
    "p" : [1537],
    "b" : [0],
    "frames" : [1564],
    "i_size" : [64483],
    "p_size" : [825054],
    "b_size" : [0],
    "size" : [889537],
    "o_codec" : ["mpeg4"],
    "o_bitrate" : [56000],
    "o_framerate" : [12.0],
    "o_width" : [176],
    "o_height" : [144],
    "umem" : [22508]
}

# Conclusion

After all my attemps and research, I choose to use the Decision Tree Regression model.
It was the model with the best accuracy without touching the hyperparameters.

Once I had find the Decision Tree Regression model, I started to tune the Hyperparameters.
With the research of the best gap of values for the hyperparemeters and the cross validation in order to get the
best combination of hyperparameters, i found a model who was a lot more effiency then the original.

the hyperparameters :
criterion : mse
max_depth : 26
min_samples_leaf : 1
min_samples_split : 2

Of course, once i created my API i tried to predict a lot of values. The accuracy of the model is very good and the model isn't overfitted.

It was a good project who allowed me to understand a lot of parts of the machine learning that i didn't understood previously and of course it was fun.
