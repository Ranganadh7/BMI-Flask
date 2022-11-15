from flask import *

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def a():
    w,h='',''
    bmi=0.0
    if request.method=='POST' and 'weight' in request.form:
        w=float(request.form.get('weight'))
        h=float(request.form.get('height'))

        bmi=w/(h*h)
        bmi=round(bmi,2)
        bmi=float(bmi)


    return render_template('bmi.html',height=h,weight=w,bmi=bmi)


app.run(debug=True)
