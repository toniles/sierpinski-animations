# sierpinski-animations


## The Essence of the Project

This initiative embodies a synthesis of mathematical exactitude and creative aesthetics. It encourages active exploration of fractal geometry through adjustable variables. Experimentation is welcomed.

## Installation

pip install matplotlib numpy


Visual samples from the repository:

- **3DPyramidBook**:
  ![3DPyramidBook](https://github.com/toniles/sierpinski-animations/assets/120176462/4d746898-b56c-44c3-b968-7a3c330a4ab9)

- **RareSquare**:
  ![RareSquare](https://github.com/toniles/sierpinski-animations/assets/120176462/c6b204fc-7934-49b8-ac65-ed3246c7560a)

## RareSquare Explanation

This script elegantly animates the transformation of the Sierpinski triangle into a dynamic fractal tree. Drawing upon recursion and rotational geometry, underpinned by principles of dynamical systems, the script showcases a temporal evolution of the fractal form.

- **Recursive Algorithm**: Utilizes the `plot_sierpinski_fold` function for recursive midpoint computation and vertex-based rotations, incrementally crafting the fractal depth.
  
- **Geometric Rotations**: Employs the `rotate` function to animate the fractal transformation, applying linear algebra to manipulate rotation angles within a two-dimensional plane.

- **Animation Mechanics**: The `update_fold` function drives the animation, managing frame-by-frame progression and utilizing angular interpolation to simulate the fractal's folding from 120 degrees down to zero.

- **Visualization**: Leverages Matplotlib's `FuncAnimation` for the graphical rendering, orchestrating the fractal's evolution into a tree-like structure through a seamless visual loop.

- **Rendering**: Executes the `plt.show()` command to deliver the fractal animation to the screen, revealing the progressive stages of the Sierpinski triangle's metamorphosis into a three-dimensional fractal geometry.

The interplay of mathematical elegance and computational graphics offers viewers a dynamic exploration of fractal transformations.

**MeltingMountain**:
  ![MeltingMountain](https://github.com/toniles/sierpinski-animations/assets/120176462/103ee920-a2c4-4926-876b-2512aeab7711)

  **MeltingMountain with +2 on the fractal complexity**:

  ![sierpinski_colored_complexity_plus_2](https://github.com/toniles/sierpinski-animations/assets/120176462/8fafd792-f02b-4e91-be7c-a788447b78be)


## MeltingMountain Explanation

This Python script intertwines recursion and linear algebra to create the Sierpinski Triangle fractal, a self-replicating geometric pattern derived from a simple equilateral triangle. It showcases the emergence of complexity from simple rules.

- **Recursion and Iteration**: The `generar_sierpinski` function recursively generates the fractal structure, employing midpoint calculations to subdivide triangles, demonstrating a core concept of fractals in dynamical systems.

- **Affine Transformations**: It applies affine transformations to maintain the collinearity and proportional distances of points, highlighting the geometric invariance inherent in fractal transformations.

- **Color Palette Creation**: The `generar_colores_pastel` function generates a pastel color palette, utilizing vector operations to create visually appealing color schemes for the fractal.

- **Rotational Transformations**: Rotations are achieved through the `abrir_fractal` function, which uses matrix operations to pivot points around an axis, marrying linear algebra with trigonometry.

- **Vector Calculus in Motion**: Vector operations, including addition and scalar multiplication, facilitate the opening motion of the fractal, serving as a practical application of vector calculus in geometry.

- **Computational Optimization**: Optimized for performance, the script leverages NumPy for its efficient handling of arrays, enhancing computational operations for vertex manipulation and transformation.

This script not only produces a visual fractal phenomenon but also serves as an applied example of mathematical concepts in computational geometry and graphics, offering a dynamic view into the unfolding of fractal patterns.

