from flask import Flask,render_template,redirect,url_for,session, request, jsonify, make_response
from service.controller import bp_bbs as app
#디비
from service.model import dbHelper,PostModel #객체 변수 땡겨옴
from service import config


# 파일 업로드 : ~/bbs/upload ->get->폼
#~/bbs/upload ->post->등록
@app.route('/')
def home():pass
@app.route('/upload',methods=['GET','POST'])
def upload() : 
    if request.method=='GET': #업로드폼
        return render_template('upload.html',config=config)
    else : #업로드 처리
        title=request.form['title']
        content=request.form['content']
        title=request.form['title']
        writer=session['uid']
        f = request.files['file']
        #경로 밑에 계정별로 폴더를 만들어서 저장 => os 모듈
        #서버 구동 위치에 따라 경로가 달라질 수 있다(주의) -특히 단축키
        import os
        path="%s/service/static/upload/img/%s"%(os.getcwd(),f.filename)
        path=path.replace('\\','/')
        f.save(path)
        file_path="/upload/img/%s"%f.filename
        param=PostModel(title,content,writer,file_path)
        dbHelper.insertPost(param)
        return render_template("common/alert.2.html", msg="등록 성공")
        #원래 인설트 후 affected_rows가 1이 나오고 이를 체크해서 성공여부를 결정해야한다.
        #~/bbs->get-> 등록된 글 리스트
        #게시판 리스트 화면을 구현하지 않아서 그냥 돌아가기로 함.