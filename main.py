#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Funciones esenciales de sistema
import sys

# Librerias para graficas
import pandas as pd
import matplotlib.pyplot as plt

# Libreria para la UI de QT
from PyQt5 import uic, QtWidgets

# Archivo UI de QT
qtCreatorFile = "GUIC.ui"

# Inicializamos la interfaz
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Inicializamos los botones con las funciones correspondientes
        self.btncsv.clicked.connect(self.get_csv)
        self.btngraficar.clicked.connect(self.plot)
        self.btnestadisticas.clicked.connect(self.estadisticas)

    # Esta función abre el archivo CSV
    def get_csv(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file')
        if file_path != "":
            # Leemos el CSV que se seleccionó
            self.df = pd.read_csv(str(file_path))

            # Lista sin duplicados para productos
            productos = list(dict.fromkeys(self.df['nombre']))
            self.comboproducto.addItems(productos)
            
            # Lista sin duplicados para categorias
            categorias = list(dict.fromkeys(self.df['categoria']))
            self.combocategoria.addItems(categorias)
            
            # Lista sin duplicados para marcas
            marca = list(dict.fromkeys(self.df['marca']))
            self.combomarca.addItems(marca)

            # Lista sin duplicados para fecha
            fecha = list(dict.fromkeys(self.df['fecha']))
            self.combofecha_de.addItems(fecha)
            self.combofecha_a.addItems(fecha)

    # Dibujar grafica
    def plot(self):
        # Agarramos las columnas con los datos del CSV
        nombres = self.df['nombre']
        cantidades = self.df['cantidad']
        fechas = self.df['fecha']
        categorias = self.df['categoria']
        marcas = self.df['marca']

        # Listas temporales para filtros
        cant_filt = []
        fechas_filt = []

        # Checamos los criterios de los filtros y los agregamos a las listas filtradas
        for nombre, cantidad, marca, cat, fecha in zip(nombres, cantidades, marcas, categorias, fechas):
            if(nombre == str(self.comboproducto.currentText())
            and marca == str(self.combomarca.currentText())
            and cat == str(self.combocategoria.currentText())
            and pd.to_datetime(fecha) >= pd.to_datetime(str(self.combofecha_de.currentText()))
            and pd.to_datetime(fecha) <= pd.to_datetime(str(self.combofecha_a.currentText()))):
                cant_filt.append(cantidad)
                fechas_filt.append(fecha)
        
        # Dibujamos la gráfica con las listas filtradas
        plt.plot(fechas_filt, cant_filt)
        plt.show()
        # estad_st = "Estadisticas de col2: " + str(self.df['col2'].describe())
        # self.resultado.setText(estad_st)

    def estadisticas(self):
        print("Estadisticas")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
