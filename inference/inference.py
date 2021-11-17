"""
    인퍼런스
    TODO:
    NOTES:
        - pytorch 기반 모델 인퍼런스
        1) 학습 된 모델을 폴더 구조에 넣어 두고
        2) 학습 된 모델을 미리 정의 해 둔 틀에 끼워서 로드 한 후
        3) 정규화 해서
        4) 요청이 들어 올 때 마다 결과 출력 하여 반환
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

# 클래스 정의 : InferenceResult
class InferenceResult:
    # 클래스 초기화
    def __init__(self, input_shape, trained_model_path):
        self.input_shape = input_shape # input shape
        self.trained_model_path = trained_model_path # 학습 된 모델 경로
    
    # 함수 : 학습 된 모델 로드
    def _trained_model_load(self):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu') # device
        self.model = PestClassifier(num_class=10).to(device) # 미리 정의해 둔 모델 틀
        self.model.load_state_dict(torch.load(self.trained_model_path, map_location=torch.device('cpu'))['model']) # 모델을 미리 정의 해 둔 틀에 끼워서 로드
        self.model.eval() # 모델을 추론에만 사용하므로 'eval' 모드로 변경
        return self.model

    # 함수 : 인퍼런스 이미지 로드 및 transform
    def _image_load(self, image_bytes):
        transform_logic = transforms.Compose([transforms.Resize(self.input_shape), transforms.ToTensor(), transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]) # 정규화 정의
        image = Image.open(io.BytesIO(image_bytes)) # 인퍼런스 이미지 로드
        self.transformed_image = transform_logic(image).unsqueeze(0) # 이미지에 트랜스폼 적용
    
    # 함수 : 인퍼런스 결과
    def _get_inference_result(self, model):
       outputs = model.forward(self.transformed_image) # 인퍼런스
       _, y_hat = outputs.max(1) # 인퍼런스 결과
       outputs = str(y_hat.item()) # 인퍼런스 결과 (보기 좋게 변경)
       return outputs