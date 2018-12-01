#class
class Orang:
    pass

org = Orang()
print(org)

#method
class Orang:
    def katakanHalo (self):
        print 'Halo, apa kabar ?'
org = Orang()
org.katakanHalo()

#method init 
class Orang:
    def __init__(self, name):
        self.name = name
    def katakanHalo(self):  
        print ('Hai, my name is {}'.format(self.name))
  
org = Orang('budi')
org.katakanHalo()

var class and object
class Orang:
    total = 0 
    def __init__(self,name):
        self.name = name
        Orang.total += 1

    def __del__(self):
        Orang.total -= 1

    def katakanHalo(self):
        print ('Hai, name my is {}'.format(self.name)) 

    def total_populasi (yas):
        print ('Total populasi orang {}'.format(yas.total)) 

    #method class 
    total_populasi = classmethod(total_populasi) 

org = Orang('budi')
org.katakanHalo()
Orang.total_populasi()    

org2 = Orang('andi')
org.katakanHalo()
Orang.total_populasi()

print ('objek dihapus')
del org

Orang.total_populasi()

#inherintance
#base class
class AnggotaSekolah:
    def __init__(self,name, age):
        self.name = name
        self.age = age

        print('create new member {}'.format(self.name))

    def info(self):
        print('Name: {}, Age: {}'.format(self.name, self.age))
    
#subclass 
class Guru(AnggotaSekolah):
    def __init__(self, name, age,salary):
        AnggotaSekolah.__init__(self, name, age)
        self.salary = salary
        print('create new teacher {}'.format(self.name))

    def info(self):
        AnggotaSekolah.info(self)
        print('Salary: {}'.format(self.salary))

#subclass
class Siswa(AnggotaSekolah):
    "representasi siswa"
    def __init__(self, name, age, score):
        AnggotaSekolah.__init__(self, name, age)
        self.score = score

        print ('membuat create student : {}'.format(self.name))

    def info(self):
        AnggotaSekolah.info(self)
        print ('Score: {}'.format(self.score))



guru = Guru('Budi', 40, 3000000)
siswa = Siswa('Andi', 25, 75)

print

anggota = [guru, siswa]

for orang in anggota:
    orang.info()
