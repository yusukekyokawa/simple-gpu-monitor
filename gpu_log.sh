date=$(date +%Y-%m%d-%H%M%S)

nvidia-smi --query-gpu=index,timestamp,pstate,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv -l 1 | tee "${date}.csv"