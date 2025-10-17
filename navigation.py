"""
Street navigation system API.
"""
from typing import List, Optional, Tuple
from graph import Graph
from dijkstra import dijkstra
from astar import astar


class Navigator:
    """Main interface for street navigation."""
    
    def __init__(self, graph: Graph):
        self.graph = graph
    
    def find_path_dijkstra(self, start: str, end: str) -> Tuple[Optional[List[str]], float]:
        """
        Find shortest path using Dijkstra's algorithm.
        
        Args:
            start: Starting location ID
            end: Destination location ID
        
        Returns:
            Tuple of (path as list of location IDs, total distance)
        """
        return dijkstra(self.graph, start, end)
    
    def find_path_astar(self, start: str, end: str) -> Tuple[Optional[List[str]], float]:
        """
        Find shortest path using A* algorithm.
        
        Args:
            start: Starting location ID
            end: Destination location ID
        
        Returns:
            Tuple of (path as list of location IDs, total distance)
        """
        return astar(self.graph, start, end)
    
    def get_route_description(self, path: Optional[List[str]]) -> List[str]:
        """
        Convert a path to human-readable directions.
        
        Args:
            path: List of node IDs representing the route
        
        Returns:
            List of direction strings
        """
        if not path:
            return ["No route found"]
        
        if len(path) == 1:
            return [f"You are already at {self.graph.get_node(path[0]).name}"]
        
        directions = [f"Start at {self.graph.get_node(path[0]).name}"]
        
        for i in range(len(path) - 1):
            current = self.graph.get_node(path[i])
            next_node = self.graph.get_node(path[i + 1])
            
            # Find the edge between current and next
            edge = None
            for e in self.graph.edges[path[i]]:
                if e.to_node == path[i + 1]:
                    edge = e
                    break
            
            if edge:
                street_name = edge.name or "the street"
                directions.append(f"Go to {next_node.name} via {street_name} ({edge.weight:.1f} units)")
            else:
                directions.append(f"Go to {next_node.name}")
        
        directions.append(f"Arrive at {self.graph.get_node(path[-1]).name}")
        
        return directions
