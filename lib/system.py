import json
import random
from lib.car_h import Car


class System:  # factory pattern

	def __init__(self, N=20):  # no of cars in the db
		#self.__database = []
		models = {  "BMW" : ["228GranCoupe", "330e", "X5"],
					"Porsche" : ["CayenneS", "911Carrera", "Panamera4", "CayenneCoupe"],
					"Mercedes" : ["S63Coupe", "GLC350e"],
					"VW" : ["GolfGT", "AtlasCrossSport", "JettaA7"]}
		c_brands = [random.choice(list(models.keys())) for _ in range(N)]
		c_models = [random.choice(models[c_brands[i]]) for i in range(N)]
		c_cons = [round(random.uniform(5, 25), 2) for _ in range(N)]
		c_rid = ["PB"+str(1000+i) for i in range(N)]  # unique rids
		c_h_d = [round(random.uniform(20, 30), 1) for _ in range(N)]  # others will be a f of it
		self.__create_cars(N, c_brands, c_models, c_cons, c_rid, c_h_d)

	def __create_cars(self, N, c_brands, c_models, c_cons, c_rid, c_h_d):  # create/load the cars
		cars = []
		for ind in range(N):
			cars.append(Car(c_brands[ind], c_models[ind], c_cons[ind],\
							c_rid[ind], c_h_d[ind], c_h_d[ind]*10, c_h_d[ind]*60, 0).__dict__)
		with open("mock_DB.json", "w") as file:  # with guarantees file closes properly
			file.write(json.dumps(cars, indent=4))
		print("S: {} cars have been successfully added to the database.\n".format(N))

	def __calc_sum(self, which_car, time_amount, time_type, promotion):  # types are h,d,w
		cost = which_car[time_type] * time_amount
		if promotion: return 0.3 * cost  # apply discount
		else: return cost

	def __update_db(self, which_car):
		with open("mock_DB.json", "r") as file:
			cars = json.loads(file.read())
		cars.remove(which_car)
		which_car["taken"] ^= 1  # toggle the availability state -> no need to check if it was taken
		#which_car["last_up"] = datetime.now()
		cars.append(which_car)
		with open("mock_DB.json", "w") as file:  # with guarantees file closes properly
			file.write(json.dumps(cars, indent=4))


	def see_av_cars(self):
		with open("mock_DB.json", "r") as file:
			cars = json.loads(file.read())
		print("S: Cars available now are:")
		for elem in cars:
			if not elem["taken"]:
				print("S: -> "+elem["brand"]+" "+elem["model"]+", consumpion:"+\
							str(elem["_cons"])+"L, hour cost:"+str(elem["_h_cost"])+"$.")
		print("S: Daily cost is found by multiplying the hour cost by 10.")
		# this is not used as advantage in the calculation,
		# but only as simplification of the generation of the data
		print("S: Weekly cost is found by multiplying the hour cost by 60.\n")

	def process_rent_request(self, which_brand, which_model, time_amount, time_type, promotion):
		taken_flag = 0
		with open("mock_DB.json", "r") as file:
			cars = json.loads(file.read())
		for elem in cars:  # check first if the car is available
			if elem["brand"] == which_brand and elem["model"] == which_model:
				if not elem["taken"]:
					print("S: Your car is being requested. We are calculating the price.")
					price = self.__calc_sum(elem, time_amount, time_type, promotion)
					if promotion: print("S: We are applying 30% discount, since you rent >=3 cars.")
					print("S: {0:.2f}$ have been withdrawn from your account.".format(price))
					self.__update_db(elem)
					print("S: The registration number of this car is {}.".format(elem["_rid"]))
					print("S: You can now use the car until the end of the time period.\n")
					return 1  # rent request was successful
				else: taken_flag = 1
		if taken_flag: print("S: Sorry but this car is taken.\n")
		else: print("S: Sorry, but we do not offer such a car.\n")
		return 0  # rent request was not possible
