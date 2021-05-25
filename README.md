# goldenpay django

Developed by Atakhan Rahimli (c) 2021

## Examples of How To Use the package

Creating A Server

```python
from django_goldenpay import PaymentGatewayGoldenpay

# Choose One
paymentGatewayGoldenpay = PaymentGatewayGoldenpay()

#result = paymentGatewayGoldenpay.getPaymentKeyJSONRequest(amount, 'Lang code', 'card type', 'Your description here') 
result = paymentGatewayGoldenpay.getPaymentKeyJSONRequest(2600, 'lv', 'v', 'description here')

status_code = result['paymentKeyResult']['status']['code'],
status_message = result['paymentKeyResult']['status']['message'],
paymentKey = result['paymentKeyResult']['paymentKey'],
urlRedirect = result['urlRedirect'],
```

https://github.com/arahimli/django_goldenpay.git