for i in {1..2000}
do
	python3 bench_versions/bench0.py $i
done

for i in {1..2000}
do
	python3 bench_versions/bench1.py $i
done