from PeachRank.RankGraph import Page_Rank

__author__ = 'nina'

def main():

    rank = Page_Rank()
    rank.initial_rank()
    rank.do_it()


if __name__ == '__main__':
    main()



#            d01    d02    d03    d04    d05    d06    d07    d08    diff
# step: 0 [0.1250 0.1250 0.1250 0.1250 0.1250 0.1250 0.1250 0.1250]
# step: 1 [0.1102 0.1201 0.1201 0.2388 0.1102 0.1398 0.1398 0.0211] 0.2870
# step: 2 [0.1225 0.1289 0.1289 0.2053 0.1225 0.1416 0.1416 0.0088] 0.0917
# step: 3 [0.1173 0.1254 0.1254 0.2237 0.1173 0.1418 0.1418 0.0073] 0.0375
