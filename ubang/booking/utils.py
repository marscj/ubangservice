from datetime import date, datetime, timedelta

from ubang.order import OrderStatus
from ubang.order.models import Order

def get_days(start, end):
    duration = date(end.year, end.month, end.day) + timedelta(days=1) - date(start.year, start.month, start.day)
    return [date(start.year, start.month, start.day) + timedelta(days=index) for index in range(duration.days) ]

def createOrder(booking):
    if booking.guide:
        order = Order.objects.create(
            customer=booking.create_by.username, 
            company=booking.company_by.name, 
            start_time=booking.start_time, 
            end_time=booking.end_time,
            vehicle=booking.vehicle.traffic_plate_no,
            guide=booking.guide.username,
            discount=booking.create_by.company.discount,
            booking=booking
        )
    else:
        order = Order.objects.create(
            customer=booking.create_by.username, 
            company=booking.company_by.name, 
            start_time=booking.start_time, 
            end_time=booking.end_time,
            vehicle=booking.vehicle.traffic_plate_no,
            discount=booking.create_by.company.discount,
            booking=booking
        )

def bookingCancel(booking):
    for order in booking.order.all():
        order.status = OrderStatus.Cancel
        order.save()
