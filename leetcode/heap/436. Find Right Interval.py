import heapq
from typing import List


class Solution_brutforce:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ret = []
        intervals_heap = []

        for interval_i in intervals:
            min_interval = -1

            for j, interval_j in enumerate(intervals):
                if interval_i == interval_j:
                    continue

                if interval_i[1] <= interval_j[0]:
                    if min_interval == -1:
                        min_interval = j
                    elif interval_j[0] < intervals[min_interval][0]:
                            min_interval = j

            ret.append(min_interval)
        return ret


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ret = [-1]*len(intervals)
        # start_intervals_heap, end_intervals_heap = zip(*intervals)
        start_heap_intervals = [[h[0]*-1, j] for j, h in enumerate(intervals)]
        end_heap_intervals = [[h[1]*-1, j] for j, h in enumerate(intervals)]

        heapq.heapify(start_heap_intervals)
        heapq.heapify(end_heap_intervals)

        for _ in range(len(end_heap_intervals)):
            ei, i = heapq.heappop(end_heap_intervals)
            top_start = [-1,-1]

            for _ in range(len(start_heap_intervals)):
                sj, j = start_heap_intervals[0]
                sj *= -1

                if ei * -1 <= sj:
                    top_start = heapq.heappop(start_heap_intervals)
                else:
                    break

            ret[i] = top_start[1]

            if top_start[1] != -1:
                heapq.heappush(start_heap_intervals,top_start)


        return ret

x = Solution().findRightInterval([[-100,-92],[-99,-49],[-98,-24],[-97,-38],[-96,-65],[-95,-22],[-94,-49],[-93,-14],[-92,-68],[-91,-81],[-90,-49],[-89,-23],[-88,5],[-87,-44],[-86,2],[-85,-81],[-84,-56],[-83,-53],[-82,-41],[-81,-68],[-80,-76],[-79,-9],[-78,-68],[-77,-19],[-76,-15],[-75,-41],[-74,26],[-73,6],[-72,-55],[-71,-35],[-70,28],[-69,-42],[-68,-55],[-67,1],[-66,-55],[-65,-31],[-64,16],[-63,-13],[-62,18],[-61,-39],[-60,8],[-59,14],[-58,36],[-57,-20],[-56,30],[-55,-9],[-54,-25],[-53,39],[-52,43],[-51,7],[-50,-48],[-49,5],[-48,-39],[-47,-2],[-46,23],[-45,46],[-44,-19],[-43,54],[-42,-11],[-41,-37],[-40,-17],[-39,28],[-38,12],[-37,-12],[-36,-34],[-35,19],[-34,44],[-33,-24],[-32,-3],[-31,3],[-30,69],[-29,53],[-28,8],[-27,-13],[-26,40],[-25,-10],[-24,40],[-23,14],[-22,4],[-21,49],[-20,-4],[-19,76],[-18,12],[-17,-15],[-16,2],[-15,81],[-14,-8],[-13,-8],[-12,40],[-11,88],[-10,79],[-9,15],[-8,-2],[-7,76],[-6,47],[-5,62],[-4,13],[-3,35],[-2,37],[-1,44],[0,2],[1,99],[2,74],[3,32],[4,42],[5,64],[6,84],[7,105],[8,103],[9,14],[10,20],[11,43],[12,58],[13,89],[14,50],[15,114],[16,59],[17,117],[18,87],[19,32],[20,81],[21,79],[22,117],[23,32],[24,120],[25,94],[26,40],[27,58],[28,35],[29,92],[30,73],[31,97],[32,115],[33,86],[34,102],[35,57],[36,132],[37,50],[38,110],[39,41],[40,131],[41,73],[42,81],[43,101],[44,61],[45,136],[46,87],[47,127],[48,84],[49,56],[50,123],[51,150],[52,148],[53,73],[54,109],[55,79],[56,146],[57,118],[58,64],[59,86],[60,84],[61,68],[62,76],[63,134],[64,103],[65,160],[66,87],[67,112],[68,135],[69,104],[70,97],[71,166],[72,136],[73,112],[74,119],[75,166],[76,127],[77,137],[78,102],[79,127],[80,166],[81,99],[82,155],[83,123],[84,132],[85,171],[86,183],[87,173],[88,112],[89,110],[90,135],[91,160],[92,128],[93,109],[94,120],[95,130],[96,139],[97,109],[98,178],[99,152]]) # [-1, 2, 0]
print(x)