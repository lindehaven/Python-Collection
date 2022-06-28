'''Profilerar modulen multi4'''
import cProfile
import pstats
import multi4

cProfile.run('multi4.print_table(1,99)', 'multi4_stats')
p = pstats.Stats('multi4_stats')
p.sort_stats('cumulative').print_stats(20)
