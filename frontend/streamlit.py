from fastai.vision.widgets import *
from fastai.vision.all import *
import streamlit as st
import pathlib
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

class Predict:
    def __init__(self, filename,n):
        self.n = n
        self.learn_inference = load_learner(Path("../models")/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
        
    
 
    def get_image_from_upload(self):
        uploaded_file = st.file_uploader("Upload Image", type=['png', 'jpeg', 'jpg'], key=self.n)

        return PILImage.create(uploaded_file) if uploaded_file is not None else None

    def display_output(self):
        st.image(self.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(self):  
        if st.button('Classify',key=self.n+12):
            pred, pred_idx, probs = self.learn_inference.predict(self.img)
            st.write(f'This is the shoe "{pred}". I am {probs[pred_idx]:.04f}% certain.')
        else: 
            st.write(f'Click the button to classify') 

if __name__=='__main__':

    
    file_name='allshoesnewmodel2.pkl'
    st.title("modelAll")
    predictor = Predict(file_name,1)
    
   