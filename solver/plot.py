import matplotlib.pyplot as plt


class Plot(object):

    def __init__(self, image):
        # Let image fill the figure
        fig = plt.figure(frameon=False)
        ax = plt.Axes(fig, [0., 0., 1., .9])
        ax.set_axis_off()
        fig.add_axes(ax)

        self._current_image = ax.imshow(image, aspect="auto", animated=True)
        self.show_fittest(image, "Initial problem")

    def show_fittest(self, image, title):
        plt.suptitle(title, fontsize=20)
        self._current_image.set_data(image)
        plt.draw()

        # Give pyplot 0.1s to draw image
        plt.pause(0.1)
