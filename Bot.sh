#!/bin/bash



while true; do
	if [ -f ".gitignore/NikeTwitterStrings.txt" ]; then
		mv .gitignore/NikeTwitterStrings.txt .gitignore/temp.txt	
	else
		cd NikeTwitter
		scrapy crawl --nolog Nike
		cd ..
		continue
	fi
	cd NikeTwitter
	#echo 'Crawling Nike...'
	scrapy crawl --nolog Nike
	#echo 'Done Crawling!'
	cd ..
	diff .gitignore/NikeTwitterStrings.txt .gitignore/temp.txt > /dev/null
	if [ $? -eq 1 ];then
		echo 'Nike Twitter page has been updated'
		exit 1
	fi
done
