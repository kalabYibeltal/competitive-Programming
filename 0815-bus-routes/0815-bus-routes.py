class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        
        busesFromSource, busesToTarget=[], [] 
        for i in range(len(routes)):
            routes[i]=set(routes[i])
            if source in routes[i] and target in routes[i]:
                return 1
            elif source in routes[i]:
                busesFromSource.append(i)
            elif target in routes[i]:
                busesToTarget.append(i)
        
        adjList={i:[] for i in range(len(routes))}
        for i in range(len(routes)-1):
            for j in range(i+1, len(routes)):
                if len(routes[i]&routes[j])>0:
                    adjList[i].append(j)
                    adjList[j].append(i)
        
        leastNumBuses=inf
        for sourceBus in busesFromSource:
            numBuses={bus:inf for bus in adjList}
            numBuses[sourceBus]=1
            queue=[sourceBus]
            while len(queue)>0:
                curr=queue.pop(0)
                for bus in adjList[curr]:
                    if numBuses[bus]>numBuses[curr]+1:
                        numBuses[bus]=numBuses[curr]+1
                        queue.append(bus)
            for targetBus in busesToTarget:
                if leastNumBuses>numBuses[targetBus]:
                    leastNumBuses=numBuses[targetBus]

        if leastNumBuses!=inf:
            return leastNumBuses 
        else:
            return -1