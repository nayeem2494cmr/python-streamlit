import streamlit as st
#EDA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use("Agg")

# def main():
#     activities=['EDA','PLOTS']
#     choices = st.sidebar.selectbox("select Activities", activities)
#     if choices=="EDA":
#         st.subheader("Exploratory Data analysis")
#         data=st.file_uploader("Upload a dataset",type=['csv',"txt"])
#         if data is not None:
#             df=pd.read_csv(data)
#             st.dataframe(df.head())
#         if st.checkbox("Show shape"):
#             st.write(df.shape)
#         if st.checkbox("Show Info"):
#             st.write(df.info)
#         if st.checkbox("Show describe"):
#             st.write(df.describe())
#         if st.checkbox("Show columns"):
#             all_columns = df.columns.to_list()
#             st.write(all_columns)
#         if st.checkbox("Show selected columns"):
#             selected_columns = st.multiselect("Select Columns",all_columns)
#             new_df = df[selected_columns]
#             st.dataframe(new_df)
#         if st.checkbox("Show selected value count"):
#             st.write(df.iloc[:, -1].value_counts())
#         if st.checkbox("Correlation Matrix"):
#             plt.matshow(df.corr())
#             st.pyplot()
#         if st.checkbox("Corelation Matrix(Seaborn)"):
#             st.write(sns.heatmap(df.corr(),annot=True))
#             st.pyplot()
#     elif choices == 'Plots':
#         st.subheader('Data Visualization')
#         data=st.file_uploader("Upload a dataset",type=['csv',"txt",'xlsx'])
#         if data is not None:
#             df=pd.read_csv(data)
#             st.dataframe(df.head())
#         if st.checkbox("Show value count"):
#             st.write(df.iloc[:, -1].value_counts().plot(kind="bar"))
#             st.pyplot()
#         # all_columns=df.columns.to_list()
#         # type_of_plot=st.selectbox("select plot type",['area',"bar","line","hist","box","kde"])
#         # selected_columns = st.multiselect("select columns to plot",all_columns)

def main():
    activies=['EDA', 'PLOTS']
    choices = st.sidebar.selectbox("Select Activities", activies)
    if choices=="EDA":
        st.subheader("Exploratory Data Analysis")
        data=st.file_uploader("Upload a dataset", type=["csv", "txt"])
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())
        if st.checkbox("Show Shapes"):
            st.write(df.shape)
        if st.checkbox("Show Describe"):
            st.write(df.describe())
        if st.checkbox("Show Columns"):
            all_columns = df.columns.to_list()
            st.write(all_columns)
        if st.checkbox("Show Selected Columns"):
            selected_columns  = st.multiselect("Select Columns", all_columns)
            new_df = df[selected_columns]
            st.dataframe(new_df)
        if st.checkbox("Show Value Counts"):
            st.write(df.iloc[:, -1].value_counts())
        if st.checkbox("Correlation Matrix"):
            plt.matshow(df.corr())
            st.pyplot()
        if st.checkbox("Correlation Matrix(Seaborn)"):
            st.write(sns.heatmap(df.corr(), annot=True))
            st.pyplot()
    elif choices == 'PLOTS':
        st.subheader("Data Visulization")
        data=st.file_uploader("Upload a dataset", type=["csv", "txt", "xlsx"])
        if data is not None:
            df=pd.read_csv(data)
            st.dataframe(df.head())
            if st.checkbox("Show Value Counts"):
                st.write(df.iloc[:, -1].value_counts().plot(kind="bar"))
                st.pyplot()
            all_columns = df.columns.to_list()
            type_of_plot = st.selectbox("Select plot type", ["area","bar","line","hist", "box","kde"])
            selected_columns = st.multiselect("Select columns to plot", all_columns)

            if st.button("Generate Plot"):
                st.success("Plot is Generated")
                if type_of_plot=='area':
                    new_extracted_df = df[selected_columns]
                    st.area_chart(new_extracted_df)
                if type_of_plot=='bar':
                    new_extracted_df = df[selected_columns]
                    st.bar_chart(new_extracted_df)
                if type_of_plot=='line':
                    new_extracted_df = df[selected_columns]
                    st.line_chart(new_extracted_df)
                else:
                    new_extracted_df_plot = df[selected_columns].plot(kind=type_of_plot)
                    st.write(new_extracted_df_plot)
                    st.pyplot()

#main
if __name__=="__main__":
    main()