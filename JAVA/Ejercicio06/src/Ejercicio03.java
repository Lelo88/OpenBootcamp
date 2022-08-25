/*Crea un array bidimensional de enteros y recórrelo, mostrando la posición y el valor de cada elemento
en ambas dimensiones.*/

public class Ejercicio03 {
    public static void main(String[] args) {

        int[][] numerosInt = {{1,2,3},{4,5,6},{7,8,9}};

        for(int i=0; i< numerosInt.length;i++){
            for(int j=0;j < numerosInt[i].length;j++){
                System.out.println("Fila: " + (i+1) + " Columna: " + (j+1) + ": " + numerosInt[i][j]);
            }
        }
    }
}
