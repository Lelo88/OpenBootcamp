package com.company;

public class SmartDevice {
    String color;
    String marca;
    String modelo;
    double alto;
    double ancho;
    double espesor;

    public SmartDevice(String color, String marca, String modelo, double alto, double ancho, double espesor) {
        this.color = color;
        this.marca = marca;
        this.modelo = modelo;
        this.alto = alto;
        this.ancho = ancho;
    }

    @Override
    public String toString() {
        return "SmartDevice{" +
                "color='" + color + '\'' +
                ", marca='" + marca + '\'' +
                ", modelo='" + modelo + '\'' +
                ", alto=" + alto +
                ", ancho=" + ancho +
                ", espesor=" + espesor +
                '}';
    }
}
