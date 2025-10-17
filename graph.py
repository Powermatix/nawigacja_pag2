"""
Graph data structure for representing street networks.
"""
from typing import Dict, List, Tuple, Set
import math


class Node:
    """Represents an intersection or location in the street network."""
    
    def __init__(self, node_id: str, x: float = 0.0, y: float = 0.0, name: str = ""):
        self.id = node_id
        self.x = x  # Coordinate for A* heuristic
        self.y = y  # Coordinate for A* heuristic
        self.name = name or node_id
    
    def __repr__(self):
        return f"Node({self.id}, {self.name})"
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.id == other.id
    
    def __hash__(self):
        return hash(self.id)


class Edge:
    """Represents a street connecting two intersections."""
    
    def __init__(self, from_node: str, to_node: str, weight: float, name: str = ""):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight  # Distance or cost
        self.name = name
    
    def __repr__(self):
        return f"Edge({self.from_node} -> {self.to_node}, weight={self.weight})"


class Graph:
    """Graph representation of a street network."""
    
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: Dict[str, List[Edge]] = {}
    
    def add_node(self, node_id: str, x: float = 0.0, y: float = 0.0, name: str = "") -> Node:
        """Add a node (intersection) to the graph."""
        if node_id not in self.nodes:
            node = Node(node_id, x, y, name)
            self.nodes[node_id] = node
            self.edges[node_id] = []
            return node
        return self.nodes[node_id]
    
    def add_edge(self, from_node: str, to_node: str, weight: float, name: str = "", bidirectional: bool = True):
        """Add an edge (street) to the graph."""
        if from_node not in self.nodes:
            self.add_node(from_node)
        if to_node not in self.nodes:
            self.add_node(to_node)
        
        edge = Edge(from_node, to_node, weight, name)
        self.edges[from_node].append(edge)
        
        if bidirectional:
            reverse_edge = Edge(to_node, from_node, weight, name)
            self.edges[to_node].append(reverse_edge)
    
    def get_neighbors(self, node_id: str) -> List[Tuple[str, float]]:
        """Get all neighbors of a node with their edge weights."""
        if node_id not in self.edges:
            return []
        return [(edge.to_node, edge.weight) for edge in self.edges[node_id]]
    
    def get_node(self, node_id: str) -> Node:
        """Get a node by its ID."""
        return self.nodes.get(node_id)
    
    def euclidean_distance(self, node1_id: str, node2_id: str) -> float:
        """Calculate Euclidean distance between two nodes."""
        node1 = self.nodes.get(node1_id)
        node2 = self.nodes.get(node2_id)
        if node1 and node2:
            return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
        return 0.0
    
    def __repr__(self):
        return f"Graph(nodes={len(self.nodes)}, edges={sum(len(e) for e in self.edges.values())})"
