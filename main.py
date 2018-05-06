#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

# Importar aquí las librerías a utilizar
import pandas as pd
import matplotlib.pyplot as plt


from PyQt5 import uic, QtWidgets

qtCreatorFile = "GUIC.ui"  # Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Aquí van los botones
        self.btncsv.clicked.connect(self.get_csv)
        self.btngraficar.clicked.connect(self.plot)
        self.btnestadisticas.clicked.connect(self.estadisticas)

    # Aquí van las nuevas funciones
    # Esta función abre el archivo CSV
    def get_csv(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file','C:/Users/66909/Desktop')
        if file_path != "":
            print("Dirección", file_path)  # Opcional imprimir la dirección del archivo
            self.df = pd.read_csv(str(file_path), sep=';')
            self.comboproducto.additems(list(self.df.columns.values))
            self.combocategoria.additems(list(self.df.columns.values))
            self.combomarca.additems(list(self.df.columns.values))
            self.combofecha.additems(list(self.df.columns.values))

    def plot(self):
        x = self.df['nombre']
        y = self.df['cantidad']
        plt.plot(x, y)
        plt.show()
        #estad_st = "Estadisticas de col2: " + str(self.df['col2'].describe())
        self.resultado.setText(estad_st)

    def estadisticas(self):
        print("Estadisticas")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
