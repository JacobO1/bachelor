for i in {1..1}
do
	python3 sw_stripped.py $i
done
echo "1/5"

for i in {1..1}
do
	python3 sw_modules.py $i
done
echo "2/5"

for i in {1..1}
do
	python3 sw_stripped++.py $i
done
echo "3/5"

for i in {1..1}
do
	python3 sw_100.py $i
done
echo "4/5"

for i in {1..1}
do
	python3 sw_500.py $i
done
echo "5/5"