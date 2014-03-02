gallery:
	ls *.JPG | xargs -n1 sh -c 'convert $0 -resize 800 $0'
