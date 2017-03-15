cd ..
echo "[INFO] Starting Lineblog crawler"
if [ "$#" -ne 3 ]
	then 
		echo "[ERROR] Invalid number of arguments."
		echo "[ERROR] Closing script."
else
	scrapy crawl lineblog -a name="$1" -a first="$2" -a last="$3" 
fi

cd scripts/