import streamlit as st
st.set_page_config(page_title="목윤서의 자기소개",layout="centered")
st.title("안녕하세요 반갑습니다")
st.subheader("웹툰작가 지망생 지망생 입니다.")
st.write("수학숙제와 미술숙제가 밀렸습니다.")
col1,col2=st.columns([1,2])
with col1:
    st.image("https://via.placeholder.com/150",caption="목윤서",width=150)
with col2:
    st.markdown("### About Me")
    st.write("위치 대한민국 서울")
    st.write("이메일 stream@example.com")
    st.write("깃허브 github.com/yourid")
    st.write("블로그 myblog.dev")
st.markdown("### Tech Stacks")
st.markdown("Languages")
st.code("Python SQL HTML CSS",language="text")
st.markdown("Frameworks Tools")
st.code("Streamlit FastAPI Git Docker",language="text")
st.markdown("### Projects")
with st.expander("1 늦게까지 밀린 숙제 하다가 학교에서 졸기"):
    st.write("기간 202605 202606")
    st.write("지금도 졸려요")
    st.write("토요일은 밤 새고 학원에 갔어요")
with st.expander("2 국영수사과 관두고 그림만 그리고 싶어하기"):
    st.write("기간 매일")
    st.write("졸려요")
    st.write("아 너무 졸린데")
st.markdown("### 방명록을 남겨주세요")
visitor_name=st.text_input("이름 또는 닉네임")
visitor_message=st.text_area("메시지")
if st.button("보내기"):
    if visitor_name and visitor_message:
        st.success(f"{visitor_name}님의 소중한 메시지가 전달되었습니다 감사합니다")
        st.info(f"{visitor_name} {visitor_message}")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요")