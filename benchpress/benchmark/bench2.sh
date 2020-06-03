for i in {1..2000}
do
	python3 lb_stripped++.py $i
done
echo "1/2"

for i in {1..2000}
do
	python3 lb_100.py $i
done
echo "2/2"