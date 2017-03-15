cd ..
echo "[INFO] Starting Instagram crawler"
if [ "$#" -ne 1 ]
	then 
		echo "[ERROR] Invalid number of arguments."
		echo "[ERROR] Closing script."
else
	scrapy crawl instagram -a name="$1"
fi

cd scripts/