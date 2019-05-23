TorresDiego_final_15.pdf: datos.txt graficador.py
	python graficador.py

datos.txt: solucion.x
	./solucion.x

solucion.x: solucion.cpp
	g++ solucion.cpp -o solucion.x
	
clean:
	rm -rf *.pdf *.x *.txt