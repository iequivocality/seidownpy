cd ..
echo "[INFO] Starting Single crawler"
if [ "$#" -ne 1 ]
	then 
		echo "[ERROR] Invalid number of arguments."
		echo "[ERROR] Closing script."
else
	scrapy crawl single -a link="$1"
fi

cd scripts/