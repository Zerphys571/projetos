clean:

	@echo "limpando objetos"
	rm -f ./bin/mcat ./obj/mcat.o
	@echo ""

tads:

	@echo "criando objetos"
	g++ -c ./src/source.c -I ./include/ -o ./obj/mcat.o
	@echo ""

exec:

	@echo "criando binário do programa"
	g++ ./app/main.c -I ./include/ ./obj/mcat.o -o ./bin/mcat
	@echo ""
	
all: clean tads exec