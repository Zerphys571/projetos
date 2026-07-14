#ifndef MCAT_H
#define MCAT_H

#include <stdio.h>

int verificarArgumentos(int qnt);

int mostrarAjuda(char *flags[]);

FILE *abrirArquivo(char *nomeArquivo[]);

FILE *verificarArquivo(FILE *arq);

void lerArquivo(FILE *arq);

void fecharArquivo(FILE *arq);

#endif