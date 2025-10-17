"""
Tests for street navigation algorithms.
"""
import unittest
from graph import Graph, Node, Edge
from dijkstra import dijkstra
from astar import astar
from navigation import Navigator


class TestGraph(unittest.TestCase):
    """Tests for the Graph data structure."""
    
    def setUp(self):
        self.graph = Graph()
    
    def test_add_node(self):
        """Test adding nodes to the graph."""
        node = self.graph.add_node("A", 0, 0, "Location A")
        self.assertEqual(node.id, "A")
        self.assertEqual(node.name, "Location A")
        self.assertIn("A", self.graph.nodes)
    
    def test_add_edge(self):
        """Test adding edges to the graph."""
        self.graph.add_node("A", 0, 0)
        self.graph.add_node("B", 1, 1)
        self.graph.add_edge("A", "B", 1.5, "Main Street")
        
        neighbors = self.graph.get_neighbors("A")
        self.assertEqual(len(neighbors), 1)
        self.assertEqual(neighbors[0], ("B", 1.5))
    
    def test_bidirectional_edge(self):
        """Test bidirectional edges."""
        self.graph.add_node("A", 0, 0)
        self.graph.add_node("B", 1, 1)
        self.graph.add_edge("A", "B", 1.5, bidirectional=True)
        
        # Check both directions
        self.assertEqual(len(self.graph.get_neighbors("A")), 1)
        self.assertEqual(len(self.graph.get_neighbors("B")), 1)
    
    def test_euclidean_distance(self):
        """Test Euclidean distance calculation."""
        self.graph.add_node("A", 0, 0)
        self.graph.add_node("B", 3, 4)
        
        distance = self.graph.euclidean_distance("A", "B")
        self.assertEqual(distance, 5.0)


class TestDijkstra(unittest.TestCase):
    """Tests for Dijkstra's algorithm."""
    
    def setUp(self):
        """Create a simple test graph."""
        self.graph = Graph()
        # Create a simple network
        #     B
        #    / \
        #   A   D
        #    \ /
        #     C
        self.graph.add_node("A", 0, 0, "A")
        self.graph.add_node("B", 1, 1, "B")
        self.graph.add_node("C", 1, -1, "C")
        self.graph.add_node("D", 2, 0, "D")
        
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("A", "C", 2.0)
        self.graph.add_edge("B", "D", 3.0)
        self.graph.add_edge("C", "D", 1.0)
    
    def test_simple_path(self):
        """Test finding a simple path."""
        path, distance = dijkstra(self.graph, "A", "D")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "D")
        # Shortest path should be A -> C -> D with distance 3.0
        self.assertEqual(distance, 3.0)
        self.assertEqual(path, ["A", "C", "D"])
    
    def test_same_start_end(self):
        """Test when start and end are the same."""
        path, distance = dijkstra(self.graph, "A", "A")
        self.assertEqual(path, ["A"])
        self.assertEqual(distance, 0)
    
    def test_no_path(self):
        """Test when no path exists."""
        self.graph.add_node("E", 10, 10, "E")
        path, distance = dijkstra(self.graph, "A", "E")
        self.assertIsNone(path)
        self.assertEqual(distance, float('inf'))
    
    def test_invalid_nodes(self):
        """Test with invalid node IDs."""
        path, distance = dijkstra(self.graph, "A", "Z")
        self.assertIsNone(path)
        self.assertEqual(distance, float('inf'))


class TestAStar(unittest.TestCase):
    """Tests for A* algorithm."""
    
    def setUp(self):
        """Create a simple test graph."""
        self.graph = Graph()
        # Create a simple network with coordinates
        self.graph.add_node("A", 0, 0, "A")
        self.graph.add_node("B", 1, 1, "B")
        self.graph.add_node("C", 1, -1, "C")
        self.graph.add_node("D", 2, 0, "D")
        
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("A", "C", 2.0)
        self.graph.add_edge("B", "D", 3.0)
        self.graph.add_edge("C", "D", 1.0)
    
    def test_simple_path(self):
        """Test finding a simple path."""
        path, distance = astar(self.graph, "A", "D")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "D")
        # Shortest path should be A -> C -> D with distance 3.0
        self.assertEqual(distance, 3.0)
        self.assertEqual(path, ["A", "C", "D"])
    
    def test_same_start_end(self):
        """Test when start and end are the same."""
        path, distance = astar(self.graph, "A", "A")
        self.assertEqual(path, ["A"])
        self.assertEqual(distance, 0)
    
    def test_no_path(self):
        """Test when no path exists."""
        self.graph.add_node("E", 10, 10, "E")
        path, distance = astar(self.graph, "A", "E")
        self.assertIsNone(path)
        self.assertEqual(distance, float('inf'))
    
    def test_invalid_nodes(self):
        """Test with invalid node IDs."""
        path, distance = astar(self.graph, "A", "Z")
        self.assertIsNone(path)
        self.assertEqual(distance, float('inf'))


