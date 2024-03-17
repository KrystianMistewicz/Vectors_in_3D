import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyArrow
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


class Arrows3D:
    def __init__(self, ends, starts=None, ax=None, label=None, color='b', linewidth=2):
        """3D plot of multiple arrows
        Args:
            ends (ndarray): (N, 3) size array of arrow end coordinates
            starts (ndarray): (N, 3) size array of arrow start coordinates.
                Assume start position of (0, 0, 0) if not given
            ax (Axes3DSubplot): existing axes to add to
            label (str): legend label to apply to this group of arrows
            kwargs (dict): additional arrow properties
        """
        self.ends = ends
        self.starts = starts
        self.ax = ax
        self.label = label
        self.color = color
        self.linewidth = linewidth
        if self.starts is None:
            self.starts = np.zeros_like(ends)
        assert self.starts.shape == self.ends.shape, "`starts` and `ends` shape must match"
        assert len(self.ends.shape) == 2 and self.ends.shape[1] == 3, \
            "`starts` and `ends` must be shape (N, 3)"
        # create new axes if none given
        if self.ax is None:
            self.ax = plt.figure().add_subplot(111, projection='3d')
        arrow_prop_dict = dict(mutation_scale=20, arrowstyle='-|>', color=self.color, shrinkA=0, shrinkB=0, linewidth=self.linewidth)
        for ind, (s, e) in enumerate(np.stack((self.starts, self.ends), axis=1)):
            a = Arrow3D(
                [s[0], e[0]], [s[1], e[1]], [s[2], e[2]],
                # only give label to first arrow
                label=self.label,
                **arrow_prop_dict
            )
            self.ax.add_artist(a)
        # store starts/ends on the axes for setting the limits
        self.ax.points = np.vstack((starts, ends, getattr(self.ax, 'points', np.empty((0, 3)))))
        self.ax.set_xlim3d(self.ax.points[:, 0].min(), self.ax.points[:, 0].max())
        self.ax.set_ylim3d(self.ax.points[:, 1].min(), self.ax.points[:, 1].max())
        self.ax.set_zlim3d(self.ax.points[:, 2].min(), self.ax.points[:, 2].max())

if __name__ == '__main__':
    ax = Arrows3D(np.array([[1, 2, 3]]), np.array([[4, 4, 4]]), label='Foo')
    # ax = arrows3d(np.random.normal(size=(5, 3)), label='Foo')
    # ax = arrows3d(np.random.normal(size=(5, 3)), ax=ax, color='r',label='Bar')
    # print(np.random.normal(size=(5, 3)))
    plt.legend()
    plt.show()