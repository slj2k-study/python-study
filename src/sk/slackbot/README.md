# slack bot

* ## 실행 전 설치
        1. pip install flask
        2. pip install datetime
        3. pip install pytz
        4. pip install requests

* ## 실행 방법
        1. flask server 기동   
           flask_server.py 파일이 존재하는 디렉토리로 이동   
           export FLASK_APP=flask_server.py   
           flask run

        2. ngrok 으로 외부 도메인 획득   
           ngrok http 5000