class TestNavigator(unittest.TestCase):
    """Tests for the Navigator class."""
    
    def setUp(self):
        """Create a test graph and navigator."""
        self.graph = Graph()
        self.graph.add_node("Home", 0, 0, "Home")
        self.graph.add_node("Store", 1, 1, "Store")
        self.graph.add_node("Park", 2, 0, "Park")
        
        self.graph.add_edge("Home", "Store", 1.5, "Main St")
        self.graph.add_edge("Store", "Park", 2.0, "Oak Ave")
        self.graph.add_edge("Home", "Park", 4.0, "Long Rd")
        
        self.navigator = Navigator(self.graph)
    
    def test_find_path_dijkstra(self):
        """Test Dijkstra pathfinding through Navigator."""
        path, distance = self.navigator.find_path_dijkstra("Home", "Park")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "Home")
        self.assertEqual(path[-1], "Park")
        self.assertEqual(distance, 3.5)  # Home -> Store -> Park
    
    def test_find_path_astar(self):
        """Test A* pathfinding through Navigator."""
        path, distance = self.navigator.find_path_astar("Home", "Park")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "Home")
        self.assertEqual(path[-1], "Park")
        self.assertEqual(distance, 3.5)  # Home -> Store -> Park
    
    def test_route_description(self):
        """Test generating route descriptions."""
        path = ["Home", "Store", "Park"]
        directions = self.navigator.get_route_description(path)
        
        self.assertIsInstance(directions, list)
        self.assertGreater(len(directions), 0)
        self.assertIn("Home", directions[0])
        self.assertIn("Park", directions[-1])
    
    def test_route_description_no_path(self):
        """Test route description when no path exists."""
        directions = self.navigator.get_route_description(None)
        self.assertEqual(directions, ["No route found"])
    
    def test_route_description_same_location(self):
        """Test route description when already at destination."""
        directions = self.navigator.get_route_description(["Home"])
        self.assertIn("already at", directions[0].lower())


class TestComplexNetwork(unittest.TestCase):
    """Tests with a more complex street network."""
    
    def setUp(self):
        """Create a complex test network."""
        self.graph = Graph()
        
        # Create a grid-like network
        #   A---B---C
        #   |   |   |
        #   D---E---F
        #   |   |   |
        #   G---H---I
        
        nodes = [
            ("A", 0, 2), ("B", 1, 2), ("C", 2, 2),
            ("D", 0, 1), ("E", 1, 1), ("F", 2, 1),
            ("G", 0, 0), ("H", 1, 0), ("I", 2, 0)
        ]
        
        for node_id, x, y in nodes:
            self.graph.add_node(node_id, x, y, f"Location {node_id}")
        
        # Add horizontal edges
        edges = [
            ("A", "B", 1.0), ("B", "C", 1.0),
            ("D", "E", 1.0), ("E", "F", 1.0),
            ("G", "H", 1.0), ("H", "I", 1.0),
        ]
        
        # Add vertical edges
        edges.extend([
            ("A", "D", 1.0), ("B", "E", 1.0), ("C", "F", 1.0),
            ("D", "G", 1.0), ("E", "H", 1.0), ("F", "I", 1.0),
        ])
        
        for from_node, to_node, weight in edges:
            self.graph.add_edge(from_node, to_node, weight)
    
    def test_dijkstra_diagonal(self):
        """Test Dijkstra on diagonal path."""
        path, distance = dijkstra(self.graph, "A", "I")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "I")
        self.assertEqual(distance, 4.0)  # Shortest Manhattan distance
    
    def test_astar_diagonal(self):
        """Test A* on diagonal path."""
        path, distance = astar(self.graph, "A", "I")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "I")
        self.assertEqual(distance, 4.0)  # Shortest Manhattan distance
    
    def test_algorithms_agree(self):
        """Test that both algorithms find paths of same length."""
        for start in ["A", "B", "G"]:
            for end in ["C", "F", "I"]:
                dijkstra_path, dijkstra_dist = dijkstra(self.graph, start, end)
                astar_path, astar_dist = astar(self.graph, start, end)
                
                # Both should find optimal paths
                self.assertEqual(dijkstra_dist, astar_dist,
                               f"Distance mismatch for {start} to {end}")


if __name__ == "__main__":
    unittest.main()
