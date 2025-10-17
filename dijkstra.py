"""
Dijkstra's algorithm implementation for shortest path finding.
"""
import heapq
from typing import Dict, List, Optional, Tuple
from graph import Graph


def dijkstra(graph: Graph, start: str, end: str) -> Tuple[Optional[List[str]], float]:
    """
    Find the shortest path from start to end using Dijkstra's algorithm.
    
    Args:
        graph: The street network graph
        start: Starting node ID
        end: Destination node ID
    
    Returns:
        Tuple of (path as list of node IDs, total distance)
        Returns (None, float('inf')) if no path exists
    """
    if start not in graph.nodes or end not in graph.nodes:
        return None, float('inf')
    
    # Priority queue: (distance, node_id)
    pq = [(0, start)]
    
    # Distance from start to each node
    distances: Dict[str, float] = {node_id: float('inf') for node_id in graph.nodes}
    distances[start] = 0
    
    # Previous node in optimal path
    previous: Dict[str, Optional[str]] = {node_id: None for node_id in graph.nodes}
    
    # Visited nodes
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Found the destination
        if current_node == end:
            break
        
        # Skip if we've found a better path already
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighbors
        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_distance + weight
            
            # Found a shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    if distances[end] == float('inf'):
        return None, float('inf')
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return path, distances[end]
