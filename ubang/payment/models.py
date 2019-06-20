from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import MaxValueValidator, MinValueValidator

from djmoney.models.fields import MoneyField
from djmoney.money import Money
from decimal import Decimal
import uuid

from .import (ChargeStatus, Currency)
from ubang.order.models import Order

# 付款
class Payment(models.Model):

    # 支付网关 支付类型
    # gateway = models.CharField(max_length=255)
    
    # 是否有效
    is_active = models.BooleanField(default=True)

    # 支付状态
    charge_status = models.CharField(
        max_length=20, choices=ChargeStatus.CHOICES,
        default=ChargeStatus.NOT_CHARGED)

    # token
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # 支付金额
    total = models.DecimalField(
        max_digits=settings.DEFAULT_MAX_DIGITS,
        decimal_places=settings.DEFAULT_DECIMAL_PLACES,
        default=Decimal("0.0"),
    )

    # 收到金额
    captured_amount = models.DecimalField(
        max_digits=settings.DEFAULT_MAX_DIGITS,
        decimal_places=settings.DEFAULT_DECIMAL_PLACES,
        default=Decimal("0.0"),
    )

    # 货币
    currency = models.CharField(max_length=10, choices=Currency.CHOICES, default=Currency.AED)

    # 额外
    # extra_data = models.TextField(blank=True, default='')

    remark = models.TextField(blank=True, null=True)

    # 订单
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')

    class Meta:
        ordering = ('pk', )

    # def get_last_transaction(self):
    #     return max(self.transactions.all(), default=None, key=attrgetter('pk'))

    # def get_total(self):
    #     return Money(self.total, self.currency or settings.DEFAULT_CURRENCY)

    # def get_authorized_amount(self):
    #     money = zero_money()

    #     transactions = self.transactions.all()

    #     if any([txn.kind == TransactionKind.CAPTURE
    #             and txn.is_success for txn in transactions]):
    #         return money

    #     authorized_txns = [
    #         txn for txn in transactions
    #         if txn.kind == TransactionKind.AUTH and txn.is_success]

    #     for txn in authorized_txns:
    #         money += Money(
    #             txn.amount, self.currency or settings.DEFAULT_CURRENCY)

    #     return money

    # def get_captured_amount(self):
    #     return Money(
    #         self.captured_amount, self.currency or settings.DEFAULT_CURRENCY)

    # def get_charge_amount(self):
    #     return self.total - self.captured_amount

    # @property
    # def is_authorized(self):
    #     return any([
    #         txn.kind == TransactionKind.AUTH
    #         and txn.is_success for txn in self.transactions.all()])

    # @property
    # def not_charged(self):
    #     return self.charge_status == ChargeStatus.NOT_CHARGED

    # def can_authorize(self):
    #     return self.is_active and self.not_charged

    # def can_capture(self):
    #     return self.is_active and self.not_charged and self.is_authorized

    # def can_charge(self):
    #     not_fully_charged = (
    #         self.charge_status == ChargeStatus.PARTIALLY_CHARGED)
    #     return self.is_active and (self.not_charged or not_fully_charged)

    # def can_void(self):
    #     return self.is_active and self.not_charged and self.is_authorized

    # def can_refund(self):
    #     can_refund_charge_status = (
    #         ChargeStatus.PARTIALLY_CHARGED,
    #         ChargeStatus.FULLY_CHARGED,
    #         ChargeStatus.PARTIALLY_REFUNDED)
    #     return (
    #         self.is_active and self.charge_status in can_refund_charge_status
    #         and self.gateway != CustomPaymentChoices.MANUAL)
