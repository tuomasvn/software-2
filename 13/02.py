import json
from credentials import connection
from flask import Flask, Response

app = Flask(__name__)
@app.route('/airport/<code>')
def airport(code):
	try:
		new_airport = get_airport_from_code(code)
		airport_name = new_airport[0]
		airport_location = new_airport[1]
		response = {
			"ICAO": code,
			"name": airport_name,
			"location": airport_location,
			"status": 200
		}
		return response
	except:
		response = {
			"message" : "Invalid input",
			"status" : 400
		}
		json_response = json.dumps(response)
		http_response = Response(response=json_response, status=400, mimetype="application/json")
		return http_response

def get_airport_from_code(icao):
	sql = f"select name, municipality from airport where ident = %s"
	cursor = connection.cursor()
	cursor.execute(sql, (icao,))
	result = cursor.fetchall()
	return result[0]

if __name__ == '__main__':
	app.run(use_reloader=True, host='localhost', port=5999)