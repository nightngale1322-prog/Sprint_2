class PointsForPlace:
    def __init__(self, place):
        self.place = place

    def get_points_for_place(self):
        if self.place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif self.place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - self.place
            return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
            return points

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self, points):
        super().__init__(points)
        self.points = 0
    def get_total_points(self, meters, place):
        points_place = self.get_points_for_place()
        points_meters = PointsForMeters.get_points_for_meters(meters)
        total = points_place + points_meters
        return total
   
points_for_place = PointsForPlace(10)
print(points_for_place.get_points_for_place())

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints(10)
print(total_points.get_total_points(100, 10))
