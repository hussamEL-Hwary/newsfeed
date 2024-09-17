import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from marshmallow import ValidationError

from serializers import post_schema, post_update_schema

load_dotenv()
app = Flask(__name__)

# Database connection
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor(dictionary=True)


# Endpoint to add new post
@app.route('/posts', methods=['POST'])
def add_post():
    json_data = request.json

    # Validate input data using the schema
    try:
        data = post_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    user_check_sql = "SELECT user_id FROM User WHERE user_id = %s"
    cursor.execute(user_check_sql, (data['user_id'],))
    user = cursor.fetchone()

    if not user:
        return jsonify({"error": "User does not exist"}), 400

    # Proceed with the rest of the logic if validation passes
    sql = "INSERT INTO Post (user_id, content) VALUES (%s, %s)"
    values = (data['user_id'], data['content'])
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Post added successfully", "post_id": cursor.lastrowid}), 201


# Endpoint to update post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    json_data = request.json
    try:
        data = post_update_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    sql = "UPDATE Post SET content = %s WHERE post_id = %s"
    values = (data['content'], post_id)
    cursor.execute(sql, values)
    db.commit()
    return jsonify({"message": "Post updated successfully"})


if __name__ == '__main__':
    app.run(debug=True)
