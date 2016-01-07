from math import sin, cos, atan2, sqrt, pow, radians
from sys import maxint

R = 6371 #radius of earth
points = dict() #holds the point and its respective (latitude, longitude) tuple
paths = [] #list of possible detour paths that can be taken

#this function calculates the great-circle distance between two latitute/longtitude points
#equation referenced from: http://www.movable-type.co.uk/scripts/latlong.html
def calc_dist((lat1, lon1), (lat2, lon2)):
	#convert to radians
	lat1 = radians(lat1)
	lat2 = radians(lat2)
	lon1 = radians(lon1)
	lon2 = radians(lon2)

	#find distance
	delta_lat = lat2 - lat1
	delta_lon = lon2 - lon1
	a = pow(sin(delta_lat/2), 2) + cos(lat1) * cos(lat2) * pow(sin(delta_lon/2), 2)
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	return R * c

#this function uses the list of possible detour paths and the dictionary of points
#to determine the shortest detour path. It does so by calculating the distance along
#each path using the calc_dist function above.
def shortest_path():
	best_distance = maxint
	best_path = None

	#iterate over every path
	for path in paths:
		total_dist = 0 #keep track of total distance so far
		#iterate over every point in the path
		for i, point1 in enumerate(path):
			if i < len(path) - 1:
				point2 = path[i + 1]
				total_dist += calc_dist(points[point1], points[point2])
		#update the best distance and the corresponding path
		if total_dist < best_distance:
			best_distance = total_dist
			best_path = path

	return best_path

def main():
	#populate our dictionary of points
	points["A"] = (35.567980, -100.722656)
	points["B"] = (-54.901882, -69.082031)
	points["C"] = (64.377941, -148.535156)
	points["D"] = (-32.138409, -108.457031)

	#populate our list of possible detour paths
	paths.append(["A", "C", "D", "B"])
	paths.append(["C", "A", "B", "D"])

	best_path = shortest_path()
	print "The best detour path is: " + ", ".join(best_path)

if __name__ == "__main__": main()