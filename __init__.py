from flask import Flask, render_template

# app = Flask(__name__)

def create_app(): # 애플리케이션 팩토리: 함수명으로 create_app 대신 다른 이름을 사용하면 작동하지 않는다(플라스크 내부에서 정의된 함수명임)
    app = Flask(__name__)
    
    from .views import main_views
    app.register_blueprint(main_views.bp)
    
    # @app.route('/') # app 객체가 함수 안에서 사용되므로, 원래 def 바깥에 있었던 hello_pybo 함수를 create_app 안으로 가져왔음

    #def hello_pybo():
    #    return 'debug test'
    
    return app
    
    
'''if __name__ == '__main__':
    app.run(debug=True)''' 