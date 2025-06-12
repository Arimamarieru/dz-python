from constants import *

class Helicopter:
    def __init__(self,y,x):
        self.y,self.x = y,x
        self.cap      = START_CAP
        self.water    = 0
        self.lives    = START_LIVES
        self.score    = 0

    # ── движение ──
    def move(self,d,w,h):
        dy,dx = {'w':(-1,0),'s':(1,0),'a':(0,-1),'d':(0,1)}.get(d,(0,0))
        ny,nx = self.y+dy,self.x+dx
        if 0<=ny<h and 0<=nx<w: self.y,self.x = ny,nx

    # ── действия ──
    def reload(self): self.water=self.cap

    def extinguish(self,board):
        if self.water and board.extinguish(self.y,self.x):
            self.water-=1; self.score+=1; return True
        return False

    def heal(self):
        if self.score>=HEAL_COST and self.lives<9:
            self.score-=HEAL_COST; self.lives+=1; return True
        return False

    def upgrade(self):
        if self.score>=UPGRADE_COST and self.cap<9:
            self.score-=UPGRADE_COST; self.cap+=1; return True
        return False

    def save_dict(self): return self.__dict__
    @classmethod
    def from_dict(cls,d):
        h=cls(d['y'],d['x']); h.__dict__.update(d); return h
