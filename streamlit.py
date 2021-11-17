"""
    스트림릿 데모 웹 페이지
    TODO:
    NOTES:
        - 스트림릿 데모 웹 페이지
        1) 사용자가 토마토 잎사귀 이미지를 업로드 하면
        2) 플라스크 REST API 서버로 request 되고
        3) 인퍼런스 진행 된 response 결과를 파싱 해서
        4) Streamlit 화면에 뿌림
    UPDATED:
    REFERENCE:
        - https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/
        - https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py
"""

# 라이브러리 로드
import streamlit as st
import pylab
import matplotlib as mpl
import matplotlib.backends
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
from PIL import Image
import requests
import json
import datetime

# Stremlit 데모 웹 페이지 작성

# 사이드 바 : 프로젝트 선택
add_selectbox = st.sidebar.selectbox("프로젝트", ("토마토 잎사귀 병충해 분류기", " "))

# 타이틀
st.title("KIWON AI")

# 헤더
st.header("토마토 잎사귀 병충해 분류기")
st.header(" ")
st.header(" ")
st.write(' - 프로젝트 개요 : ')

# 추가 설명 : 토마토 잎사귀 병충해 설명
with st.expander('더 보기'):
    st.write('- 품질 좋고 맛 좋은 토마토를 생산하기 위해서는 성장에 영향을 미치는 요인 (온도, 습도, 햇빛, 병충해 발생 등)들이 중요합니다.')
    st.write('- 병충해는 식물의 잎, 줄기, 뿌리, 열매 등 다양한 곳에서 발생 할 수 있습니다.')
    st.write('- 병충해로부터 재배중인 과일이나 채소를 보호하는 것이 농산물 품질과 수확량을 보장하는데 필수적 요소입니다.')
    st.write('- 병충해를 조기 발견 하고 적절한 처방으로 병충해 확산을 방지 하는 것이 중요합니다.')
    st.write('- 농부가 수시로 모니터링 해서 병충해를 발견 하는 것은 비효율적입니다. 따라서 식물을 효과적으로 보호하기 위해서는 자동화 감지 및 식별이 필요합니다.')

st.header(" ")
st.header(" ")
st.markdown("---------------")
st.header(" ")
st.header(" ")

# 코드 실행 도중 출력 메시지
with st.spinner('Wait...'):
    # time.sleep(2) # 2초 대기
    image = st.file_uploader('토마토 잎사귀 이미지 업로드 : ') # 이미지 업로드
    st.header(" ")

    if image != None: # 이미지가 업로드 됐을 경우에만 실행
        # 플라스크 REST API 서버에 request 보내기
        before_inference_time = datetime.datetime.now()
        resp = requests.get("http://127.0.0.1:5000/inference", # API 주소
                    files={"file": image}) # 인퍼런스 할 이미지
        inference_result = resp.json() # 인퍼런스 결과
        inference_result = inference_result['inference_result'] # 인퍼런스 결과 파싱
        after_inference_time = datetime.datetime.now()

        st.write(' - 이미지 : ')
        st.image(image) # 인퍼런스 한 이미지 출력
        st.header(" ")
        st.write(' - 분류 결과 : ')
        st.write(str(inference_result)) # 인퍼런스 결과 출력
        st.header(" ")
        st.write(' - 소요 시간 : ')
        st.write(after_inference_time - before_inference_time)# 인퍼런스 소요 시간 출력
        st.success('Success!') # 성공 시 메시지
        st.balloons() # 풍선 효과

# 텍스트 : 결과 해석 (질병 설명)
st.header(" ")
st.header(" ")
st.markdown("---------------")
st.header(" ")
st.header(" ")
st.header("결과 해석")
st.header(" ")
st.write(" - 0 : 궤양병")
st.write(" - 1 : 잎곰팡이병")
st.write(" - 2 : 점무늬병")
st.write(" - 3 : 토마토퇴록바이러스")
st.write(" - 4 : 황화잎말림바이러스")
st.write(" - 5 : 흰가루병")
st.write(" - 6 : 정상")
st.write(" - 7 : 아메리카잎굴파리")
st.write(" - 8 : 청벌레")
st.write(" - 9 : 아메리카잎굴파리(ROI)")