"""
    플라스크 REST API 서버 (모델 서빙)
    TODO:
    NOTES:
        - 플라스크 REST API 서버 (모델 서빙)
        1) 학습 된 모델을 로드 하고
            - 모델은 main에서 로드 해서 전체 중에 '딱 1번 만 로드' 해야 함 (사용자 경험 개선)
        2) request로 받은 이미지 파일을 읽어서
        3) inference 로직에 따라 output을 생성 해서
        4) response 함
    UPDATED:
    REFERENCE: https://tutorials.pytorch.kr/intermediate/flask_rest_api_tutorial.html
"""

# 라이브러리 로드
import io
import os
import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from PIL import Image
from torchvision import transforms
from flask import Flask, jsonify, request
from model.model import PestClassifier
from inference.inference import InferenceResult

# 전역 변수 선언
trained_model_path = 'trained_model/best.pt' # 학습 된 모델 경로
input_shape = 128 # input shape

# 플라스크 : 웹앱 프로젝트
app = Flask(__name__)

# 플라스크 : 로직 정의
@app.route('/inference', methods=['GET']) # url 패턴 정의
def inference(): # 뷰 정의
    if request.method == 'GET':
        file = request.files['file'] # request로 받은 파일
        img_bytes = file.read() # request로 받은 파일 읽기
        
        # Class : InferenceResult
        inference_result = InferenceResult(input_shape, trained_model_path) # InferenceResult 클래스
        inference_result._image_load(img_bytes) # 인퍼런스 이미지 로드 및 transform
        inference_result = inference_result._get_inference_result(model) # 인퍼런스 결과

        # 인퍼런스 결과 출력
        inference_result = jsonify({'inference_result': inference_result})

        return inference_result

# 메인 정의
if __name__ == '__main__':
    # Class : InferenceResult
    #  - InferenceResult 클래스의 모델 로드는 main에 위치 해서 '1번만 로드' 해야 함 (사용자 경험 개선)
    #  - '1번만 로드 된 모델'을 이용 해 request가 올 때 인퍼런스 로직만 돌게 해야 함
    inference_result = InferenceResult(input_shape, trained_model_path) # InferenceResult 클래스
    model = inference_result._trained_model_load() # 학습 된 모델을 main에서 한 번만 로드

    # 플라스크 서버 (모델 서빙) 로컬 환경에서 run
    app.run(host='127.0.0.1', port=5000, threaded=False)