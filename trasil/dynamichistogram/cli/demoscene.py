import numpy as np

class DemoScene:
    def __init__(self, *hists):
        self.hists = hists
        
        self._axs = []

    def add_dot(self, x):
        for h in self.hists:
            h.add(x)

    @property
    def axs(self):
        return self._axs

    @axs.setter
    def axs(self, axs):
        self._axs = axs

    def draw_scene(self):
        for ax in self.axs:
            ax.cla()
            #ax.set_ylim(0, 1)

        for h in self.hists:
            h.draw_hist(self.axs[0])
            h.draw_cdf(self.axs[1])

    def get_cdf_diff(self, a, b, m=100):
        x = np.linspace(a, b, m)

        y0 = self.hists[0].cdf(x)
        y1 = self.hists[1].cdf(x)

        return np.sum(np.square(y0 - y1))/m
