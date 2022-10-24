import pickle 
import streamlit as st
 
model = pickle.load(open('C:/Users/Josham Kadiebwe/Desktop/python/Datasets/Dataset2/Jonathan Equilibrage de donnee/Amazon_rfc.pkl', 'rb'))
 

def main ():
     st.title('Lingerie fabric')
