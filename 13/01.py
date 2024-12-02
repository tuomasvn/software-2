from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/prime_number/<number>')
def prime(number):
	try:
		if int(number) > 0:
			inum = int(number)
			if inum == 1:
				isPrime = False
			elif inum == 2:
				isPrime = True
			else:
				for n in range (2, inum):
					if inum % n == 0:
						isPrime = False
						break
					else:
						isPrime = True
			response = {
				"Number" : number,
				"isPrime" : isPrime,
				"status" : 200
			}
			return response
		else:
			response = {
				"message" : "that's negative",
				"status" : 400
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

if __name__ == '__main__':
	app.run(use_reloader=True, host='0.0.0.0', port=5999)