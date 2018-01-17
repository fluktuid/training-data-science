FILE="~/output.txt"
for i in `seq 10`;
do
bash a2.sh 10000 >> FILE
done

