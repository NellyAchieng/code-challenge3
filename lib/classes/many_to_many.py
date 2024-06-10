
class Band:
    # def _init_(self, name, hometown):
    #     self.name = name
    #     self.hometown = hometown
    #     self._concerts = []

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, value):
    #     if isinstance(value, str) and len(value) > 0:
    #         self._name = value
    #     else:
    #         raise Exception("Name must be a non-empty string")

    # @property
    # def hometown(self):
    #     return self._hometown

    # @hometown.setter
    # def hometown(self, value):
    #     if hasattr(self, '_hometown'):
    #         raise Exception("Hometown cannot be changed")
    #     if isinstance(value, str) and len(value) > 0:
    #         self._hometown = value
    #     else:
    #         raise Exception("Hometown must be a non-empty string")

    # @property
    # def concerts(self):
    #     return self._concerts if self._concerts else None

    # @property
    # def venues(self):
    #     if not self._concerts:
    #         return None
    #     return list({concert.venue for concert in self._concerts})

    # def play_in_venue(self, venue, date):
    #     concert = Concert(date, self, venue)
    #     self._concerts.append(concert)
    #     venue.add_concert(concert)
    #     return concert

    # def all_introductions(self):
    #     if not self._concerts:
    #         return None
    #     return [concert.introduction() for concert in self._concerts]

    # def add_concert(self, concert):
    #     if isinstance(concert, Concert) and concert not in self._concerts:
    #         self._concerts.append(concert)
    all =[]
    def __init__(self, name, hometown):
        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("Hometown must be a non-empty string")
        self.name = name
        Band.all.append(self) 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError("Name must be non-empty string")
    @property
    def hometown(self):
        return self._hometown 

    def concerts(self):
        concerts = [concert for concert in Concert.all if concert.band == self]
        return concerts if concerts else None

    def venues(self):
        venues = list(set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")

class Concert:
    # all = []

    # def _init_(self, date, band, venue):
    #     self.date = date
    #     self.band = band
    #     self.venue = venue
    #     band.add_concert(self)
    #     venue.add_concert(self)
    #     if self not in Concert.all:
    #         Concert.all.append(self)

    # @property
    # def date(self):
    #     return self._date

    # @date.setter
    # def date(self, value):
    #     if isinstance(value, str) and len(value) > 0:
    #         self._date = value
    #     else:
    #         raise Exception("Date must be a non-empty string")

    # @property
    # def band(self):
    #     return self._band

    # @band.setter
    # def band(self, value):
    #     if isinstance(value, Band):
    #         self._band = value
    #     else:
    #         raise Exception("Band must be of type Band")

    # @property
    # def venue(self):
    #     return self._venue

    # @venue.setter
    # def venue(self, value):
    #     if isinstance(value, Venue):
    #         self._venue = value
    #     else:
    #         raise Exception("Venue must be of type Venue")

    # def hometown_show(self):
    #     return self.band.hometown == self.venue.city

    # def introduction(self):
    #     return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
    all = []
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date):
            self._date = date
        else:
            raise ValueError("Date must be non-empty string")
    @property
    def band(self):
        return self._band
    @band.setter
    def band(self, band):
        if not isinstance(band, Band):
            raise TypeError("Band must be of type Band")
        self._band = band

    @property
    def venue(self):
        return self._venue
    @venue.setter
    def venue(self, venue):
        if not isinstance(venue, Venue):
            raise ValueError("Venue must be of type Venue")
        self._venue = venue
    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all = []
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be non-empty string")
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, city):
        if isinstance(city, str) and len(city):
            self._city = city
        else:
            raise ValueError("City must be non_empty string")
    def concerts(self):
        result =[concert for concert in Concert.all if concert.venue == self]
        return result if result else None
    def bands(self):
        result = list(set(concert.band for concert in self.concerts()))
        return result if result else None
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None