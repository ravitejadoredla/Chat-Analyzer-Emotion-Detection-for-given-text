# Chat-Analyzer-Emotion-Detection-for-given-text
NLP techniques are used
Emotion classification attempts to detect the emotional content in the input text and based on different approaches establish what kind of emotional content is present, if any. Textual emotion classification relies mainly on linguistic resources and it introduces many challenges to assignment of text to emotion represented by a proper model. A crucial part of each emotion detector is emotion model.

* [App features](#features)
* [Project development](#project-development)
  * [Data preparation](#data-preparation)
  * [Text cleaning](#text-cleaning)
  * [Model building](#model-building)

# Features
The text emotion classification Logistic Regression project facets:

* Text to Speech (Using GTTS API) 
* Speech to text (Uploaded speech and recorded speech with speech_recognition)
* Translation 
* Text Tokenization
* Named Entity Recognition (with Spacy) 
* Text Emotion Classification

# Project development
## Data preparation
The dataset is 34793 row csv file that has two columns: Emotion and Text. According to the discrete basic emotion description approach, emotions can be classified into six basic emotions _(van den Broek, 2013)_: 
* :frowning_face: Sadness, 
* :smile: Joy 
* :flushed: Surprise
* :angry: Anger
* :vomiting_face: Disgust
* :fearful: Fear 

## Text cleaning
Text cleaning is the process of preparing raw text for NLP (Natural Language Processing) so that machines can understand human language. 
The three text cleaning techniques that were performed on the text emotion dataset are: 
* Normalizing text 
* Removing stop words 
* Removing user handles

## Model building
The linear sequence of steps required to prepare the data, tune the model, and transform the predictions is called the modeling pipeline. Modern machine learning libraries like the scikit-learn Python library allow this sequence of steps to be defined and used correctly (without data leakage) and consistently (during evaluation and prediction). 

The linear regression pipeline that was created takes as an argument a vectorizer (the CountVectorizer transformer) and an estimator as steps 
