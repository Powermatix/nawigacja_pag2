# Street Navigation System (nawigacja_pag2)

A Python implementation of street navigation using Dijkstra's and A* pathfinding algorithms.

## Features

- **Graph-based street network representation**: Nodes represent intersections/locations, edges represent streets
- **Dijkstra's algorithm**: Finds the shortest path between two locations
- **A* algorithm**: Optimized pathfinding using Euclidean distance heuristic
- **Navigation API**: Simple interface for route finding and directions
- **Comprehensive test suite**: Unit tests for all components

## Project Structure

```
.
├── graph.py           # Graph data structure (nodes, edges)
├── dijkstra.py        # Dijkstra's algorithm implementation
├── astar.py          # A* algorithm implementation
├── navigation.py     # Navigator API
├── test_navigation.py # Unit tests
├── example.py        # Usage examples
├── demo.py           # Interactive demo with visual network map
└── README.md         # This file
```

## Installation

No external dependencies required. Uses only Python standard library.

Requirements:
- Python 3.6+

## Usage

### Basic Example

```python
from graph import Graph
from navigation import Navigator

# Create a street network
graph = Graph()

# Add locations (intersections)
graph.add_node("Home", 0, 0, "Home")
graph.add_node("Store", 1, 2, "Store")
graph.add_node("Park", 3, 3, "Park")

# Add streets (edges) with distances
graph.add_edge("Home", "Store", 2.0, "Main Street")
graph.add_edge("Store", "Park", 2.5, "Oak Avenue")
graph.add_edge("Home", "Park", 5.0, "Long Road")

# Create navigator
navigator = Navigator(graph)

# Find shortest path using Dijkstra
path, distance = navigator.find_path_dijkstra("Home", "Park")
print(f"Path: {path}")  # ['Home', 'Store', 'Park']
print(f"Distance: {distance}")  # 4.5

# Find shortest path using A*
path, distance = navigator.find_path_astar("Home", "Park")
print(f"Path: {path}")  # ['Home', 'Store', 'Park']
print(f"Distance: {distance}")  # 4.5

# Get turn-by-turn directions
directions = navigator.get_route_description(path)
for direction in directions:
    print(direction)
```

### Running the Example

```bash
python example.py
```

### Running the Demo

For a visual demonstration with a network map:

```bash
python demo.py
```

## Running Tests

```bash
python test_navigation.py
```

Or with verbose output:

```bash
python test_navigation.py -v
```

## Algorithms

### Dijkstra's Algorithm

- Finds the shortest path between two nodes in a weighted graph
- Guarantees optimal solution
- Time complexity: O((V + E) log V) where V is vertices and E is edges
- Does not use heuristics

### A* Algorithm

- Finds the shortest path using a heuristic function
- Uses Euclidean distance as heuristic (straight-line distance)
- Generally faster than Dijkstra for spatial graphs
- Time complexity: O((V + E) log V) in worst case, but often faster in practice
- Guarantees optimal solution with admissible heuristic

## API Reference

### Graph

```python
graph = Graph()
graph.add_node(node_id, x, y, name)  # Add a location
graph.add_edge(from_node, to_node, weight, name, bidirectional=True)  # Add a street
```

### Navigator

```python
navigator = Navigator(graph)

# Find path using Dijkstra
path, distance = navigator.find_path_dijkstra(start, end)

# Find path using A*
path, distance = navigator.find_path_astar(start, end)

# Get directions
directions = navigator.get_route_description(path)
```

## License

MIT License