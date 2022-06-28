'''Profilerar modulen strobogrammatic1'''
import cProfile
import pstats
import strobogrammatic1
cProfile.run('strobogrammatic1.strobogrammatic(8)', 'restats1')
p = pstats.Stats('restats1')
p.sort_stats('cumulative').print_stats(20)
