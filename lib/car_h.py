class Car: 
	def __init__(self, brand, model, cons, rid, h_cost, d_cost, w_cost, taken):
		self.brand = brand
		self.model = model
		self._cons = cons  # fuel consuption
		self._rid = rid  # registration id number
		self._h_cost = h_cost  # cost per hour
		self._d_cost = d_cost  # cost per day, let it be hour_cost*10
		self._w_cost = w_cost  # cost per week, let it be hour_cost*60
		self.taken = taken # 0 or 1
