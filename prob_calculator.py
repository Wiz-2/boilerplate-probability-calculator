import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for k,v in kwargs.items():
            while(v!=0):
                self.contents.append(k)
                v-=1
        self.value= copy.deepcopy(self.contents)
    def draw(self,num_of_balls_to_be_drawn):
        if(num_of_balls_to_be_drawn>len(self.value)):
            sample_list=self.value
        else:
            sample_list=random.sample(self.value,
            num_of_balls_to_be_drawn)
            self.contents=[]
            for i in range(0,len(self.value)-num_of_balls_to_be_drawn):
                self.contents.append(i)
        return sample_list
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M=0
    for i in range(0,num_experiments):
        list_drawn=hat.draw(num_balls_drawn)
        matched=0
        no_of_times=0
        for k,v in expected_balls.items():
            count=0
            no_of_times+=1
            for j in list_drawn:
                if(j==k and count<v):
                    count+=1
                if(count==v):
                    matched+=1
                    break
        if(no_of_times==matched):
            M+=1
    return (M/num_experiments)

            




