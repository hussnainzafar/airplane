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
    def time_to_reached(self):
        '''this function calculate time using distance and speed
        then store them into object variable time'''
        self.time= self.distance/self.speed
    def set_color(self,color):
        ''' This function is used to set the color'''
        self.color=color
    def set_engine(self, engine):
        ''' This function is used to set the engine'''
        # self.engine=engine

    def set_door(self, door):
        self.door=door
    def set_speed(self, speed):
        self.speed=speed




obj = Airplane("white",400,1200,2,8000) #Create the object of plane and initiallizing it
obj.time_to_reached() 
obj.show_time() #This is used to show or output time
