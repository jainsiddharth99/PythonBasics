from flask import Flask,session
from checker import check_logged_in
app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello from simple webapp'

@app.route('/page1')
@check_logged_in
def page1():
    return 'page1'
@app.route('/page2')
@check_logged_in
def page2():
    return 'page2'
@app.route('/page3')
@check_logged_in
def page3():
    return 'page3'

@app.route('/login')
def do_login()->str:
    session['logged_in']=True
    return 'you are now logged in'

@app.route('/logout')
def do_logout():
    session.pop('logged_in')
    return 'you are now logged out'

app.secret_key='youwillneverguessmysecretkey'

if __name__==('__main__'):
    app.run(debug=True)
