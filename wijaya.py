#class 
#konsep merupakan abtraksi atau blueprint yang mendefinisikan suatu object
class Car:
    color = 'black'
    transmission = 'manual'

    def __init__(self, transmission):
        self.transmission = transmission
        print('engine is ready')

    def drive(self):
        print('Drive')
    
    def reverse(self):
        print('reverse, Please check your behind.')

#method
#behaviour, punya beberapa parameter
    gear_position = 'N'
    def change_gear(self, gear='N'):
        self.gear_position = gear
        print('Gear position on: {}'.format(self.gear_position))

    def get_gear_position(self):
        return self.gear_position


#self mengacu pada class instance untuk mengakses atribute
 
 #inheritance & overriding
class Tesla(Car):

    def drive(self):
        print('LOL gas')

# ferrari = Car('auto')
# ferrari.change_gear()
# ferrari.get_gear_position()

tesla = Tesla('oke')   
tesla.drive()

