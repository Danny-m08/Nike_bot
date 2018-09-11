#!/bin/bash


echo 'Bot is running'
while [ 1 ]; do
	

	cp .gitignore/NikeTwitterStrings.txt .gitignore/temp.txt
	#echo 'Crawling NikeStore Twitter'
	cd NikeTwitter && scrapy crawl --nolog Nike && cd ..
	#echo 'Done Crawling'


	
	#cd NikeTwitter
	#echo 'Crawling Nike...'
	#scrapy crawl --nolog Nike
	#echo 'Done Crawling!'
	#cd ..
	diff .gitignore/NikeTwitterStrings.txt .gitignore/temp.txt > /dev/null
	
	if [ $? -eq 1 ];then
		echo 'Nike Twitter page has been updated'
		rm .gitignore/temp.txt
		date
		exit 1
	fi
	let i++
done

rm .gitignore/temp.txt
exit 0
