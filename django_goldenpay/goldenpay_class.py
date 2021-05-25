import requests, hashlib
import json as json_pack

import xmltodict

from django.conf import settings


class PaymentGatewayGoldenpay:
    urlGetPaymentKey = settings.GOLDENPAY_URL_PAYMENT_KEY
    urlGetPaymentResult = settings.GOLDENPAY_PAYMENT_RESULT
    urlRedirect = settings.GOLDENPAY_URL_REDIRECT

    merchantName = settings.GOLDENPAY_MERCHANT_NAME
    authKey = settings.GOLDENPAY_AUTH_KEY

    def getPaymentKeyJSONRequest(self, amount, lang, cardType, description):

        params = {
            'merchantName': self.merchantName,
            'cardType': cardType,
            'amount': amount,
            'description': description
        }

        params['hashCode'] = self.getHashcCode(params)

        params['lang'] = lang

        json_result = json_pack.loads(self.getJsonContent(self.urlGetPaymentKey, params))

        json_result['urlRedirect'] = "{}{}".format(self.urlRedirect, json_result['paymentKeyResult']['paymentKey'])

        return json_result

    def getPaymentResult(self, payment_key):
        params = {
            'payment_key': payment_key
        }
        params['hash_code'] = self.getHashcCode(params)

        json_result = self.file_get_contents("{}{}".format(
            self.urlGetPaymentResult, self.params_url_encode(params)
        ))

        return json_pack.loads(json_result)

    def getHashcCode(self, params):
        result_val = "{}{}".format(self.authKey, self.implode(params))
        return hashlib.md5(result_val.encode()).hexdigest()

    def params_url_encode(self, item):
        encode_url = ""
        for key, value in item.items():
            encode_url += str(key) + "=" + str(value) + "&"
        encode_url = "?%s" % encode_url[:-1]
        return encode_url

    def getJsonContent(self, url, content):

        r = requests.post(url=url,json=content)

        o = xmltodict.parse(r.text)

        return json_pack.dumps(o)


    def file_get_contents(self,url):
        return requests.get(url=url)

    def implode(self,dict_val):
        return_val = ''.join(map(str, dict_val.values()))
        return return_val