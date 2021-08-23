import matplotlib.pyplot as pyplot

class Chart:
    def drawLineChart(self,x,y,title,xlabel,ylabel):
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)

        pyplot.plot(x,y,marker='o')
        pyplot.show()

    def drawBarChart(self,x,y,title,xlabel,ylabel):
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)

        pyplot.bar(x,y)
        pyplot.show()