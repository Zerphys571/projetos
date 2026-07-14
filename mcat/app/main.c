#include "mcat.h"
#include <stdlib.h>

int
main(int argc, char *argv[])
{
  if (verificarArgumentos(argc))
    return EXIT_FAILURE;
  else if (!mostrarAjuda(argv))
    return EXIT_SUCCESS;
  else
  {
    FILE *arquivo = abrirArquivo(argv);

    lerArquivo(arquivo);
  }
  return EXIT_SUCCESS;
}