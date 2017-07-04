#include <stdio.h>
#define UMBRAL 0.2
#define COEFICIENTE 0.3
void perceptron();
int gnet(int[],float[],int);
int comparacion(float);
void entrenamiento(int[],float[],int, int, int);

void perceptron(){
  int variables = 0, prueba = 1, salida;
  printf("*Ingrese la cantidad de variables: ");
  scanf("%d", &variables);
  int entradas[variables];
  float pesos[variables];
  for(int i = 0; i<variables;i++)
    pesos[i] = 0.5;
  printf("***Prueba numero %d\n",prueba);

  for(int i = 0; i < variables; i++){
    int entrada;
    printf("\n*Ingrese entrada numero %d:", i);
    scanf("%d", &entrada);
    entradas[i] = entrada;
  }

  printf("***Entradas: \n");
  for(int i = 0; i<variables;i++){
    printf("Entrada numero %d: %d\n", i, entradas[i]);
  }

  printf("\nIngrese salida:");
  scanf("%d",&salida);

  int resultado = gnet(entradas,pesos,variables);
  if(resultado == salida){
    printf("***Salida correcta \n");
  }
  else{
    printf("***Salida incorrecta\n ***Comenzando entrenamiento\n*\n*\n*");
    entrenamiento(entradas,pesos,salida, resultado,variables);
  }
}

void entrenamiento(int entradas[],float pesos[], int salida, int resultado,int variables){
    int entrenam = 0;  
  while(salida != resultado){
        entrenam++;
    printf("Entrenamiento numero %d\n",entrenam);
    for(int i = 0; i < variables; i++){
      float variacion = (resultado-salida) * entradas[i] * COEFICIENTE;
      pesos[i] = pesos[i] - variacion;
      printf("Peso nuevo %d: %.2f\n",i,pesos[i]);
    }
    resultado = gnet(entradas,pesos,variables);
  }
  printf("***Entrenamiento finalizado\n");
  printf("***Cantidad de Entrenamientos %d \n",entrenam);
  printf("RF: %d\n", resultado);
  printf("***Pesos nuevos: \n");
  for (int i = 0; i < variables; i++)
    printf("Peso %d: %.2f\n",i,pesos[i]);
}

int gnet(int entradas[], float pesos[],int variables){ 
  float resultado = 0;
  for(int i =  0; i<variables;i++){
    resultado += entradas[i]*pesos[i];
    printf("R: %.2f\n", resultado);
  } 
  resultado -= UMBRAL;
  printf("RF: %.2f\n",resultado );
  int comp = comparacion(resultado);
  return comp;
}

int comparacion(float resultado){
    if(resultado <= 0)
      return 0;
    return 1;
}

int main(){
  perceptron();
  return 0;
}

