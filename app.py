from flask import Flask,render_template


app = Flask(__name__)

biblioteca = {"Python":{'Machine Learning':['scikit-learn','Keras','XgBoot'],
              'Data Visualization':['Matplotib','Seaborn','Bokeh'],
              'Processamento de Linguagem Natural':['NLTK','Spacy','Gensim'],
              'Distributed Deep Learning':['Dist-keras','elephas','spark-deep-learning'] }}


@app.route('/')
def index(biblioteca=biblioteca):
    return render_template("index.html",classes=biblioteca)
