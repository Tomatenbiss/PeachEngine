from Frontier import Frontier

__author__ = 'nina'


class Page_Rank(object):

    def __init__(self):
        self.peach_decay = 0.95
        self.peach_abort = 0.04
        self.peach_delta = 0.0
        self.float_format = "{0:.4f}"
        self.difference = 1.0
        self.step = 0
        self.rank_graph = {}
        self.rank_graph_new = {}

        seed = [
            "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html",
            "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html",
            "http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html",
            ]

        frontier = Frontier(seed)
        frontier.peaching()

        self.link_graph = frontier.pageStructureDic()

        # self.link_graph = {'d01': ['d02', 'd03', 'd04'],
        #                    'd02': ['d03', 'd04', 'd01', 'd05'],
        #                    'd03': ['d04', 'd01', 'd02', 'd05'],
        #                    'd04': ['d01', 'd02', 'd03', 'd05'],
        #                    'd05': ['d04'],
        #                    'd06': ['d07'],
        #                    'd07': ['d06'],
        #                    'd08': []}

        self.backlinks = []

        self.peach_teleportation = 0.05 / len(self.link_graph)

    # calculate rank value for the first step 1/N
    # debugged
    def initial_rank(self):
        for x in self.link_graph:
            self.rank_graph[x] = 1.0 / len(self.link_graph)
            #self.rank_graph[x] = float(self.float_format.format(round((1.0 / len(self.link_graph)), 4)))
        for x in self.rank_graph:
            self.rank_graph_new[x] = float(self.float_format.format(0, 4))

    #get backlinks of a page and return a list with them
    #debugged
    def get_backlinks(self, key):
        self.backlinks = []
        for x in self.link_graph:
            if key in self.link_graph[x]:
                self.backlinks.append(x)


    #calculate backlinks Pj of Pi
    #debugged
    def part_one(self, key):
        part_one = 0
        self.get_backlinks(key)
        for x in self.backlinks:
            part_one += self.rank_graph[x] / len(self.link_graph[x])
        return part_one
        # return float(self.float_format.format(part_one, 4))


    #calculate Pj with zero outlinks
    #debugged
    def part_two(self):
        part_two = 0
        for x in self.link_graph:
            if len(self.link_graph[x]) == 0:
                part_two = self.rank_graph[x] / len(self.link_graph)
        return part_two
        # return float(self.float_format.format(part_two, 4))


    # put everything in formula and keep track of totals
    #debugged
    def calculate_rank(self, key):
        self.rank_graph_new[key] = self.peach_decay * (self.part_one(key) + self.part_two()) + self.peach_teleportation
        # self.rank_graph_new[key] = float(self.float_format.format((self.peach_decay * (self.part_one(key) + self.part_two()) + self.peach_teleportation), 4))
        return self.rank_graph_new

    #calculate the difference in delta
    #debugged
    def calculate_difference(self):
        self.peach_delta = 0.0
        for x in self.rank_graph:
            bla = abs(self.rank_graph[x] - self.rank_graph_new[x])
            # bla = float(self.float_format.format((abs(self.rank_graph[x] - self.rank_graph_new[x])), 4))
            self.peach_delta += bla
        return self.peach_delta

    #update the rank values for next step
    #debugged
    def update_ranks(self):
        for x in self.rank_graph:
            self.rank_graph[x] = self.rank_graph_new[x]

    #to print out a graph
    def print_rank(self, graph):
        for x in sorted(graph):
            #print "%s: %f" % (x, graph[x])
            print (x, ": ", (float(self.float_format.format(graph[x], 4))))


    #bring it all together
    def do_it(self):
        while self.difference >= self.peach_abort:
            print ("\n+++++++++ step:", self.step)
            for x in self.link_graph:
                self.calculate_rank(x)
                print ("OLD:")
                self.print_rank(self.rank_graph)
                print ("NEW:")
                self.print_rank(self.rank_graph_new)

            self.difference = self.calculate_difference()
            print (">>>>>>DIFFERENCE<<<")
            print ((float(self.float_format.format(self.difference, 4))))

            self.update_ranks()
            print ("NACH UP RANK")
            self.print_rank(self.rank_graph_new)

            self.step += 1
