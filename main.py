from lib.client import Client
from lib.system import System

import random

n = 15  # no of cars in the mock db
SYS = System(n)
CLI = Client("C")
CLI1 = Client("D")
m = 20  # no cars to be requested

models = {  "BMW" : ["228GranCoupe", "330e", "X5"],
			"Porsche" : ["CayenneS", "911Carrera", "Panamera4", "CayenneCoupe"],
			"Mercedes" : ["S63Coupe", "GLC350e"],
			"VW" : ["GolfGT", "AtlasCrossSport", "JettaA7"]}

# now I will be generating lists of m elements
some_brands = [random.choice(list(models.keys())) for _ in range(m)]
some_models = [random.choice(models[some_brands[i]]) for i in range(m)]
# some sample data

CLI.request_av_cars(SYS)
CLI1.request_av_cars(SYS)

for i in range(m):  # to test each method
	if i % 3 == 0: CLI.request_rent_hourly(syst=SYS, which_brand=some_brands[i], which_model=some_models[i], no_hours=random.randint(4, 12))
	elif i % 3 == 1: CLI1.request_rent_daily(syst=SYS, which_brand=some_brands[i], which_model=some_models[i], no_days=random.randint(1, 7))
	else: CLI.request_rent_weekly(syst=SYS, which_brand=some_brands[i], which_model=some_models[i], no_weeks=random.randint(1, 6))
	if not i % (m//2+1): CLI.request_av_cars(SYS)  # print the available list 2 times
	if not i % (m//3+1): CLI1.request_av_cars(SYS)  # print comes from the other client here

CLI.request_av_cars(SYS)
