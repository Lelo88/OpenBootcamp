import java.util.Scanner;

public class Ejercicio08 {

    private static int Dividir(int a, int b) throws ArithmeticException {
        return a / b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese los numeros para dividir dividir: ");
        System.out.print("Numero 1: ");
        int a = scanner.nextInt();
        System.out.print("Numero 2: ");
        int b = scanner.nextInt();
        try {
            System.out.println("Resultado: " + Dividir(a, b));
        } catch (ArithmeticException e) {
            System.out.println("La division no puede realizarse");
        } finally {
            System.out.println("Fin del programa");
        }
    }
}
