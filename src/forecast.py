from bs4 import BeautifulSoup as Soup
import urllib3
import yaml

class Forecast(object):
    base_url = 'https://forecast.weather.gov/MapClick.php?w0=t&w1=td&w2=hi&w3=sfcwind&w3u=1&w4=sky&w5=pop&w6=rh&w7=rain&w8=thunder&w9=fog&w10=mhgt&w10u=0&w11=lal&w12=twind&w12u=1&w13=ft20w&w13u=1&w14=rfti&w15=cig&w16=vsby&AheadHour=0&Submit=Submit&FcstType=graphical&textField1={latitude}&textField2={longitude}&site=all&unit=0&dd=&bw='
    latitude = 0
    longitude = 0
    
    def __init__(self, *args, **kwargs):
        for kw in kwargs:
            print('{}: {}'.format(kw, kwargs[kw]))
        if 'latitude' in kwargs and 'longitude' in kwargs:
            self.latitude = kwargs['latitude']
            self.longitude = kwargs['longitude']
        elif 'location' in kwargs:
            self.latitude = kwargs['location'][0]
            self.longitude = kwargs['location'][1]
        
        self.url = self.base_url.format(latitude=self.latitude, longitude=self.longitude)
        print(self.url)
        
        self.get_soup()
        print(self.soup)
        
    def get_soup(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
        response = urllib3.PoolManager().request('GET', self.url, headers=headers)
        self.soup = Soup(response.data, 'html.parser')


if __name__ == '__main__':
    # Allow rudimentary testing in PyDroid3
    loc = (29.5882, -95.0260)
    fc = Forecast(kilo='whiskey', location=loc)
