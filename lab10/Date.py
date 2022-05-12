'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    
    def __init__(self, y, m, d): 
        self.year = y
        if self.year == '':
            y = '1900'
        self.month = m
        if self.month == '':
            m = '1'
        self.day = d
        if self.day == '':
            d = '1'
        
    def __str__(self): 
        year = str(self.year) 
        month = str(self.month)
        day = str(self.day)
        s = ''
        s = year + '/' + month + '/' + day
        return s
        
    def same_day_in_year(self, other): 
        if self.month == other.month: 
            return True
        else:
            return False 
        
    def is_leap_year(self):
        if (self.year % 4 == 0) and (self.year % 100 != 0) and self.year %400 != 0: 
            return True
        else:
            return False
        
    def __lt__(self, other):
        if self.year < other.year:        
            return True 
        elif self.year == other.year and self.month < other.month: 
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        else:
            return False
             
if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    d4 = Date(1998, 4, 11)
    print("d1: " + str(d1))
    print("d2: " + str(d2))   
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()
    print('d1.is_leap_year()', d1.is_leap_year()) 
    print('d2.is_leap_year()', d2.is_leap_year())
    print() 
    print('d1 < d2', d1.__lt__(d2))
    print('d2 < d3', d2.__lt__(d3))
    print('d3 < d4', d3.__lt__(d4))
    print('d2 < d4', d2.__lt__(d4))