# Beginner Puzzle Solver

## About
This repository aims to implement various search algorithms to solve the NP-hard puzzle problem. The objective is to learn these algorithms and compare their performance practically.

## Algorithms Implemented
1. **Breadth-First Search (BFS)**: Explores all neighboring nodes at the current depth before moving deeper, ensuring the shortest path but using more memory.
2. **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking, conserving memory but not guaranteeing the shortest path.
3. **Depth-Limited Search**: A variant of DFS that restricts the depth of exploration to avoid infinite paths.
4. **Iterative Deepening Search (IDS)**: Combines the depth efficiency of DFS with the completeness of BFS by incrementally increasing the depth limit.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/JavadiSM/puzzle-solver
   ```

2. Navigate to the project directory:
   ```bash
   cd puzzle-solver
   ```

3. Run the main script:
   ```bash
   .\main.py
   ```

4. Enter the size of the puzzle grid (e.g., 3 for a 3x3 grid) and the initial puzzle state.

## Future Work
- Implement additional search algorithms like A* and Greedy Best-First Search.
- Benchmark and compare algorithm performance. (if I have time to)
- Develop a graphical user interface (GUI). (I would be grateful if you are eager to cooperate)
