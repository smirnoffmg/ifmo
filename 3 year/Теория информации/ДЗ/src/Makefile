all: clean compile create archives c_density

compile: 
		g++ -o generator generator.cpp
		g++ -o compare compare.cpp
		g++ -o density density.cpp
		g++ -o entropy entropy.cpp

create:
		./generator

clean:
		rm -f *.out *.txt *.csv *.zip *.bz2 *.gz

archives: zip tar_gz tar_bz2

zip:
		zip random.zip random.txt

tar_gz:
		tar -zcvf random.tar.gz random.txt

tar_bz2:
		tar -jcvf random.tar.bz2 random.txt

gz:
		gunzip random.txt

c_density:
		./density random.txt > d_random.csv
		./density random.tar.gz > d_random_gz.csv
		./density random.tar.bz2 > d_random_bz2.csv		
		./density random.zip > d_random_zip.csv		