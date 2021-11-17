"""
    모델 정의 클래스
    TODO:
    NOTES:
        - EfficientNet b6의 학습 된 모델 '틀'
        - 학습 된 모델.pt와 같은 형식의 '틀' (같은 형식으로 쌓은 레이어) 코드를 여기에 작성 해야 함!
    UPDATED:
    REFERENCE:
"""

# 라이브러리 로드
import torch
from torch import nn
from torch.nn import functional as F
from efficientnet_pytorch import EfficientNet
from collections import OrderedDict

# 학습 된 모델 '틀'
class PestClassifier(nn.Module):
    def __init__(self, num_class):
        super(PestClassifier, self).__init__()
        self.model = EfficientNet.from_pretrained('efficientnet-b6', num_classes=1280)

        num_features = self.model._fc.in_features
        self.model._fc = nn.Sequential(nn.Linear(num_features, 500),
                                 nn.BatchNorm1d(500),
                                 nn.ReLU(),
                                 nn.Dropout(p=0.2),
                                 nn.Linear(500, 250),
                                 nn.BatchNorm1d(250),
                                 nn.ReLU(),
                                 nn.Dropout(p=0.2),
                                 nn.Linear(250, num_class))
        
    def forward(self, input_img):
        # Model
        x = self.model(input_img)
        
        return x