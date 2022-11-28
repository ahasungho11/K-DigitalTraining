

# <span style="color: #6666FF">사전 확인사항 & GPU 준비</span>
***

1. 내 PC 환경 확인하기
  1) GPU 체크 -> 
    - 내 PC에 장착된 GPU 모델 확인
    -- [윈도우키+X] > 장치관리자 클릭 > 디스플레이 어댑터 클릭 > 모델명 확인 
    -- [ NVIDIA GeForce RTX 3060 Laptop GPU ]

![[Pasted image 20221030141419.png]]

https://developer.nvidia.com/cuda-gpus

![[Pasted image 20221030141338.png]]
**1. 내 PC에 장착된 GPU 모델 확인**  
[윈도우키+X] > 장치관리자 클릭 > 디스플레이 어댑터 클릭 > 모델명 확인
  
  
  ***
  2) 아나콘다(Anaconda) 설치
  ![[Pasted image 20221030142933.png|300x250]]
  
  
  
  
  
  3) 파이썬 

```
import sys

print("--sys.version—")
print(sys.version)
```

```
3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)]
```

  2) 윈도우

```
에디션 : Windows 11 Pro
버전 : 22H2
```

  
  
  
  
  3) 
  4) 

Window11
- Windows Operating System Support in CUDA 11.7
- Visual Studio 2022 17.0 (컴파일러 도구)

```
Visual Studio를 설치하는 목적은 LightGBM, Surprise등의 패키지를 활용하기 위함이므로
Visual Studio 2019용 Build Tools을 설치해도 되는데, 컴퓨터 비전을 위한 전처리 등 OpenCV의 활용 가능성을 위해 여기서는 Community 라이센스를 설치한다. 버전은 위에서 확인한대로 2019을 설치한다.
```




- conda create -n tf2.0 python
- conda activate tf2.0
- pip install jupyter notebook
- pip install ipykernel
- python -m ipykernel install --user --name 가상머신이름 --display-name "표시할이름"
- 