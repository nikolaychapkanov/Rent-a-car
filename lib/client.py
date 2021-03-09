from lib.system import System


class Client:

	def __init__(self, first_letter):
		self._no_rented_cars = 0
		self.__msg = first_letter  # only relevant for the print messages

	def __check_for_promotion(self):  # determine if it is possible to get discount on the next car
		return self._no_rented_cars >= 2 # will return a boolean

	def request_av_cars(self, syst):
		print(self.__msg+": Please show me the available cars.\n")
		syst.see_av_cars()

	# send request for how some hours to rent a car, given its name and model
	def request_rent_hourly(self, syst, which_brand, which_model, no_hours):
		print(self.__msg+": I would like to rent a {0:s} {1:s} for {2:d} hours.\n".format(which_brand, which_model, no_hours))
		promotion = self.__check_for_promotion()
		reply = syst.process_rent_request(which_brand, which_model, no_hours, "_h_cost", promotion)
		if reply: self._no_rented_cars += 1

	def request_rent_daily(self, syst, which_brand, which_model, no_days):
		print(self.__msg+": I would like to rent a {0:s} {1:s} for {2:d} days.\n".format(which_brand, which_model, no_days))
		promotion = self.__check_for_promotion()
		reply = syst.process_rent_request(which_brand, which_model, no_days, "_d_cost", promotion)
		if reply: self._no_rented_cars += 1

	def request_rent_weekly(self, syst, which_brand, which_model, no_weeks):
		print(self.__msg+": I would like to rent a {0:s} {1:s} for {2:d} weeks.\n".format(which_brand, which_model, no_weeks))
		promotion = self.__check_for_promotion()
		reply = syst.process_rent_request(which_brand, which_model, no_weeks, "_w_cost", promotion)
		if reply: self._no_rented_cars += 1
