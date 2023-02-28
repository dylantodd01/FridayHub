#use this for calling in the finance API

from yahoo_fin.stock_info import get_data

class Data(get_data.myData):
    amazon_weekly= get_data("amzn", start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")

    class Meta:
        verbose_name = 'Amazon'

    def __str__(self):
        return self.amazon_weekly
    
