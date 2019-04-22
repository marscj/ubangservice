from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.core.validators import MaxValueValidator, MinValueValidator

from djmoney.models.fields import MoneyField

from .import (ChargeStatus, CustomPaymentChoices, TransactionError, TransactionKind)
from ubang.order.models import Order

# 付款
class Payment(models.Model):

    # 支付网关 支付类型
    gateway = models.CharField(max_length=255)
    
    # 是否有效
    is_active = models.BooleanField(default=True)

    # 创建时间
    create_at = models.DateTimeField(auto_now_add=True)

    # 修改时间
    last_change = models.DateTimeField(auto_now=True)

    # 支付状态
    charge_status = models.CharField(
        max_length=20, choices=ChargeStatus.CHOICES,
        default=ChargeStatus.NOT_CHARGED)

    # token
    token = models.CharField(max_length=128, blank=True, default='')

    # 支付金额
    total = MoneyField(max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])

    # 收到金额
    captured_amount = MoneyField(max_digits=settings.DEFAULT_MAX_DIGITS, decimal_places=settings.DEFAULT_DECIMAL_PLACES, validators=[MinValueValidator(0.0)])

    # 货币
    currency = models.CharField(max_length=10)

    # 支付ip
    customer_ip_address = models.GenericIPAddressField(blank=True, null=True)

    # 额外
    extra_data = models.TextField(blank=True, default='')

    # 订单
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')

    class Meta:
        ordering = ('pk', )

    def __repr__(self):
        return 'Payment(gateway=%s, is_active=%s, create_at=%s, charge_status=%s)' % (
            self.gateway, self.is_active, self.create_at, self.charge_status)

    def get_last_transaction(self):
        return max(self.transactions.all(), default=None, key=attrgetter('pk'))

    def get_total(self):
        return Money(self.total, self.currency or settings.DEFAULT_CURRENCY)

    def get_authorized_amount(self):
        money = zero_money()

        transactions = self.transactions.all()

        if any([txn.kind == TransactionKind.CAPTURE
                and txn.is_success for txn in transactions]):
            return money

        authorized_txns = [
            txn for txn in transactions
            if txn.kind == TransactionKind.AUTH and txn.is_success]

        for txn in authorized_txns:
            money += Money(
                txn.amount, self.currency or settings.DEFAULT_CURRENCY)

        return money

    def get_captured_amount(self):
        return Money(
            self.captured_amount, self.currency or settings.DEFAULT_CURRENCY)

    def get_charge_amount(self):
        return self.total - self.captured_amount

    @property
    def is_authorized(self):
        return any([
            txn.kind == TransactionKind.AUTH
            and txn.is_success for txn in self.transactions.all()])

    @property
    def not_charged(self):
        return self.charge_status == ChargeStatus.NOT_CHARGED

    def can_authorize(self):
        return self.is_active and self.not_charged

    def can_capture(self):
        return self.is_active and self.not_charged and self.is_authorized

    def can_charge(self):
        not_fully_charged = (
            self.charge_status == ChargeStatus.PARTIALLY_CHARGED)
        return self.is_active and (self.not_charged or not_fully_charged)

    def can_void(self):
        return self.is_active and self.not_charged and self.is_authorized

    def can_refund(self):
        can_refund_charge_status = (
            ChargeStatus.PARTIALLY_CHARGED,
            ChargeStatus.FULLY_CHARGED,
            ChargeStatus.PARTIALLY_REFUNDED)
        return (
            self.is_active and self.charge_status in can_refund_charge_status
            and self.gateway != CustomPaymentChoices.MANUAL)

# # 交易
# class Transaction(models.Model):

#     # 创建时间
#     create_at = models.DateTimeField(auto_now_add=True, editable=False)

#     # 支付
#     payment = models.ForeignKey(Payment, related_name='transactions', on_delete=models.PROTECT)

#     # token
#     token = models.CharField(max_length=128, blank=True, default='')
    
#     # 种类
#     kind = models.CharField(max_length=10, choices=TransactionKind.CHOICES)

#     # 交易是否成功
#     is_success = models.BooleanField(default=False)

#     # 货币
#     currency = models.CharField(max_length=10)

#     # 金额
#     amount = models.DecimalField(
#         max_digits=settings.DEFAULT_MAX_DIGITS,
#         decimal_places=settings.DEFAULT_DECIMAL_PLACES,
#         default=Decimal('0.0'))

#     # 错误信息
#     error = models.CharField(
#         choices=[(tag, tag.value) for tag in TransactionError],
#         max_length=256, null=True)

#     # 入口信息
#     gateway_response = JSONField(encoder=DjangoJSONEncoder)

#     class Meta:
#         ordering = ('pk', )

#     def __repr__(self):
#         return 'Transaction(type=%s, is_success=%s, created=%s)' % (
#             self.kind, self.is_success, self.created)

#     def get_amount(self):
#         return Money(self.amount, self.currency or settings.DEFAULT_CURRENCY)
