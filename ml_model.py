import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from sklearn.model_selection import train_test_split

def train_model():
	Train = pd.read_csv("train.csv")
	Train.head()
	X=Train.drop('label',axis=1)
	Train.isnull().sum()
	Train=Train.dropna()
	Train.isnull().sum()
	Train=Train.copy()
	Train.reset_index(inplace=True)
	x=Train['title']
	y=Train['label']
	ps = PorterStemmer()
	corpus = []
	for i in range(0, len(Train)):
	    review = re.sub('[^a-zA-Z]', ' ', Train['title'][i])
	    review = review.lower()
	    review = review.split()
	    
	    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
	    review = ' '.join(review)
	    corpus.append(review)

	voc_size=5000
	one_hot_rep=[one_hot(words,voc_size)for words in corpus]
	sentence_length=25
	embedded_docs=pad_sequences(one_hot_rep,padding='pre',maxlen=sentence_length)
	embedding_vector_features=40
	model=Sequential()
	model.add(Embedding(voc_size,embedding_vector_features,input_length=sentence_length))
	model.add(Dropout(0.3))
	model.add(LSTM(200))
	model.add(Dropout(0.3))
	model.add(Dense(1,activation='sigmoid'))
	model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
	z =np.array(embedded_docs)
	y =np.array(y)
	x_train, x_test, y_train, y_test = train_test_split(z, y, test_size=0.10, random_state=42)
	model.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=20,batch_size=64)
	model.save("main_model.h5")
def income_message(message):
	voc_size=5000
	nltk.download('stopwords')
	model = tf.keras.models.load_model('main_model.h5')
	Test=[]
	Test.append(message)
	ps = PorterStemmer()
	corpus_test = []
	for i in range(0, len(Test)):
	#     review = re.sub('[^a-zA-Z]', ' ',Test['title'][i])
	    review = re.sub('[^a-zA-Z]', ' ',Test[i])
	    review = review.lower()
	    review = review.split()
	    
	    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
	    review = ' '.join(review)
	    corpus_test.append(review)

	one_hot_rep_Test=[one_hot(words,voc_size)for words in corpus_test] 
	sentence_length=25
	embedded_docs_test=pad_sequences(one_hot_rep_Test,padding='pre',maxlen=sentence_length)
	x_test=np.array(embedded_docs_test)
	check=model.predict_classes(x_test)
	final_ans = int(check[0][0])
	return final_ans

	
