
import pandas as pd
from ast import literal_eval
import time

from cdqa.utils.filters import filter_paragraphs
from cdqa.utils.download import download_model, download_bnpp_data
from cdqa.pipeline.cdqa_sklearn import QAPipeline

df = pd.read_csv('data/GlobalTravelPolicy_DL.csv', 
                 converters={'paragraphs': literal_eval})


cdqa_pipeline = QAPipeline(reader='models/bert_qa.joblib', 
                           retriever='bm25okapi',
                           retrieve_by_doc = False, # Read by paragraphs 
                           #ngram_range = (1,1), min_df=1, k1=5.0, preprocessor=preprocess,
                           #stop_words=None,
                           #b=0.75,
                           #floor=0.25
                          )

cdqa_pipeline.fit_retriever(df)
query = 'what are Business trips?'
prediction = cdqa_pipeline.predict(query=query, retriever_score_weight=1.0)

print('query: {}\n'.format(query))
print('answer: {}\n'.format(prediction[0]))
print('title: {}\n'.format(prediction[1]))
print('paragraph: {}\n'.format(prediction[2]))

