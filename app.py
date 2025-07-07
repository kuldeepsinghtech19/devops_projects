from flask import Flask, jsonify

app = Flask(_name_)

# Dummy data
USER = {
    "name": "Kuldeep singh",
    "mobile_number": "6367888865"
}

@app.route('/get-user', methods=['GET'])
def get_user():
    return jsonify({
        "status": "success",
        "user": USER
    })

if _name_ == '_main_':
    app.run(debug=True)