package com.company;

public class Smartwatch extends SmartDevice{

    String resistente;
    String bluetootht;


    public Smartwatch(String color, String marca, String modelo, double alto, double ancho, double espesor, String resistente, String bluetootht) {
        super(color, marca, modelo, alto, ancho, espesor);
        this.resistente = resistente;
        this.bluetootht = bluetootht;
    }

    @Override
    public String toString() {
        return "Smartwatch{" +
                "resistente='" + resistente + '\'' +
                ", bluetootht='" + bluetootht + '\'' +
                ", color='" + color + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                ", alto=" + alto +
                ", ancho=" + ancho +
                ", espesor=" + espesor +
                '}';
    }
}
