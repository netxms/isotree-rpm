.PHONY: all clean

all:
	docker run --cap-add=SYS_ADMIN -it --rm -v ${PWD}/cache:/var/cache/mock -v ${PWD}:/drone/src -v ${PWD}/result:/result ghcr.io/netxms/builder-rpm:latest

dist:
	git clone --recursive https://github.com/netxms/isotree isotree-0.6.1
	tar zcf SOURCES/isotree-0.6.1.tar.gz isotree-0.6.1
	rm -rf isotree-0.6.1

clean:
	rm -rf result/*
