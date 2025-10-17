#!/usr/bin/env python3
"""
Simple demonstration of the navigation system with a visual representation.
"""
from graph import Graph
from navigation import Navigator


def print_network_map():
    """Print a simple ASCII representation of the street network."""
    print("""
    Street Network Map:
    
         Store (1,2)
           / \\
          /   \\
         /     \\
    Home(0,0)   School(2,1) -- Library(4,1)
                  \\           /
                   \\         /
                    \\       /
                     Park(3,3)
                       |
                   Hospital(2,4)
    """)


def main():
    """Run a simple demonstration."""
    print("=" * 70)
    print("STREET NAVIGATION SYSTEM DEMO")
    print("=" * 70)
    
    print_network_map()
    
    # Create the network
    graph = Graph()
    
    # Add locations with coordinates
    locations = [
        ("Home", 0, 0),
        ("School", 2, 1),
        ("Store", 1, 2),
        ("Park", 3, 3),
        ("Library", 4, 1),
        ("Hospital", 2, 4),
    ]
    
    for location, x, y in locations:
        graph.add_node(location, x, y, location)
    
    # Add streets
    streets = [
        ("Home", "School", 2.5, "Main Street"),
        ("Home", "Store", 2.0, "Oak Avenue"),
        ("School", "Library", 2.0, "Elm Street"),
        ("Store", "School", 1.5, "Park Road"),
        ("Store", "Park", 2.5, "Lake Drive"),
        ("Store", "Hospital", 3.0, "Center Street"),
        ("Park", "Library", 2.0, "Pine Avenue"),
        ("Park", "Hospital", 1.5, "River Road"),
    ]
    
    for from_loc, to_loc, distance, name in streets:
        graph.add_edge(from_loc, to_loc, distance, name)
    
    # Create navigator
    navigator = Navigator(graph)
    
    # Test cases
    test_routes = [
        ("Home", "Hospital"),
        ("Home", "Library"),
        ("Store", "Library"),
    ]
    
    print("\n" + "=" * 70)
    print("PATHFINDING DEMONSTRATIONS")
    print("=" * 70)
    
    for start, end in test_routes:
        print(f"\n{'-' * 70}")
        print(f"Finding route from {start} to {end}")
        print(f"{'-' * 70}")
        
        # Use Dijkstra
        path_d, dist_d = navigator.find_path_dijkstra(start, end)
        print(f"\nDijkstra's Algorithm:")
        print(f"  Path: {' → '.join(path_d)}")
        print(f"  Distance: {dist_d:.1f} units")
        
        # Use A*
        path_a, dist_a = navigator.find_path_astar(start, end)
        print(f"\nA* Algorithm:")
        print(f"  Path: {' → '.join(path_a)}")
        print(f"  Distance: {dist_a:.1f} units")
        
        # Verify both give optimal results
        if dist_d == dist_a:
            print(f"\n  ✓ Both algorithms found optimal path!")
        
        # Show directions for Dijkstra path
        print(f"\nTurn-by-turn directions:")
        for i, direction in enumerate(navigator.get_route_description(path_d), 1):
            print(f"  {i}. {direction}")
    
    print("\n" + "=" * 70)
    print("Demo completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
