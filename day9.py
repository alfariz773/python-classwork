class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        return f"VehicleID: {self._vehicle_id}, Base Rate: {self._base_rate}"

    def rental_charge(self):
        return 0.0


class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self.num_seats


class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5

def calculate_rental(vehicle: Vehicle):
    return vehicle.rental_charge()

AMG = Car("car001",100.00,4)
Himalaya = Bike("BIKE001",80.00,"Supermotto")

print(AMG.display_details())  
print("Car Rental Charge:", calculate_rental(AMG))  

print(Himalaya.display_details()) 
print("Bike Rental Charge:", calculate_rental(Himalaya))
    
