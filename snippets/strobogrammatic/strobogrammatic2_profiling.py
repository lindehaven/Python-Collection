'''Profilerar modulen strobogrammatic2'''
import cProfile
import pstats
import strobogrammatic2
cProfile.run('strobogrammatic2.strobogrammatic(21,21)', 'restats2')
p = pstats.Stats('restats2')
p.sort_stats('cumulative').print_stats(20)
