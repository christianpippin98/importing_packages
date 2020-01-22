from appliances.kitchen.utility.dishwasher import DishWasher
from appliances.laundry.dryer import Dryer
from appliances.laundry.washer import Washer
from appliances.kitchen.utility.refrigerator import Refrigerator
from appliances.appliance import Appliance
from appliances.kitchen.coffeemaker import CoffeeMaker
from appliances.kitchen.can_opener import CanOpener

whirlpool_dishwasher = DishWasher("black", "electric")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "coal")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless", "electric")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white", "electric")
mr_coffee.make_coffee()

poppa_can = CanOpener("pink", "propane")
poppa_can.open_can()