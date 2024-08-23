from flask import Blueprint, jsonify, request
from .DataHelper import *

Data = Blueprint('Data', __name__)

@Data.route('getbranch', methods=['POST'])
def getbranch():
    try:
        result = DataHelper.getbranch()
        return jsonify(status='Success', result=result)
    except Exception as e:
        return jsonify(status='Fail', msg=str(e))
    
@Data.route('getorder', methods=['POST'])
def getorder():
    try:
        result = DataHelper.getorder()
        return jsonify(status='Success', result=result)
    except Exception as e:
        return jsonify(status='Fail', msg=str(e))
    
@Data.route('addorder', methods=['POST'])
def addorder():
    try:
        data = request.json
        DataHelper.addorder(data)
        return jsonify(status='Success')
    except Exception as e:
        return jsonify(status='Fail', msg=str(e))
    
@Data.route('editorder', methods=['POST'])
def editorder():
    try:
        data = request.json
        DataHelper.editorder(data)
        return jsonify(status='Success')
    except Exception as e:
        return jsonify(status='Fail', msg=str(e))
    
@Data.route('deleteorder', methods=['POST'])
def deleteorder():
    try:
        data = request.json
        DataHelper.deleteorder(data['tracking_no'])
        return jsonify(status='Success')
    except Exception as e:
        return jsonify(status='Fail', msg=str(e))

@Data.route('test', methods=['POST'])
def test():
    try:
        DataHelper.test()
        return jsonify(status='Success')
    except Exception as e:
        return jsonify(status='Fail', msg=str(e))
