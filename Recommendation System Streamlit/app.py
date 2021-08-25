
import streamlit as st
import pandas as pd

st.set_page_config('Amazon Dress Recommendation System')


st.title('Amazon Fashions Recommendation System')

Org = pd.read_csv('Original.csv')
Sim = pd.read_csv('similarity.csv') 


product_list = Org['Dress_type'].values

selected_product = st.selectbox(
    "Type or select a product from the dropdown",
    range(len(product_list)),
    format_func=lambda x: product_list[x])

def get_recommendation(selected_product):
	cn=[]
	for i in Sim.iloc[selected_product]:
		cn.append(Org.iloc[i])
	return cn

if st.button('Show Recommendation'):
	re_df=get_recommendation(selected_product)
	re_df=pd.DataFrame(re_df)
	col1,col2=st.columns((1,2))
	with col1:
		st.markdown(
    f"""
    <div class="container" style="float:right;">
        <img class="logo-img" src="{Org['Image'].values[selected_product]}">
    </div>
    """,
    unsafe_allow_html=True)

	with col2:
		st.markdown('<p style="font-weight: bold;">{}</p>'.format(Org['Brand'].values[selected_product]), unsafe_allow_html=True)
		st.markdown('<p>{}</p>'.format(Org['Dress_type'].values[selected_product]), unsafe_allow_html=True)
		st.markdown('<p><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color: #565959;">₹{}</span></p>'.format(Org['Disc_price'].values[selected_product], Org['Actual_price'].values[selected_product]), unsafe_allow_html=True)


	st.markdown('<p style="font-size: 1.2rem;">Products related to this item:</p>', unsafe_allow_html=True)
	count = 0
	for i in range(4):
		for j in st.columns(3):
			if count == 10:
				break
			with j:
				st.image(re_df['Image'].values[count])
				st.markdown('<p style="text-align: center; font-weight: bold;">{}</p>'.format(re_df['Brand'].values[count]), unsafe_allow_html=True)
				st.markdown('<p style="text-align: center;">{}</p>'.format(re_df['Dress_type'].values[count]), unsafe_allow_html=True)
				st.markdown('<p style="text-align: center;"><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color: #565959;">₹{}</span></p>'.format(re_df['Disc_price'].values[count], re_df['Actual_price'].values[count]), unsafe_allow_html=True)
				count += 1





   

