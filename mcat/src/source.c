#include "mcat.h"
#include <stdlib.h>
#include <string.h>

int verificarArgumentos(int qnt)
{
  if (qnt < 2)
  {
    printf("Número de argumentos inválidos!\n");
    return 1;
  }

  return 0;
}

int mostrarAjuda(char *flags[])
{
  if (strcmp(flags[1], "-h") == 0 || strcmp(flags[1], "--help") == 0)
  {
    printf("\n");
    printf("Uso: ./mcat [opção] ou [caminho_arquivo]\n");
    printf("Descrição: Lê arquivos pelo terminal\n");
    printf("Opções:\n");
    printf("\t-h, --help\tMostra ajuda");
    printf("\n");
    return 0;
  }
  return 1;
}

FILE *abrirArquivo(char *nomeArquivo[])
{
  FILE *arquivo = fopen(nomeArquivo[1], "r");

  arquivo = verificarArquivo(arquivo);

  return arquivo;
}

FILE *verificarArquivo(FILE *arquivo)
{
  if (arquivo == NULL)
  {
    printf("Erro ao abrir arquivo!\n");
    return NULL;
  }

  return arquivo;
}

void lerArquivo(FILE *arquivo)
{
  int caractere = 0;

  while((caractere = fgetc(arquivo)) != EOF)
  {
    putchar(caractere);
  }
  fecharArquivo(arquivo);
}

void fecharArquivo(FILE *arquivo)
{
  fclose(arquivo);
}