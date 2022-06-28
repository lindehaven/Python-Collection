'''Profilerar modulen fakultet'''
import cProfile
import pstats
import fakultet
cProfile.run('fakultet.fakultet(500)', 'restats')
p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(20)
