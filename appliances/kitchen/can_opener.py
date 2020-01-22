from appliances import Appliance

class CanOpener(Appliance):

    def __init__(self, color, heat_method):
        super().__init__(color, heat_method)

    def open_can(self):
        print("Tuna smells bad")
