class settings:    '''    支付基础配置信息    '''    app_id="2016080800192107"    method="alipay.trade.page.pay"    gateway="https://openapi.alipaydev.com/gateway.do?"    format="json"    charset="utf-8"    sign_type="RSA2"    version="1.0"    notify_url=""    __prikey_file="alipay/prikey.txt"    prikey=open(__prikey_file,"rb").read()class alipayData():    '''    支付宝基础信息    '''    public_key='''MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy5rvamC9iEYGirbUzP/QxDISoboiftsnNUiHSC3b4QTm4UBjxMgEBW1f02wlD4CEYpW8ZYksxBl00nzSSE8viLNi9k2y+NtqEW41qMlJoaOdbqkrGxZjsiDYPAz24oYjHFAughHDT2dHLz0mkHJcHZ2JiMEEvXvhHSpGcRBkzGVsPZabzXIh0qWvN63xXomXyUMIONJczZ0cd1+Kz5i77mW0cQIE+2EKoLhUM/Z2Zd/sgeIEPkw8+c+h75gmUULYAPwYjSZF50+8Vjuq/wRiqdmxbxt1oLRdaPiRWmp4fe4gEJ22D+3/vmRFoqRFdJPPq7DnECNmgl7UIyOQu4u+3QIDAQAB'''