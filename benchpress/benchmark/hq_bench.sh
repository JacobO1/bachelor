for i in {1..3}
do
	python3 hq_stripped.py $i
done
echo "1/3"
for i in {1..3}
do
	python3 hq_100.py $i
done
echo "2/3"
for i in {1..3}
do
	python3 hq_1000.py $i
done
echo "3/3"
