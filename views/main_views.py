from flask import Blueprint, render_template
from pybo.models import Question

bp=Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'hello, pybo'

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc()) # 질문 목록 데이터 획득(order_by: 조회 결과를 정렬하는 함수)
    return render_template('question/question_list.html', question_list=question_list)

# 앞으로 라우팅 함수는 이 파일에 추가하면 됨 