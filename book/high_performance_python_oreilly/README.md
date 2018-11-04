### Basic commands

#### Python:

cProfile is a module for profiling with -s param sorts result (cumulative sorts by running time), -o output_file for further analisys with python module pstats

```python -m cProfile -s cumulative python_file.py```

```python -m cProfile -o profile.stats python_file.py```

#### Linux:

Time module with verbose returns more precise result

```/bin/usr/time --verbose script-to-run```

### Line profiler

firs install line profiler
```pipenv install line_profiler```

Decorator @profile is added to __builtins__. 
Decorate a function. Now it is profiled line by line while you call script using kernprof.
usage:

```kernprof -lv python_script.py```
