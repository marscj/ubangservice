
class CarCategory:
    Mini = 'Mini Car'
    Economy = 'Economy Car'
    Standerd = 'Standerd Car'
    Luxury = 'Luxury Car'
    SUV = 'SUV Car'
    Seat_7 = '7 Seat Car'
    Permium = 'Permium Car'

    CHOICES = [
        (Mini, 'Mini Car'),
        (Economy, 'Economy Car'),
        (Standerd, 'Standerd Car'),
        (Luxury, 'Luxury Car'),
        (SUV, 'SUV Car'),
        (Seat_7, '7 Seat Car'),
        (Permium, 'Permium Car'),
    ]

class BusCategory:
    Luxury_Coachs = 'Luxury Coachs Bus'
    Mini_Coaches = 'Mini Coaches Bus'
    Mini_Vans = 'Mini Vans Bus'

    CHOICES = [
        (Luxury_Coachs, 'Luxury Coachs Bus'),
        (Mini_Coaches, 'Mini Coaches Bus'),
        (Mini_Vans, 'Mini Vans Bus'),
    ]

class VehicleCategory:
    CHOICES = CarCategory.CHOICES + BusCategory.CHOICES

class VehicleType:
    Car = 'Car'
    Bus = 'Bus'

    CHOICES = [
        (Car, 'Car'),
        (Bus, 'Bus'),
    ]