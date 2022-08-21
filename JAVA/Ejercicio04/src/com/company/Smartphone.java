package com.company;

public class Smartphone extends SmartDevice{
    String tipoAntena;
    int memoria;

    public Smartphone(String color, String marca, String modelo, double alto, double ancho, double espesor, String tipoAntena, int memoria) {
        super(color, marca, modelo, alto, ancho, espesor);
        this.tipoAntena = tipoAntena;
        this.memoria = memoria;
    }

    @Override
    public String toString() {
        return "Smartphone{" +
                "tipoAntena='" + tipoAntena + '\'' +
                ", memoria=" + memoria +
                ", color='" + color + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                ", alto=" + alto +
                ", ancho=" + ancho +
                ", espesor=" + espesor +
                '}';
    }
}
