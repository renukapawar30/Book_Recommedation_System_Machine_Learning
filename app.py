# Book Recommendation Feedback system

# import libaries
import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(layout ='wide')

st.header('Book Recommender System')

st.markdown('''
            #### This site using collabative filtering suggests book from our catlog
            #### We recommend top 50 books for every one as well
            ''')


# import our models

popular = pickle.load(open('popular.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_score = pickle.load(open('similarity_score.pkl','rb'))

# Top 50 Books

st.sidebar.title('Top 50 Books')

if st.sidebar.button('SHOW'):
    cols_per_row = 5
    num_row = 10
    for row in range(num_row):
        cols = st.columns(cols_per_row)
        for col in range(cols_per_row):
            book_ind = row + cols_per_row + col
            if book_ind < len(popular):
                with cols[col]:
                    st.image(popular.iloc[book_ind]['Image-URL-M'])
                    st.text(popular.iloc[book_ind]['Book-Title'])
                    st.text(popular.iloc[book_ind]['Book-Author'])




# Function to recommend books

def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_item = sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
    # Lets create an empty list and in that list i want to popluate with the book information
    # Book-Title,Book-Authors,Image-url
    # Empty List
    data =[]
    for i in similar_item:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)
    return data


#This is giving name of books 
book_list = pt.index

st.sidebar.title('Similar Book Suggestion')
selected_box = st.sidebar.selectbox('Select the Books in dropdown',book_list)

if st.sidebar.button('Recommend'):
    book_recommend = recommend(selected_box)
    cols = st.columns(5)
    for col_idx in range(5):
        with cols[col_idx]:
            if col_idx < len(book_recommend):
                st.image(book_recommend[col_idx][2])
                st.text(book_recommend[col_idx][1])
                st.text(book_recommend[col_idx][0])






# Import data

books = pd.read_csv('C:/Users/lenono/Desktop/Data Science/Python/Book Recommedation System/Data/Books.csv') # books data
users = pd.read_csv('C:/Users/lenono/Desktop/Data Science/Python/Book Recommedation System/Data/Users.csv')  #Users location and age data
ratings = pd.read_csv('C:/Users/lenono/Desktop/Data Science/Python/Book Recommedation System/Data/Ratings.csv') # users ratingg data

st.sidebar.title('Data Used')

if st.sidebar.button('Show'):
    st.subheader('This is Book Data we used in our model')
    st.dataframe(books)
    st.subheader('This is User Rating Data we used in our model')
    st.dataframe(ratings)
    st.subheader('This is Users Data we used in our model')
    st.dataframe(users)
    



































