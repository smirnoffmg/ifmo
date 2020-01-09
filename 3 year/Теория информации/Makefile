all: clean compile create archives compare


compile: 
		g++ -o generator generator.cpp
		g++ -o compare compare.cpp

create:
		./generator

compare:
		./compare

clean:
		rm -f *.out *.txt *.zip *.bz2 *.gz

archives: zip tar_gz tar_bz2

zip:
		zip random.zip random.txt

tar_gz:
		tar -zcvf random.tar.gz random.txt

tar_bz2:
		tar -jcvf random.tar.bz2 random.txt

gz:
		gunzip random.txt