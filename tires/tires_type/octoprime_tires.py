from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tire_wears):
        self.tire_wears = tire_wears
        self.tire_need_to_service = 3.0

    def needs_service(self):
        return sum(self.tire_wears) >= self.tire_need_to_service