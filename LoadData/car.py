class CarModelGeneration:
    def __init__(self,is_electric,fuel_capacity,tire_size,cost):
        self.is_electric = is_electric
        self.fuel_capacity = fuel_capacity
        self.tire_size = tire_size
        self.cost = cost

class CarModel:
    def __init__(self, model: str, generations: list[CarModelGeneration]):
        self.model = model
        self.generations = generations
    

class CarFamily:
    def __init__(self,brand: str,models: list[CarModel]):
        self.brand = brand
        self.models = models