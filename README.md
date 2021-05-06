# fio-random-experiments
Experiments using fio randomization
See also: https://www.n0derunner.com/2021/05/understanding-fio-norandommap-and-randrepeat-parameters/

Usage
```
cd fio/no-randommap_no-randrepeat
fio rr-no_randommap-no_randrepeat.fio --write_iolog=iolog-3.out
python3 ../r.py iolog-3.out > xy3.out
gnuplot
gnuplot> plot "xy3.out" using 2:3 with points pointtype 5
```
