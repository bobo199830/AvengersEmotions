import pandas as pd
import jieba
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.externals import joblib 
def chinese_word_cut(mytext):
    return " ".join(jieba.cut(mytext))
def get_custom_stopwords(stop_words_file):
    with open(stop_words_file) as f:
        stopwords=f.read()
    stopwords_list=stopwords.split('\n')
    custom_stopwords_list=[i for i in stopwords_list]
    return custom_stopwords_list
df=pd.read_csv('data.csv',encoding='gb18030')
x=df[['comment']].astype(str)
y=df[['sentiment']]
x['cut_comment']=x.comment.apply(chinese_word_cut)
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1)
stop_words_file="stopwordsHIT.txt"
stopwords=get_custom_stopwords(stop_words_file)
max_df = 0.8 # 在超过这一比例的文档中出现的关键词（过于平凡），去除掉。
min_df = 3 # 在低于这一数量的文档中出现的关键词（过于独特），去除掉。
vect = CountVectorizer(max_df = max_df,
                       min_df = min_df,
                       token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
                       stop_words=frozenset(stopwords))
term_matrix = pd.DataFrame(vect.fit_transform(x_train.cut_comment).toarray(), columns=vect.get_feature_names())
nb=MultinomialNB()
pipe=make_pipeline(vect,nb)
cross_val_score(pipe, x_train.cut_comment, y_train, cv=5, scoring='accuracy').mean()
print(cross_val_score(pipe, x_train.cut_comment, y_train, cv=5, scoring='accuracy').mean())
pipe.fit(x_train.cut_comment,y_train)
pipe.predict(x_test.cut_comment)
y_pred=pipe.predict(x_test.cut_comment)
print(metrics.accuracy_score(y_test,y_pred))
print(metrics.confusion_matrix(y_test,y_pred))
joblib.dump(pipe,"train_model.m")
