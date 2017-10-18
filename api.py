from flask import Flask,request,redirect
from alipay import place_order,getOrderId,notify_verify
app=Flask(__name__)
@app.route("/alipay",methods=["GET"])
def alipay():
    mon=request.args.get("money")
    if mon:
        l=dir(alipay)
        url=place_order(getOrderId(),float(mon),"test",return_url="baidu.com")
        print(url)
        return redirect(url, code=302)
    return "error"
@app.route("/callback")
def callback():
    if request.method=='POST':
        param=request.form.to_dict()
    elif request.method=='GET':
        param=request.args.to_dict()
    else:
        return "error"
    print(param)
    re=notify_verify(param)
    print(re)
    return "success"


app.run(port=7002)
