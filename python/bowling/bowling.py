from enum import Enum


class State(Enum):
    INVALID=0
    OPEN=1
    SPARE=2
    STRIKE=3
    FILL=4
    
class BowlingGame:
    def __init__(self):
        self.counter=0
        self.frame=0
        self.points=[0,0,0,0,0,0,0,0,0,0]
        self.total_frame=10
        self.remain_pin=10
        self.prev_flag=[State.INVALID,State.INVALID ]
        

    def roll(self, pins):
        #first verdict whether it's round, cnt, remaining bowling
        #check is it valid to roll ball(end or not?)
        if pins<0: 
            raise ValueError("boling game already End!")
        if self.frame==9 and self.counter>2:
            raise ValueError("boling game already End!")
        if self.frame==9 and self.prev_flag[1]!=State.FILL and self.counter>1:#second round should be new state,
            raise IndexError("cannot throw bonus with an open frame")
        #and then check whether pins match remain_pin
        if pins > self.remain_pin:
            raise ValueError("hit pin > remain pin")
        #get hit then count!
        # frame 1-9 | frame 10 , counter 1, 2,3, 
        if self.counter==0:
            #first attempt in the round
            #point add first
            if self.prev_flag[1]==State.SPARE or self.prev_flag[1]==State.STRIKE:
                self.points[self.frame-1]+=pins
            if self.prev_flag[0] == State.STRIKE and self.prev_flag[1]== State.STRIKE:
                self.points[self.frame-2]+=pins
            self.points[self.frame] += pins
            self.prev_flag[0] = self.prev_flag[1]
            self.prev_flag[1] = State.INVALID
            if pins==10:
                if self.frame<9:
                    self.frame +=1
                    self.prev_flag[1] = State.STRIKE
                else:
                    self.prev_flag[1] = State.FILL
                    self.counter+=1
                return
            else:
                self.remain_pin-=pins
                self.counter +=1
                return
        if self.counter ==1:
            if self.prev_flag[0] == State.STRIKE:
                self.points[self.frame-1] += pins
            self.points[self.frame] += pins
            #need to verdict whether is the tenth rounds or not?
            #only concern if previous round doesnot kill all pin 
            if self.remain_pin-pins==0 :
                if self.frame<9:
                    self.prev_flag[1] = State.SPARE
                    self.frame +=1
                    self.counter=0
                    self.remain_pin=10
                else:
                    if self.prev_flag[1]==State.INVALID:
                        self.prev_flag[1] = State.FILL
                    self.counter+=1
                    self.remain_pin=10
            else:
                if self.frame<9:
                    self.prev_flag[1]=State.OPEN
                    self.frame+=1
                    self.counter=0
                    self.remain_pin=10
                    return
                else:
                    self.remain_pin-=pins
                    self.counter+=1
            return 
        if self.counter==2:
            self.points[self.frame] += pins
            self.counter+=1
            
            
    def print(self):
        print(f'current frame: {self.frame}, counter: {self.counter}')
        print(f'-1 flag: {self.prev_flag[1]}, -2 flag: {self.prev_flag[0]}')
        print(f'remain pin: {self.remain_pin}')
        print(f'current points: {self.points}')   
        

    def score(self):
        if self.frame<9:
            raise ValueError("invalid")
        else:
            if self.prev_flag[1]==State.FILL:
                if self.counter<=2:
                    raise ValueError("invalid")
            else:
                if self.counter<=1:
                     raise ValueError("invalid")
        result=0
        for num in self.points:
            result +=num
        return result

if __name__ == "__main__":
    bow =BowlingGame()
    game = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3]
    for g in game:
        bow.roll(g)
        bow.print()
    
    print(bow.score())
    
    