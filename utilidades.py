import spacy
nlp = spacy.load('en_core_web_lg')
import re 
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
nltk.download('stopwords')
stopwords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

def preprocesamiento(texto):
    texto = texto.lower()
    texto = re.sub(r'\d+', '', texto)
    texto = re.sub(r'[^\w\s]', '', texto)
    patron = re.compile(r'''\b(?:creative|common|et|al |aal|fig|author|original|license|journal|bmc|plo|
                        reference|data|journalpone|august|licensed|common|sharing|author|copyright
                        |sharing|distribution|international|permit|author|link|format|licence|material|regulation
                        |image|plo|source|adaptation|otherwise|permitted|credit|statutory|pone|acces|open|holder
                        |third|indicate|exceeds|party|visit|need|permit|common|copyright|directly|intended)\b''', flags=re.IGNORECASE)
    texto = patron.sub('', texto)
    texto = texto.split()[:2500]
    texto = [palabra for palabra in texto if palabra not in stopwords]
    texto = [lemmatizer.lemmatize(palabra) for palabra in texto]
    texto = ' '.join(texto)
    return texto

def vectorize(text):
  texto = text.lower()
  texto = re.sub(r'@[A-Za-z0-9]+','',texto)
  texto = re.sub(r'[^0-9A-Za-z \t]','',texto)
  texto = re.sub(r'\w+:\/\/\S+','',texto)
  patron = re.compile(r'''\b(?:creative|common|et|al |aal|fig|author|original|license|journal|bmc|plo|
                        reference|data|journalpone|august|licensed|common|sharing|author|copyright
                        |sharing|distribution|international|permit|author|link|format|licence|material|regulation
                        |image|plo|source|adaptation|otherwise|permitted|credit|statutory|pone|acces|open|holder
                        |third|indicate|exceeds|party|visit|need|permit|common|copyright|directly|intended|colon|thyroid|lung)\b''', flags=re.IGNORECASE)
  texto = patron.sub('', texto)
  texto = re.sub(r'rt','',texto)
  texto = word_tokenize(texto)
  texto = texto[:2500]
  texto = [palabra for palabra in texto if palabra not in stopwords]
  texto = [lemmatizer.lemmatize(palabra) for palabra in texto]
  texto = ' '.join(texto)
  texto = nlp(texto).vector
  return texto