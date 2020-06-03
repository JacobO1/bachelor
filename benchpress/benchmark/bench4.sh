for i in {1..2000}
do
	python3 sw_modules.py $i
done
echo "1/2"

for i in {1..2000}
do
	python3 sw_stripped++.py $i
done
echo "2/2"