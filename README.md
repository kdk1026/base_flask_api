# Python Flask API
#### [Python 유틸] (https://github.com/kdk1026/python_util)

## 가상환경 생성
```
python -m venv venv
```

<br />

## 가상환경 활성화
```
(Windows)
venv\Scripts\activate

(Linux/Mac)
source venv/bin/activate
```

<br />

## VS Code 인터프리터 설정 (자동으로 가상환경 켜기)
1. `Ctrl + Shift + P` -> `Python: Select Interpreter` 선택
2. 리스트에서 `./venv/Scripts/activate` 선택
3. 터미널 새로 열기 `Ctrl + Shift + ~`

<br />

## 설치된 라이브러리 목록 추출
#### - Git에 올리는 경우
```
pip freeze > requirements.txt
```

<br />

## 라이브러리 한 번에 설치
#### - Git에서 내려받는 경우
```
pip install -r requirements.txt
```

<br /><br />

## Flask 설치
```
pip install flask
```

<br />

## 프로젝트 구조 만들기
```
app.py 생성

mkdir templates
mkdir static
```

<br />

## app.py 코드 작성

<br />

## 서버 실행
```
python app.py
```

<br />

## 앱 생성 (파일 직접 생성)
```
mkdir apps/sample
```

## app.py 에 register_blueprint 처리