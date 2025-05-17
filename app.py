import pandas as pd
import streamlit as st
import pickle
#import numpy as np



def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0].item()
    distances = similarity[movie_index]
    movies_list = sorted([(k, float(val)) for k, val in enumerate(distances)], reverse=True, key=lambda x: x[1])[1:6]
    movie_recommend = []
    for j in movies_list:
        movie_id=j[0]
        #fetch poster from API
        movie_recommend.append(movies.iloc[j[0]].title)
    return movie_recommend



#movies1= pickle.load(open('movies.pkl', 'rb'))
#movies1 = movies1['title'].values
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'How would you like to be contacted ?',
    movies['title'].values
)
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
