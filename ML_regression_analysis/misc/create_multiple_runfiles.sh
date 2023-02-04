
for i in $(seq 65 1 336)
do
	sed 's/res-n/res-'"$i"'/g' res.conf > res-$i.namd
done
