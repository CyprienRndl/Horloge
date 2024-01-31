import time


class univers:
    """
    Univers
    """
    def __init__(self, Time, Min, Hour, Day,Year):
        self.time = Time
        self.Min = Min
        self.Hour = Hour
        self.day = Day
        self.year = Year
    
    def Time(self):
        while True:
            time.sleep(1)
            self.time = self.time + 1
            
            if self.time == 60:
                self.Min = self.Min + 1
                self.time = 0
                
                if self.Min == 60:
                    self.Hour = self.Hour + 1
                    self.Min = 0
                    
                    if self.Hour >= 24:
                        self.day = self.day + 1
                        self.Hour = 0
                        
                        if self.day >= 365:
                            self.year = self.year + 1
                            self.day = 0
                        
                        else:
                            print(self.year,'Années',self.day,'Jours',self.Hour,"Heures",self.Min,'Minutes',self.time,'Secondes')
                    
                    else:
                        print(self.year,'Années',self.day,'Jours',self.Hour,"Heures",self.Min,'Minutes',self.time,'Secondes')
                
                else:
                    print(self.year,'Années',self.day,'Jours',self.Hour,"Heures",self.Min,'Minutes',self.time,'Secondes')

            else:
                print(self.year,'Années',self.day,'Jours',self.Hour,"Heures",self.Min,'Minutes',self.time,'Secondes')


                    

temps = univers(0,0,0,0,0)

temps.Time()