/*Crea un "Vector" del tipo de dato que prefieras, y añádele 5 elementos.
Elimina el 2o y 3er elemento y muestra el resultado final.*/

import java.util.Vector;

public class Ejercicio04 {
    public static void main(String[] args) {
        Vector vector = new Vector();
        vector.addElement(1);
        vector.addElement(2);
        vector.addElement(3);
        vector.addElement(4);

        System.out.println(vector);

        vector.remove(2);
        vector.remove(1);

        System.out.println(vector);
    }
}
