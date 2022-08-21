package com.company;

public class SmartDeviceMain {
    public static void main(String[] args) {

        Smartphone celular = new Smartphone("negro", "motorola", "one fusion", 15.2, 8.7,1.1,"4g",128);
        System.out.println(celular);

        Smartwatch reloj = new Smartwatch("blanco", "lenovo","watchOne",20.1,5.0, 0.56,"resistente","Bluethoot 5.0");
        System.out.println(reloj);
    }
}
