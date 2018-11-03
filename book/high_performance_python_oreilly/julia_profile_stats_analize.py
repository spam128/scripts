#stats get by command
#python -m cProfile -o profile.stats julia_set.py
import pstats
p = pstats.Stats("profile.stats")
p.sort_stats("cumulative")
p.print_stats()
p.print_callers()

