public class EjercicioFuncion {
    public static void main(String[] args) {
         double precio = 124.51;
        System.out.println("El precio con el iva incluido es de : " + impuesto(precio));
    }

    public static double impuesto(double numero){
        double nuevoPrecio = (numero * 21)/100 + numero;
        return nuevoPrecio;
    }
}
