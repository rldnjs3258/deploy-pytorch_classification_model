# Tomato Disease Classification Model Deploy
 - 플라스크 API (모델 서빙) reference 1 : https://seokhyun2.tistory.com/43
 - 플라스크 API (모델 서빙) reference 2 : https://tutorials.pytorch.kr/intermediate/flask_rest_api_tutorial.html
 - Streamlit reference 1 : https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/
 - Streamlit reference 2 : https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py

<br>
<hr>
<br>

## 1. Streamlit이란?
 - 데모 형식으로 웹을 만들 수 있는 프레임워크
 - 단점 : Interactive (파라미터, input shape, batch size 등 사용자가 화면에서 선택 할 경우) 한 동작이 발생 할 경우 새로 고침이 됨 -> form과 submit 이용해야 함

<br>
<hr>
<br>

## 2. How to run
##### 1-1) 플라스크 API 서버 (모델 서빙) : python flask_server.py
 - 터미널을 열어 플라스크 API 서버 (모델 서빙)을 먼저 실행 합니다.
##### 1-2) (Option) 플라스크 API 서버 (모델 서빙) 테스트 : python flask_test.py
 - '필요 시' 터미널을 열어 플라스크 API 서버 (모델 서빙)을 테스트 합니다.
##### 2-1) Streamlit : streamlit run streamlit.py
 - 터미널을 열어 Stremlit으로 개발 된 데모 웹 페이지를 실행 합니다.
##### 2-2) 사용자는 http://127.0.0.1:5000/으로 웹 페이지에 접근 가능 합니다.

<br>
<hr>
<br>

## 3. DIR 구조 설명
 - inference/ : 인퍼런스가 진행 되는 로직입니다. (학습 된 모델을 폴더 구조에 넣어 두고 > 모델을 미리 정의 해 둔 틀에 끼워서 로드 한 후 > 정규화 해서 > 요청이 들어 올 때 마다 결과 출력 하여 반환)
 - inference_image/ : 인퍼런스 할 이미지를 담는 곳입니다. (테스트 용)
 - model/ : 학습 된 모델 '틀'을 담는 곳입니다.
 - trained_model/ : 학습 된 모델을 담는 곳입니다.
 - flask_server.py : 플라스크 API 서버 (모델 서빙) 실행 파일
 - flask_test.py : 플라스크 API 서버 (모델 서빙) 테스트 파일
 - requirements.txt : 필요 라이브러리 설치
 - streamlit.py : 스트림릿 데모 웹 페이지

<br>
<hr>
<br>

## 4. 프로젝트 진행 순서
##### 1) 토마토 잎 분류 best 모델 저장
##### 2) 플라스크 API 서버 (모델 서빙) 개발
##### 3) 플라스크 API 서버 (모델 서빙) 테스트
##### 4) 스트림릿 데모 웹 페이지 개발

<br>
<hr>
<br>

## 5. 아키텍쳐 설명
##### 1) 인퍼런스 로직 (PyTorch)
 - 학습 된 모델 로드 (나의 best 모델을 로컬 특정 폴더에 위치 시키기!)
 - 인풋 이미지 정규화
 - Request 발생 시 인퍼런스 결과 반환

<br>

##### 2) 모델 서빙 (Flask)
 - Request 이미지 파일
 - 인퍼런스 로직 적용
 - 요청이 들어 올 때 마다 인퍼런스 결과 반환

<br>

##### 3) 웹 페이지 (Streamlit)
 - 사용자가 이미지 업로드
 - 플라스크 API 서버로 이미지 request
 - 인퍼런스 진행 된 response 결과 파싱
 - Streamlit 화면에 뿌림

<br>
<hr>
<br>

## 6. 기타
 - 여러 데이터를 한 번에 인퍼런스 할 경우 고려하기
 - 인퍼런스가 돌 때 추가 호출이 올 경우 고려하기
 - 배치성, 실시간성, 큐에 넣고 한 번에 동작 등 여러 시나리오 고려 하기