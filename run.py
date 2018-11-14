#serves as an entry point to our application
#it gets a copy of the app package and runs it

from app import create_app

app = create_app()















# '''single delivery order API'''
	# def get(self, order_id):
	# 	"""find an order by order_id and assign it to one_order"""
	# 	"""call the get_one method from order models"""
	# one_order = Parcels.get_one(self, order_id) # import from
	# models(Parcels.get_one)

		# return make_response(jsonify(
    #   {"status": "ok",
    #   "order": one_order}), 200)
# order_id = self.order_id,
