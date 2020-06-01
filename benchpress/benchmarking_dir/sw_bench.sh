for i in {1..3}
do
	python3 sw_stripped.py $i
done
echo "1/3"
for i in {1..3}
do
	python3 sw_100.py $i
done
echo "2/3"
for i in {1..3}
do
	python3 sw_500.py $i
done
echo "3/3"
