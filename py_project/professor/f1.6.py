# 주소를 쳐서 요청할때 끝에 /를 붙일것인가 아닌가?
# 1. 모듈 가져오기
from flask import Flask, request

# 2. 앱생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
# /pro or /pro/ 이것을 다같이 같은 url로 인식시키는 방법
# /pro  요청 -> /pro/
# /pro/ 요청 -> /pro/
# 라우트에서 요청 주소를 정의할때 끝에 /를 추가해 준다
@app.route('/pro/')
def home():
    return 'home page %s' % request.method

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다.')