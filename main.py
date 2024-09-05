from openai import OpenAI
import time
import streamlit as st

# OpenAI API 키 설정
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 제목
st.title('당신에 필요한 휴식은? 😌')

# 사용자 입력
work_description = st.text_area("평소에 무슨 일을 해요?")
books_per_year = st.number_input("1년에 책은 몇 권 읽어요?", min_value=0, step=1)
computer_usage = st.slider("하루에 몇 시간 정도 컴퓨터를 사용해요?", min_value=0, max_value=24, step=1)

if st.button('결과 보기 🚀'):
    st.write('결과를 기다려주세요...')

    # ChatGPT API를 통해 피드백 생성
    prompt = f"""
    사용자의 일상: {work_description}
    연간 책 읽기 수: {books_per_year}
    컴퓨터 사용 시간: {computer_usage}
    사용자가 번아웃 상태일 수 있으며, 어떤 휴식이 필요한지 400자 내외로 피드백을 제공해 주세요.
    """

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )

    chat_result = response.choices[0].text.strip()

    # DALL·E 또는 유사 이미지 생성 API 호출
    image_response = openai.Image.create(
        prompt="a serene and peaceful landscape",
        n=1,
        size="1024x1024"
    )

    image_url = image_response.data[0].url

    st.write("**피드백**")
    st.write(chat_result)

    st.write("**평화를 주는 이미지**")
    st.image(image_url)
