import streamlit as st
st.set_page_config(page_title="Mtb-bike", page_icon="🚴‍♂️", layout="wide")
tab1, tab2, tab3, tab4, tab5, tab6, = st.tabs(["Начало", "Зачем мне велик","Что он мне даст?","Буду-ли я гулять больше?","Как часто я буду его использывать?","Цена велика?"])
col1, col2, col3, col4 = st.columns([1,2,3,4])
with tab1:
        st.title("Mtb-bike")
        st.title("Почему мне нужен Mtb-bike?")
        st.subheader("Для папы и для мамы")
        st.header("На этом сайте - вы увидите зачем мне велик")
        st.image("https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcSYr_wYgQ7VMaokijjaZDMAqCDH6mNeqg5H7qDuNfsc_nA_Nk7E-p3Qw71zAL5fIfbY7jlMYmudxruM5rhkwgew3Y4B699fgW2OMXqW-Rug&usqp=CAc", width=300)
with tab2:
        st.header("Зачем мне велик - Велик мне нужен что бы я катался по городу и не сидел дома 24/7")
        st.image("https://iv.okcdn.ru/getVideoPreview?id=3848937999075&idx=9&type=39&tkn=0Axq6JgZWJfDVAOqfhoWSYtU69w&fn=vid_x", width=500)

with tab3:
        st.header("Что он мне даст?- Я буду больше гулять и буду чучуть щасливие")
with tab4:
        st.header("Буду-ли я гулять больше?- да я буду больше гулять")
with tab5:
        st.header("Как часто я буду его использывать? - Каждый раз когда буду гулять ")
with tab6:
        st.header("Цена велика? - будет 500евро ")