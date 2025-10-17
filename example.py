"""
Example usage of the street navigation system.
"""
from graph import Graph
from navigation import Navigator


def main():
    """Demonstrate the street navigation system."""
    
    # Create a street network
    print("Creating street network...")
    graph = Graph()
    
    # Add locations (intersections)
    graph.add_node("Home", 0, 0, "Home")
    graph.add_node("School", 2, 1, "School")
    graph.add_node("Store", 1, 2, "Store")
    graph.add_node("Park", 3, 3, "Park")
    graph.add_node("Library", 4, 1, "Library")
    graph.add_node("Hospital", 2, 4, "Hospital")
    
    # Add streets (edges) with distances
    graph.add_edge("Home", "School", 2.5, "Main Street")
    graph.add_edge("Home", "Store", 2.0, "Oak Avenue")
    graph.add_edge("School", "Library", 2.0, "Elm Street")
    graph.add_edge("Store", "School", 1.5, "Park Road")
    graph.add_edge("Store", "Park", 2.5, "Lake Drive")
    graph.add_edge("Store", "Hospital", 3.0, "Center Street")
    graph.add_edge("Park", "Library", 2.0, "Pine Avenue")
    graph.add_edge("Park", "Hospital", 1.5, "River Road")
    
    # Create navigator
    navigator = Navigator(graph)
    
    print(f"\nGraph created with {len(graph.nodes)} locations")
    print(f"Total streets: {sum(len(edges) for edges in graph.edges.values())}")
    
    # Example 1: Find path using Dijkstra
    print("\n" + "="*60)
    print("Example 1: Route from Home to Hospital using Dijkstra")
    print("="*60)
    
    path, distance = navigator.find_path_dijkstra("Home", "Hospital")
    if path:
        print(f"\nShortest path found! Total distance: {distance:.1f} units")
        print("\nRoute:")
        for direction in navigator.get_route_description(path):
            print(f"  {direction}")
    else:
        print("No route found!")
    
    # Example 2: Find path using A*
    print("\n" + "="*60)
    print("Example 2: Route from Home to Library using A*")
    print("="*60)
    
    path, distance = navigator.find_path_astar("Home", "Library")
    if path:
        print(f"\nShortest path found! Total distance: {distance:.1f} units")
        print("\nRoute:")
        for direction in navigator.get_route_description(path):
            print(f"  {direction}")
    else:
        print("No route found!")
    
    # Example 3: Compare both algorithms
    print("\n" + "="*60)
    print("Example 3: Comparing Dijkstra vs A*")
    print("="*60)
    
    start, end = "Home", "Park"
    
    path_dijkstra, dist_dijkstra = navigator.find_path_dijkstra(start, end)
    path_astar, dist_astar = navigator.find_path_astar(start, end)
    
    print(f"\nRoute from {start} to {end}:")
    print(f"Dijkstra: {' -> '.join(path_dijkstra)} (distance: {dist_dijkstra:.1f})")
    print(f"A*:       {' -> '.join(path_astar)} (distance: {dist_astar:.1f})")
    
    if dist_dijkstra == dist_astar:
        print("\n✓ Both algorithms found optimal paths with the same distance!")
    
    # Example 4: Multiple routes
    print("\n" + "="*60)
    print("Example 4: Finding routes from Home to all locations")
    print("="*60)
    
    for destination in ["School", "Store", "Park", "Library", "Hospital"]:
        path, distance = navigator.find_path_astar("Home", destination)
        if path:
            print(f"\nTo {destination}: {distance:.1f} units")
            print(f"  Route: {' -> '.join(path)}")


if __name__ == "__main__":
    main()
