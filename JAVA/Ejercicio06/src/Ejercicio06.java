/*Crea un ArrayList de tipo String, con 4 elementos.
Cópialo en una LinkedList. Recorre ambos mostrando únicamente el valor de cada elemento.*/

import java.util.ArrayList;
import java.util.LinkedList;

public class Ejercicio06 {
    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();
        lista.add("Mi");
        lista.add("nombre");
        lista.add("es");
        lista.add("Leandro");

        LinkedList<String> linkedlist = new LinkedList<>();

        for (int i = 0; i < lista.size(); i++) {
            linkedlist.add(i, lista.get(i));
        }

        System.out.println("Elementos del Array:");
        for (String elementos : lista) System.out.print(elementos + " ");

        System.out.println("\n\nElementos de la LinkedList:");
        for (String elementos : linkedlist) {
            System.out.print(elementos + " ");
        }
    }
}
