for i in {1..1}
do
	python3 lb_stripped.py $i
done
echo "1/5"

for i in {1..1}
do
	python3 lb_modules.py $i
done
echo "2/5"

for i in {1..1}
do
	python3 lb_stripped++.py $i
done
echo "3/5"

for i in {1..1}
do
	python3 lb_100.py $i
done
echo "4/5"

for i in {1..1}
do
	python3 lb_500.py $i
done
echo "5/5"