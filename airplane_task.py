class Airplane():
    def __init__(self,color,engine,speed,door,distance):
        self.color = color     #Storing color to object attribute color
        self.engine = engine    #Storing engine to object attribute engine
        self.speed = speed      #Storing speed to object attribute speed
        self.door = door        #storing door to attribute door
        self.distance = distance    #Storing distance to attribute distance
        self.time = 0           #to Store time
    def show_time(self):
        '''This function is used to calculate time and show the output'''
        print("hours: ",self.time)

    def get_color(self):
        '''This function is used to return color'''
        return self.color
    def get_engine(self):
        '''This function is used to return engine'''
        return self.engine
    def get_speed(self):
        '''This function is used to return speed'''
        return self.speed
    def get_door(self):
        '''This function is used to return door'''
        return self.door
    def get_distance(self):
        '''This function is used to return distance'''
        return self.distance
    def get_time(self):
        '''This function is used to return time'''
        return self.time


obj = Airplane("white",400,1200,2,8000) #Create the object of plane and initiallizing it
obj.show_time() #This is used to show or output time