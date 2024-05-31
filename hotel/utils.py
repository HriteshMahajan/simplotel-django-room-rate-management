# hotel/utils.py

from .models import OverriddenRoomRate, DiscountRoomRate


def calculate_final_rate(room_rate, stay_date):
    overridden_rate = OverriddenRoomRate.objects.filter(room_rate=room_rate, stay_date=stay_date).first()
    rate = overridden_rate.overridden_rate if overridden_rate else room_rate.default_rate

    discounts = DiscountRoomRate.objects.filter(room_rate=room_rate)
    max_discount = max(discounts, key=lambda d: d.discount.discount_value) if discounts else None

    if max_discount:
        if max_discount.discount.discount_type == 'fixed':
            rate -= max_discount.discount.discount_value
        elif max_discount.discount.discount_type == 'percentage':
            rate -= rate * (max_discount.discount.discount_value / 100)

    return rate
