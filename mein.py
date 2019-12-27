#coding=utf8
class Driver:
    def __init__(self,coordinate):
        self.distanceToArea = 0
        self.coordinate = coordinate.split(' ')
        self.coordinateX = int(coordinate[0])
        self.coordinateY = int(coordinate[1])

        self.distance_N = self.coordinateX - DIMENSION_N
        if((self.distance_N) <= 0):
            self.distance_N = 0

        self.distance_M = self.coordinateY - DIMENSION_M
        if((self.distance_M) <= 0):
            self.distance_M = 0

        self.distanceToArea = self.distance_N + self.distance_N     

DIMENSION_N = 0
DIMENSION_M = 0

area_demandX0 = 0
area_demandY0 = 0
area_demandX1 = 0
area_demandY1 = 0

K = 0
D = 0

coordinateDrivers = []
claimingDrivers = []

#обработать исключения ввода размерности матрицы 
DIMENSION = raw_input().split(' ')
DIMENSION_N = int(DIMENSION[0])
DIMENSION_M = int(DIMENSION[1])

print DIMENSION_N
print DIMENSION_M

#обработать исключения ввода зоны повышенного спроса
area_demand = raw_input().split(' ')
area_demandX0 = area_demand[0]
area_demandY0 = area_demand[1]
area_demandX1 = area_demand[2]
area_demandY1 = area_demand[3]

#обработать исключения ввода параметров коэффициента
paramS = raw_input().split(' ')
K = int(paramS[0])
D = int(paramS[1])

#обработать исключения ввода притендующих водителей
coordinate = raw_input().split(' ')

for i in range(len(coordinate)/2):
    coordinateDrivers.append(coordinate[i*2] + ' ' + coordinate[(i*2) + 1])
    print coordinateDrivers[i]

for i in range(len(coordinateDrivers)):
    claimingDrivers.append(Driver(coordinateDrivers[i]))

print claimingDrivers[1].distanceToArea

DForRepayment = 0
#обработать исключение коэффициента не требующего работы
DForRepayment = K - D

