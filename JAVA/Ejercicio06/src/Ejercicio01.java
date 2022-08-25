/*Dada la función:

 public static String reverse(String texto) { }

Escribe el código que devuelva una cadena al revés. Por ejemplo, la cadena "hola mundo", debe retornar "odnum aloh".*/

import java.util.Scanner;

public class Ejercicio01 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        String cadena;
        System.out.println("Ingrese un texto para dar vuelva: ");
        cadena = scanner.nextLine();

        System.out.println(reverse(cadena));
    }

    public static String reverse(String texto) {
        StringBuilder reves = new StringBuilder(texto);
        texto = reves.reverse().toString();
        return texto;
    }
}
