from flask import Flask, request, abort, jsonify
import json

from .firestore_client import fs

app = Flask(__name__)

@app.route("/", methods=['GET'])
def route_index():
    response = {'message': 'hello'}
    return json.dumps(response)


@app.route("/fs/<string:collection_id>/<string:doc_id>", methods=['GET'])
def fs_get(collection_id, doc_id):
    response = {'success': True}

    doc_ref = fs.collection(collection_id).document(doc_id)
    doc = doc_ref.get()
    if doc.exists:
        response = doc.to_dict()
    else:
        response = {}

    return json.dumps(response)


@app.route("/fs/<string:collection_id>/<string:doc_id>", methods=['POST'])
def fs_post(collection_id, doc_id):
    response = {'success': True}

    if request.headers.get('Content-Type') != 'application/json':
        abort(400, {'message': 'Content-Type is not application/json'})
    
    if not request.data:
        abort(400, {'message': 'Invalid request'})
    
    doc_ref = fs.collection(collection_id).document(doc_id)
    print(f'INFO: register {request.data} in {collection_id}/{doc_id}')
    registeration_data = request.json
    doc_ref.set(registeration_data)

    return json.dumps(response)


@app.route("/fs/<string:collection_id>/<string:doc_id>", methods=['PUT'])
def fs_put(collection_id, doc_id):
    response = {'success': True}

    if request.headers.get('Content-Type') != 'application/json':
        abort(400, {'message': 'Content-Type is not application/json'})
    
    if not request.data:
        abort(400, {'message': 'Invalid request'})
    
    doc_ref = fs.collection(collection_id).document(doc_id)
    update_data = request.json
    print(f'INFO: update {json.dumps(update_data)} in {collection_id}/{doc_id}')
    doc_ref.update(update_data)

    return json.dumps(response)


@app.route("/fs/<string:collection_id>/<string:doc_id>", methods=['DELETE'])
def fs_delete(collection_id, doc_id):
    response = {'success': True}
    
    doc_ref = fs.collection(collection_id).document(doc_id)
    doc_ref.delete()

    return json.dumps(response)


@app.errorhandler(400)
@app.errorhandler(405)
def error_handler(error):
    """
    abort(400),abort(405) リクエストエラーのハンドラ
    """
    response = jsonify({'message': error.description, 'result': error.code})
    return response, error.code


if __name__ == "__main__":
    app.run(host='0.0.0.0')