import streamlit as st
import pickle as pk
import pandas as pd
import plotly.graph_objects as go


def get_clean_data():
     # read the data into a pandas data frame
    data = pd.read_csv('../data/data.csv')
    # remove null values:
    data = data.dropna(axis = 1)
    # rename the Target Lables from Malignant to 1 and Benign to 0
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B':0})
    
    return data

def uplaod_data():
    st.sidebar.header("Cell Nuclei Details")
    
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a CSV with your data", type='csv')
        st.markdown('''
                    *File must in the following format:*
                    '''
                     )
        example_data = {'Feature' : ['radius_mean', 'texture_mean', '....'], 
                        'Values' : ['17.9', '10.38', '....']}
        st.subheader("Cell Nuclei Details")
        st.table(example_data)
    
    if uploaded_file is not None:
        # Load CSV file into a DataFrame
        df = pd.read_csv(uploaded_file, header=None, names=["Feature", "Value"])

        df['Feature'] = df['Feature'].str.rstrip()
        
        data_dict = dict(zip(df["Feature"], df["Value"]))
        
        
        
        return data_dict

    return None

def input_data():
    with st.sidebar:
        st.header("Alternatively Enter Values Manually")
        data = get_clean_data()
        side_barlabels = [
    ('Radius (mean)', 'radius_mean'),
    ('Texture (mean)', 'texture_mean'),
    ('Perimeter (mean)', 'perimeter_mean'),
    ('Area (mean)', 'area_mean'),
    ('Smoothness (mean)', 'smoothness_mean'),
    ('Compactness (mean)', 'compactness_mean'),
    ('Concavity (mean)', 'concavity_mean'),
    ('Concave Points (mean)', 'concave points_mean'),
    ('Symmetry (mean)', 'symmetry_mean'),
    ('Fractal Dimension (mean)', 'fractal_dimension_mean'),
    ('Radius (SE)', 'radius_se'),
    ('Texture (SE)', 'texture_se'),
    ('Perimeter (SE)', 'perimeter_se'),
    ('Area (SE)', 'area_se'),
    ('Smoothness (SE)', 'smoothness_se'),
    ('Compactness (SE)', 'compactness_se'),
    ('Concavity (SE)', 'concavity_se'),
    ('Concave Points (SE)', 'concave points_se'),
    ('Symmetry (SE)', 'symmetry_se'),
    ('Fractal Dimension (SE)', 'fractal_dimension_se'),
    ('Radius (worst)', 'radius_worst'),
    ('Texture (worst)', 'texture_worst'),
    ('Perimeter (worst)', 'perimeter_worst'),
    ('Area (worst)', 'area_worst'),
    ('Smoothness (worst)', 'smoothness_worst'),
    ('Compactness (worst)', 'compactness_worst'),
    ('Concavity (worst)', 'concavity_worst'),
    ('Concave Points (worst)', 'concave points_worst'),
    ('Symmetry (worst)', 'symmetry_worst'),
    ('Fractal Dimension (worst)', 'fractal_dimension_worst')
]
        input_dict = {}
        
        for label, key in side_barlabels:
            input_dict[key] = st.slider(
                label= label,
                min_value= float(0),
                max_value= float(data[key].max()),
                # default value:
                value= float(data[key].mean())
            )
    return input_dict

def get_chart_data(input_data):
    categories = ['Radius', 'Texture', 'Fractal Dimension', 
                  'Symmetry', 'Concave Points', 
                  'Concavity', 'Compactness', 
                  'Smoothness', 'Area', 'Perimeter']
    
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
            input_data['radius_mean'], input_data[]
            
            ],
        theta=categories,
        fill='toself',
        name='Mean'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=[4, 3, 2.5, 1, 2],
        theta=categories,
        fill='toself',
        name='Standard Error'
    ))
    
    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 5]
        )),
    showlegend=False
    )
    
    st.plotly_chart(fig)
    
def main():
    # Set the Page configuration
    st.set_page_config(
        page_title= "Breast Cancer Prediction Application",
        page_icon= ":female-doctor",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Upload Data using csv
    uploaded_data = uplaod_data()
    # Input data manually using sliders:
    slider_data = input_data()
    
    with st.container():
        
        st.title("Breast Cancer Predictor")
        st.write("This app allows predicts using machine learning whether a breast mass is benign or malignant based on the measurements it recieves from your cytosis lab. The data was trained using Wisconsin dataset(https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)")
        col1, col2 = st.columns([4, 1])
        
        if uploaded_data is not None:
            with col1:
                st.markdown(
                    '''
                    ## Using Data from CSV File
                    '''
                )
                data = uploaded_data 
                  

        else:
            with col1:
                st.markdown(
                    '''
                    ## Using Data from Sliders
                    '''
                )
                data = slider_data
                
        get_chart_data(data)
        
        
    








if __name__ == '__main__':
    main()