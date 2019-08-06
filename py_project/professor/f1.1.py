# 프로젝트 절차
# 기획(아이템수집->제안서/기획서/전체일정)
# ->개발(요구사항분석->개발계획서[개발일정/업무분담/기술분석])
# ->테스팅/디버깅->오픈베타테스트등등->수정->런칭
# 1. 모듈 가져오기
from flask import Flask

# 2. 앱생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
@app.route('/')
def home():
    return "home page"

# ~/login 이라는 요청을 처리하는 웹서비스를 구성하시오
@app.route('/login')
def login():
    return "login page"

# ~/logout 구현
@app.route('/logout2')
def logout():
    return "logout page"

# 4. 서버 가동
if __name__ == '__main__':
    # 디버깅 모드를 사용하면 내가 수정한 내용이 반영되어 
    # 자동으로 재가동된다 -> 즉 자동반영된다
    app.run(debug=True)