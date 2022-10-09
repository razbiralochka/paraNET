import tensorflow as tf
import numpy as np
import re
import pickle
tf.config.set_visible_devices([], 'GPU')
class ParaNETmodel():
    def __init__(self):
        with open('dictf.pkl', 'rb') as f:
            self.dict_of_words = pickle.load(f)
        self.dictThemes = {0: 'Спам', 1: 'Запись', 2: 'Общая информация', 3: 'Информация курсантам', 4: 'Тандемы'}
        self.a = np.zeros([1, 200])
        self.nn_words = list()
        self.paraNET = tf.keras.models.load_model('ParaNet')

        print('NN is ready!')
    def msg_Analise(self,msg):
        newword = re.split("[^а-яё]", msg.lower())
        print('new message!')
        for word in newword:

            if (word in self.dict_of_words):
                self.nn_words.append(self.dict_of_words[word])
        for j, var in enumerate(self.nn_words):
            self.a[0, j] = self.nn_words[j]

        self.b=self.a.reshape(1,1,200)
        themes = self.paraNET.predict(self.b)

        arg = np.argmax(themes)

        theme = self.dictThemes[arg]
        print(themes)
        self.nn_words.clear()

        return theme