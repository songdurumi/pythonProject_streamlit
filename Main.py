import streamlit as st
import pandas as pd

st.set_page_config(
	page_title='Streamlit 프로토타입 만들기',
	page_icon='🎈',
	layout='wide'
)

st.text('🎈Streamlit 프로토타입 만들기')
st.title('📌Title을 입력하세요.')
st.header('송영학의 웹페이지')
st.subheader('Subheader(세부 머리글)을 입력하세요.')
st.markdown('안녕하세요 여러분\n\n'
			'저는 송영학 입니다')
st.markdown('# H1 #')
st.markdown('## H2 ##')
st.markdown('### H3 ###')
st.markdown('#### H4 ####')
st.markdown('##### H5 #####')
st.markdown('###### H6 ######')
st.markdown("1. 하나")
st.markdown("2. 둘")
st.markdown("3. 셋")
st.markdown("* 하나")
st.markdown("* 둘")
st.markdown("* 셋")
st.caption('이것은 caption 입니다')
st.code("코드 블록 표시")




stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'
index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'
df_stocks = pd.read_csv(stocks_file)
df_index = pd.read_csv(index_file)

st.dataframe(df_stocks)

st.dataframe(df_index.style.highlight_max(axis=0))

symbol = st.selectbox('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()))
st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])

symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL', key='df')
st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])