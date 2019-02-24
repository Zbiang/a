#coding=utf-8
from flask import Flask,jsonify,request
app = Flask(__name__) #获得 Flask 实例
 #写一个 POST 的方法，传一个 name 的参数，返回一个  json 数据
@app.route('/getJson', methods=['POST'])
def getJson():
    #bala bala,下边随便返回点东西
    name=request.form.get('name', default='windliang')
    data={
    'name':name,
    'place':'wuhan'
    }
    msg='get success'
    code=True
    return getBaseReturnValue(data,msg,code)
#返回 json 数据    
def getBaseReturnValue(data,msg,code):
  json_data = jsonify({'data':data,'msg':msg,'success':code})
  return json_data
  
if __name__ == '__main__':
    app.run(host='0.0.0.0') #在服务器上运行