from flask import Flask
app=Flask(__name__)



@app.route('/')
def index():
    return 'hkjlkjkhhkkhljjjjjjjjjjjljklome'

if __name__=="__main__":
    app.run()


@app.route('/home')
def printname():
    return ""

