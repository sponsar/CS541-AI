from PIL import Image,ImageDraw
from Tkinter import Tk,Button,Frame,Label
import math,sys
#path=sys.path[0]

class PointToPoint:
	def __init__(self,str,start_point,end_point):#"/PointPos.txt"
		self.path=sys.path[0]
		self.readPoints(str)
		self.Astar(start_point,end_point)
		self.Dijkstra(start_point,end_point)

	def readPoints(self,str):
		self.point_map=dict()
		infile=open(self.path+str)
		for line in infile:
			line=line.strip()#string
			column=line.split('=')
			self.point_map[eval(column[0])]=eval(column[1])
		infile.close()

	def action(self,point):#return a set of points
		return self.point_map[point]

	def distance(self,a,b):# a and b are tuple of points
		return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
	def draw(self,end_point,father,algorithm):
		img = Image.open(self.path+"/map.jpg")
		draw=ImageDraw.Draw(img)
		while end_point in father:
			draw.line((  end_point,father[end_point]  ),fill=(255,0,0))
			end_point=father[end_point]
		img.show()
		img.save(self.path+algorithm,"jpeg")

	def Astar(self,start_point, end_point): #void
		if start_point==end_point:
			return 
		# make a map, map<point,int>
		hash=dict()
		hash[start_point]=self.distance(start_point,end_point)

		cost=dict()
		cost[start_point]=0

		close_set=set()
		father=dict()

		while len(hash)>0:
			cur_point=min(hash,key=hash.get)
			close_set.add(cur_point)
			hash.pop(cur_point)
			if(cur_point==end_point):
				self.draw(end_point,father,"/Astar_map.jpg")
				return

			for next_point in self.action(cur_point):
				if next_point not in close_set:
					heuristic=cost[cur_point]+self.distance(cur_point,next_point)+self.distance(next_point,end_point)

					if (next_point not in hash) or (heuristic<hash[next_point]):
						hash[next_point]=heuristic
						cost[next_point]=cost[cur_point]+self.distance(cur_point,next_point)
						father[next_point]=cur_point
	def Dijkstra(self,start_point, end_point):
		if start_point==end_point:
			return
		hash=dict()
		hash[start_point]=0

		close_set=set()
		father=dict()

		while len(hash)>0:
			cur_point=min(hash,key=hash.get)
			close_set.add(cur_point)
			if(cur_point==end_point):
				self.draw(end_point,father,"/Dijkstra_map.jpg")
				return
			for next_point in self.action(cur_point):
				if next_point not in close_set:
					dij=hash[cur_point]+self.distance(cur_point,next_point)
					if (next_point not in hash) or (dij<hash[next_point]):
						hash[next_point]=dij
						father[next_point]=cur_point
			hash.pop(cur_point)


def main():
	PointToPoint("/PointPos.txt",(40,240),(535,20))

main()




