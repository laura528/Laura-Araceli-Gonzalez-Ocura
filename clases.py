class Estado(): 
    def __init__(self, estado, confirmados, negativos, sospechosos, recuperados, fallecidos, activos):
        self.estado = estado
        self.confirmados = confirmados
        self.negativos = negativos 
        self.sospechosos = sospechosos 
        self.recuperados = recuperados
        self.fallecidos = fallecidos
        self.activos = activos
       
    def presentar(self):
        presentacion = ("{}: confirmados {}, negativos {}, sospechosos {}, recuperados {}, fallecidos {}, activos {}") 
        print(presentacion.format(self.estado, self.confirmados, self.negativos, self.sospechosos, self.recuperados, self.fallecidos, self.activos))
        print(' ')
        
coahuila = Estado('COAHUILA',26389, 35574, 3504, 21371, 1880, 1042)
chihuahua = Estado('CHIHUAHUA',11123, 10531, 3619, 7443,1389, 330)
colima = Estado('COLIMA', 4870, 3385, 252, 3224, 531, 307)
durango = Estado('DURANGO', 8947, 15184, 1592, 6948, 632, 598)
cdmx = Estado('CDMX', 126371, 212710, 20498, 99500, 9667, 4569)

coahuila.presentar() 
chihuahua.presentar()
colima.presentar()
durango.presentar()
cdmx.presentar()
