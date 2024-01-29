from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears
        self.tire_need_to_service = 0.9

    def needs_service(self):
        for tire in self.tire_wears:
            if tire >= self.tire_need_to_service:
                return True
        return False