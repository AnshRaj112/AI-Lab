# Test Cases for Day 2 Programs

## Sample Graph
We'll use a simple undirected graph with 4 vertices:
- Vertices: 0, 1, 2, 3
- Edges: (0,1), (1,2), (2,3), (0,2)

### Adjacency Matrix Representation:
```
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
```

### Adjacency List Representation:
```
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
```

---

## File 1.py - Count Edges (Matrix)

### Input:
```
Enter the number of vertices: 4
Enter the row 1: 0 1 1 0
Enter the row 2: 1 0 1 0
Enter the row 3: 1 1 0 1
Enter the row 4: 0 0 1 0
```

### Expected Output:
```
Adjacency Matrix:
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
Number of edges: 4
```

---

## File 2.py - Count Edges (List)

### Input:
```
Enter the number of vertices: 4
Enter neighbors of vertex 0: 1 2
Enter neighbors of vertex 1: 0 2
Enter neighbors of vertex 2: 0 1 3
Enter neighbors of vertex 3: 2
```

### Expected Output:
```
Adjacency List:
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
Number of edges: 4
```

---

## File 3.py - Calculate Degrees (Matrix)

### Input:
```
Enter the number of vertices: 4
Enter the row 1: 0 1 1 0
Enter the row 2: 1 0 1 0
Enter the row 3: 1 1 0 1
Enter the row 4: 0 0 1 0
```

### Expected Output:
```
Adjacency Matrix:
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
Degrees: [2, 2, 3, 1]
```

---

## File 4.py - Calculate Degrees (List)

### Input:
```
Enter the number of vertices: 4
Enter neighbors of vertex 0: 1 2
Enter neighbors of vertex 1: 0 2
Enter neighbors of vertex 2: 0 1 3
Enter neighbors of vertex 3: 2
```

### Expected Output:
```
Adjacency List:
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
Degrees: [2, 2, 3, 1]
```

---

## File 5.py - Check Direct Connection (Matrix)

### Test Case 1: Connected vertices
#### Input:
```
Enter the number of vertices: 4
Enter the row 1: 0 1 1 0
Enter the row 2: 1 0 1 0
Enter the row 3: 1 1 0 1
Enter the row 4: 0 0 1 0
Enter the first vertex: 0
Enter the second vertex: 1
```

#### Expected Output:
```
Adjacency Matrix:
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
Vertices 0 and 1 are directly connected.
```

### Test Case 2: Not connected vertices
#### Input:
```
Enter the number of vertices: 4
Enter the row 1: 0 1 1 0
Enter the row 2: 1 0 1 0
Enter the row 3: 1 1 0 1
Enter the row 4: 0 0 1 0
Enter the first vertex: 0
Enter the second vertex: 3
```

#### Expected Output:
```
Adjacency Matrix:
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
Vertices 0 and 3 are NOT directly connected.
```

---

## File 6.py - Check Direct Connection (List)

### Test Case 1: Connected vertices
#### Input:
```
Enter the number of vertices: 4
Enter neighbors of vertex 0: 1 2
Enter neighbors of vertex 1: 0 2
Enter neighbors of vertex 2: 0 1 3
Enter neighbors of vertex 3: 2
Enter the first vertex: 0
Enter the second vertex: 1
```

#### Expected Output:
```
Adjacency List:
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
Vertices 0 and 1 are directly connected.
```

### Test Case 2: Not connected vertices
#### Input:
```
Enter the number of vertices: 4
Enter neighbors of vertex 0: 1 2
Enter neighbors of vertex 1: 0 2
Enter neighbors of vertex 2: 0 1 3
Enter neighbors of vertex 3: 2
Enter the first vertex: 0
Enter the second vertex: 3
```

#### Expected Output:
```
Adjacency List:
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
Vertices 0 and 3 are NOT directly connected.
```

---

## File 7.py - Check Path Existence (Matrix)

### Test Case 1: Valid path
#### Input:
```
Enter the number of vertices: 4
Enter the row 1: 0 1 1 0
Enter the row 2: 1 0 1 0
Enter the row 3: 1 1 0 1
Enter the row 4: 0 0 1 0
Enter the sequence of nodes (space-separated): 0 1 2 3
```

#### Expected Output:
```
Adjacency Matrix:
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
Path exists with sequence: [0, 1, 2, 3]
Length of the path: 3
```

### Test Case 2: Invalid path (not connected)
#### Input:
```
Enter the number of vertices: 4
Enter the row 1: 0 1 1 0
Enter the row 2: 1 0 1 0
Enter the row 3: 1 1 0 1
Enter the row 4: 0 0 1 0
Enter the sequence of nodes (space-separated): 0 3
```

#### Expected Output:
```
Adjacency Matrix:
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
Path does NOT exist with sequence: [0, 3]
```

### Test Case 3: Another valid path
#### Input:
```
Enter the number of vertices: 4
Enter the row 1: 0 1 1 0
Enter the row 2: 1 0 1 0
Enter the row 3: 1 1 0 1
Enter the row 4: 0 0 1 0
Enter the sequence of nodes (space-separated): 0 2 3
```

#### Expected Output:
```
Adjacency Matrix:
[0, 1, 1, 0]
[1, 0, 1, 0]
[1, 1, 0, 1]
[0, 0, 1, 0]
Path exists with sequence: [0, 2, 3]
Length of the path: 2
```

---

## File 8.py - Check Path Existence (List)

### Test Case 1: Valid path
#### Input:
```
Enter the number of vertices: 4
Enter neighbors of vertex 0: 1 2
Enter neighbors of vertex 1: 0 2
Enter neighbors of vertex 2: 0 1 3
Enter neighbors of vertex 3: 2
Enter the sequence of nodes (space-separated): 0 1 2 3
```

#### Expected Output:
```
Adjacency List:
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
Path exists with sequence: [0, 1, 2, 3]
Length of the path: 3
```

### Test Case 2: Invalid path (not connected)
#### Input:
```
Enter the number of vertices: 4
Enter neighbors of vertex 0: 1 2
Enter neighbors of vertex 1: 0 2
Enter neighbors of vertex 2: 0 1 3
Enter neighbors of vertex 3: 2
Enter the sequence of nodes (space-separated): 0 3
```

#### Expected Output:
```
Adjacency List:
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
Path does NOT exist with sequence: [0, 3]
```

### Test Case 3: Another valid path
#### Input:
```
Enter the number of vertices: 4
Enter neighbors of vertex 0: 1 2
Enter neighbors of vertex 1: 0 2
Enter neighbors of vertex 2: 0 1 3
Enter neighbors of vertex 3: 2
Enter the sequence of nodes (space-separated): 0 2 3
```

#### Expected Output:
```
Adjacency List:
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1, 3]
Vertex 3: [2]
Path exists with sequence: [0, 2, 3]
Length of the path: 2
```

---

## Additional Test Cases (Simple 3-vertex triangle)

For a simpler test, you can use a triangle graph with 3 vertices:

### Matrix:
```
[0, 1, 1]
[1, 0, 1]
[1, 1, 0]
```

### List:
```
Vertex 0: [1, 2]
Vertex 1: [0, 2]
Vertex 2: [0, 1]
```

This graph has:
- 3 edges
- All vertices have degree 2
- All pairs of vertices are directly connected
- Any sequence of vertices forms a valid path

