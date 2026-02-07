# 🗼 Tower of Hanoi State Solver
A recursive algorithm that solves the Tower of Hanoi puzzle while tracking and visualizing the state of all three rods at every step.

### 🧠 Recursive Logic
The solver follows a classic recursive pattern to move $n$ disks from a Source rod to a Target rod using an Auxiliary rod:
1.  **Move** $n-1$ disks from Source to Auxiliary.
2.  **Move** the $n^{th}$ (largest) disk from Source to Target.
3.  **Move** $n-1$ disks from Auxiliary to Target.



### 🛠️ Features
* **State Visualization:** Unlike basic solvers, this implementation maintains a real-time representation of the disks using Python lists.
* **Efficient Recursion:** Solves the puzzle in the optimal $2^n - 1$ moves.
* **String Formatting:** Outputs the rod states in a clean, readable format suitable for logging or terminal display.

### 💻 Skills Demonstrated
* **Recursive Function Design**
* **State-Space Tracking**
* **Data Structure Manipulation (Stacks/Lists)**
