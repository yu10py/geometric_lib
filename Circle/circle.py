import math


def area(r):
    ''' 
    Возвращает площадь круга с радиусом r
	
	Параметры: 
	    r (float): радиус круга

	Возращаемое значение:
	    math.pi * r * r (float): площадь круга
    
    '''
    if (r >= 0):
        return math.pi * r * r
    else:
        raise ValueError



def perimeter(r):
    '''
    Возвращает периметр окружности радиуса r

        Параметры:
            r (float): радиус круга

        Возвращаемое значение:
            2 * math.pi * r  (float): периметр круга

    '''
    if (r >= 0):
        return 2 * math.pi * r
    else:
        raise ValueError

