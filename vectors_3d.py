import matplotlib.pyplot as plt
import numpy as np
from custom_3d_arrow import Arrows3D


class Vector:
    def __init__(self, x: float, y: float, z: float, *start_coordinates):
        """
        This is an instance of Vector class
        :param x: x component of the vector
        :param y: y component of the vector
        :param z: z component of the vector
        """
        self.x = x
        self.y = y
        self.z = z
        self.vector = np.array([self.x, self.y, self.z])
        if len(start_coordinates) == 0:
            self.x0 = 0
            self.y0 = 0
            self.z0 = 0
        else:
            self.x0 = start_coordinates[0]
            self.y0 = start_coordinates[1]
            self.z0 = start_coordinates[2]

class VectorProduct:
    def __init__(self, vector1, vector2):
        """
        This class calculates and shows the vector product of two Vector instances
        :param vector1: an instance of the Vector class
        :param vector2: an instance of the Vector class
        """
        self.vector1 = vector1
        self.vector2 = vector2

    def calculate(self):
        calculated_vector = np.cross(self.vector1.vector, self.vector2.vector)
        result = Vector(calculated_vector[0], calculated_vector[1], calculated_vector[2])
        return result

    def show_3D_plot(self):
        label_list = ['a vector', 'b vector', 'vector product a x b']
        graph = Graph([self.vector1, self.vector2, self.calculate()], label_list, '3D graph of vector product', set_aspect_equal=True)
        graph.show_graph()


class AddVectors:
    def __init__(self, vector1, vector2):
        """
        This class calculates and shows the sum of two Vector instances
        :param vector1: an instance of the Vector class
        :param vector2: an instance of the Vector class
        """
        self.vector1 = vector1
        self.vector2 = vector2

    def calculate(self):
        x = self.vector1.x + self.vector2.x
        y = self.vector1.y + self.vector2.y
        z = self.vector1.z + self.vector2.z
        return Vector(x, y, z)

    def show_3D_plot(self):
        vector3 = self.calculate()
        self.vector2.x0 = self.vector1.x
        self.vector2.y0 = self.vector1.y
        self.vector2.z0 = self.vector1.z
        self.vector2.x += self.vector1.x
        self.vector2.y += self.vector1.y
        self.vector2.z += self.vector1.z
        label_list = ['a vector', 'b vector', 'sum a + b']
        graph = Graph([self.vector1, self.vector2, vector3], label_list, '3D graph of vector sum')
        graph.show_graph()

class Graph:
    def __init__(self, vector_list, label_list, graph_title, set_aspect_equal=False):
        self.vector_list = vector_list.copy()
        self.label_list = label_list.copy()
        self.graph_title = graph_title
        self.set_aspect_equal = set_aspect_equal

    def show_graph(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x_min = min([v.x0 for v in self.vector_list]+[v.x for v in self.vector_list])
        x_max = max([v.x0 for v in self.vector_list]+[v.x for v in self.vector_list])
        y_min = min([v.y0 for v in self.vector_list]+[v.y for v in self.vector_list])
        y_max = max([v.y0 for v in self.vector_list]+[v.y for v in self.vector_list])
        z_min = min([v.z0 for v in self.vector_list]+[v.z for v in self.vector_list])
        z_max = max([v.z0 for v in self.vector_list]+[v.z for v in self.vector_list])
        color_list = ['r', 'b', 'g', 'y', 'm']
        l = len(color_list)
        for n, vector in enumerate(self.vector_list):
            arrow = Arrows3D(np.array([[vector.x, vector.y, vector.z]]), np.array([[vector.x0, vector.y0, vector.z0]]), ax=ax, label=self.label_list[n], color=color_list[n % l], linewidth=2)
            ax = arrow.ax
        ax.set_xlim([x_min, x_max])
        ax.set_ylim([y_min, y_max])
        ax.set_zlim([z_min, z_max])
        ax.set_xlabel('x', fontsize=24)
        ax.set_ylabel('y', fontsize=24)
        ax.set_zlabel('z', fontsize=24)
        plt.title(self.graph_title, fontsize=36)
        if self.set_aspect_equal:
            ax.set_aspect("equal")
        plt.legend(fontsize=24)
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')
        plt.show()


if __name__ == '__main__':
    v1 = Vector(-1, 1, -1)
    v2 = Vector(-5, 1, 2)
    # v3 = AddVectors(v1, v2)
    v3 = VectorProduct(v1, v2)
    # v3.calculate()
    v3.show_3D_plot()
