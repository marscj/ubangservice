
class CarCategory:
    Mini = 0
    Economy = 1
    Standerd = 2
    Luxury = 3
    SUV = 4
    Seat_7 = 5
    Permium = 6

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
    Luxury_Coachs = 7
    Mini_Coaches = 8
    Mini_Vans = 9

    CHOICES = [
        (Luxury_Coachs, 'Luxury Coachs Bus'),
        (Mini_Coaches, 'Mini Coaches Bus'),
        (Mini_Vans, 'Mini Vans Bus'),
    ]

class VehicleCategory:
    CHOICES = CarCategory.CHOICES + BusCategory.CHOICES

class VehicleType:
    Car = 0
    Bus = 1

    CHOICES = [
        (Car, 'Car'),
        (Bus, 'Bus'),
    ]

class PriceType:
    Cost = 0
    Gross = 1

    CHOICES = [
        (Cost, 'Cost price'),
        (Gross, 'Gross price ')
    ]