class CarModelGeneration:
    def __init__(self,fuel_capacity,tire_size,max_tire_pressure):
        self.fuel_capacity = fuel_capacity
        self.tire_size = tire_size
        self.max_tire_pressure = max_tire_pressure

class CarModel:
    def __init__(self, model: str, generations: list[CarModelGeneration]):
        self.model = model
        self.generations = generations
        pass
    
    def get_num_generations(self):
        return len(self.generations)

class CarFamily:
    def __init__(self,brand: str,models: list[CarModel]):
        self.brand = brand
        self.models = models
