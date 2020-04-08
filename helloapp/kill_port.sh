port=8000

lsof -i:$port | awk '{if (NR>1){print $2}}' | xargs kill -9

