for i in {1..3}
do
	python3 lb_stripped.py $i
done
echo "1/3"
for i in {1..3}
do
	python3 lb_100.py $i
done
echo "2/3"
for i in {1..3}
do
	python3 lb_500.py $i
done
echo "3/3"
