try:
	from server import app
	import unittest

except Exception as e:
	print(f"Missing modules: {e}")

class FlaskTestCase(unittest.TestCase):
	# Check for response 200
	def test_index(self):
		test_client = app.test_client(self)
		response = test_client.get("/")
		status_code = response.status_code
		self.assertEquals(status_code, 200)

if __name__ == "__main__":
	unittest.main()
