"""
    플라스크 REST API 서버 (모델 서빙) 테스트
    TODO:
    NOTES:
        - 플라스크 REST API 서버 (모델 서빙) 테스트
        1) 플라스크 REST API 서버 (모델 서빙)에 request (이미지)를 보내서
         (테스트이기 때문에 이미지는 폼 입력 값이 아닌 하드 코딩)
        2) 인퍼런스 진행 된 response 결과를 봄
    UPDATED:
    REFERENCE: https://tutorials.pytorch.kr/intermediate/flask_rest_api_tutorial.html
"""

# 라이브러리 로드
import requests
import json

# 플라스크 REST API 서버 (모델 서빙)에 request 보내기
resp = requests.get("http://127.0.0.1:5000/inference", # API 주소
                     files={"file": open('inference_image/10004.png','rb')}) # 인퍼런스 할 이미지
inference_result = resp.json() # 인퍼런스 결과

# 인퍼런스 결과 출력
print(inference_result)