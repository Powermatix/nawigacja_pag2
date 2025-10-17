"""
A* algorithm implementation for shortest path finding with heuristic.
"""
import heapq
from typing import Dict, List, Optional, Tuple
from graph import Graph


def astar(graph: Graph, start: str, end: str) -> Tuple[Optional[List[str]], float]:
    """
    Find the shortest path from start to end using A* algorithm.
    
    Uses Euclidean distance as heuristic function.
    
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
    
    def heuristic(node_id: str) -> float:
        """Heuristic function: Euclidean distance to goal."""
        return graph.euclidean_distance(node_id, end)
    
    # Priority queue: (f_score, node_id)
    # f_score = g_score + h_score
    pq = [(heuristic(start), start)]
    
    # Cost from start to each node (g_score)
    g_score: Dict[str, float] = {node_id: float('inf') for node_id in graph.nodes}
    g_score[start] = 0
    
    # Estimated total cost from start to goal through node (f_score)
    f_score: Dict[str, float] = {node_id: float('inf') for node_id in graph.nodes}
    f_score[start] = heuristic(start)
    
    # Previous node in optimal path
    previous: Dict[str, Optional[str]] = {node_id: None for node_id in graph.nodes}
    
    # Visited nodes
    visited = set()
    
    while pq:
        current_f, current_node = heapq.heappop(pq)
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        # Found the destination
        if current_node == end:
            break
        
        # Check all neighbors
        for neighbor, weight in graph.get_neighbors(current_node):
            if neighbor in visited:
                continue
            
            tentative_g_score = g_score[current_node] + weight
            
            # Found a better path to neighbor
            if tentative_g_score < g_score[neighbor]:
                previous[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                heapq.heappush(pq, (f_score[neighbor], neighbor))
    
    # Reconstruct path
    if g_score[end] == float('inf'):
        return None, float('inf')
    
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return path, g_score[end]
