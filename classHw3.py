import datetime


class WebPush:
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print(self.push_type + " Push gönderildi")

    def push_bilgileri(self):
        return self.platform, self.optin, self.global_frequency_capping, self.start_date, self.end_date, self.language, \
               self.push_type


class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, send_date):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type, price_info,
                 discount_rate):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self):
        discount_price = self.price_info * self.discount_rate

        return discount_price


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.stock_info = stock_info

    def stockUptade(self):
        self.stock_info = not self.stock_info

        return self.stock_info


TriggerPushType = TriggerPush("Desktop", True, 15, datetime.datetime(2022, 1, 1).strftime("%m/%d/%Y"),
                              datetime.datetime(2022, 2, 1).strftime("%m/%d/%Y"), "tr_TR", "Trigger", "HomePage")
TriggerPushType.send_push()
print(TriggerPushType.push_bilgileri())

BulkPushType = BulkPush("Desktop", True, 15, datetime.datetime(2022, 1, 1), datetime.datetime(2022, 2, 1), "tr_TR",
                        "Bulk", 10)
BulkPushType.send_push()

SegmentPushType = SegmentPush("Desktop", True, 15, datetime.datetime(2022, 1, 1), datetime.datetime(2022, 2, 1),
                              "tr_TR", "Segment", "DiscountBuyers")
SegmentPushType.send_push()

PriceAlertPushType = PriceAlertPush("Desktop", True, 15, datetime.datetime(2022, 1, 1), datetime.datetime(2022, 2, 1),
                                    "tr_TR", "PriceAlert", 100, 0.2)
PriceAlertPushType.send_push()
print("{} TL İNDİRİMİ KAÇIRMAYIN!".format(PriceAlertPushType.discountPrice()))

InstockPushType = InstockPush("Desktop", True, 15, datetime.datetime(2022, 1, 1), datetime.datetime(2022, 2, 1),
                              "tr_TR", "InstockPush", False)
InstockPushType.send_push()
print("Stok durumu:{} ".format(InstockPushType.stockUptade()))
