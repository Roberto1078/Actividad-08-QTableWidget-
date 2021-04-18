from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from administrador.particula import Particula
from administrador.particulas import Particulas


class Mainwindow(QMainWindow) :
    def __init__(self) :
        super(Mainwindow, self).__init__()
        self.particulas = Particulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.action_guardar.triggered.connect(self.guardar_archivo)
        self.ui.action_abrir.triggered.connect(self.abrir_archivo)
        #Tabla :
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_tabla_pushButton.clicked.connect(self.buscar_tabla)

    @Slot()
    def mostrar_tabla(self) :
        self.ui.tabla.setColumnCount(10)
        headers = ["ID","Origen X","Origen Y","Destino en x","Destino en y","Velocidad","Red","Green","Blue","Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        self.ui.tabla.setRowCount(len(self.particulas))
 
        row = 0
        for particula in self.particulas :
            id_widget = QTableWidgetItem(particula.id)
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(particula.velocidad)
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            red_blue = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, red_blue)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1

    @Slot()
    def buscar_tabla(self) :

        id = self.ui.buscar_tabla_lineEdit.text()
        encontrado = False

        for particula in self.particulas :

            if id == particula.id :

                self.ui.tabla.clear()
                self.ui.tabla.setColumnCount(10)
                headers = ["ID","Origen X","Origen Y","Destino en x","Destino en y","Velocidad","Red","Green","Blue","Distancia"]
                self.ui.tabla.setHorizontalHeaderLabels(headers)
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(particula.id)
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(particula.velocidad)
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                red_blue = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, red_blue)
                self.ui.tabla.setItem(0, 9, distancia_widget)
                encontrado = True
                break
        if not encontrado :
            QMessageBox.warning(
                self,
                'Atencion',
                f'La particula con id "{id}" no existe'
            )

    @Slot()
    def abrir_archivo(self) :
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.particulas.abrir(ubicacion) :
            QMessageBox.information(
                self,
                'Exito',
                'Se abrio el archivo ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo abrir el archivo'
            )

    @Slot()
    def guardar_archivo(self) :
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        
        if self.particulas.guardar(ubicacion) :
            QMessageBox.information(
                self,
                'Exito',
                'Guardado correctamente en ' + ubicacion
            )
        else :
            QMessageBox.critical(
                self,
                'Error',
                'No se pudo guardar el archivo'
            )

    @Slot()
    def click_mostrar(self) :
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar_final(self) :
        i_d = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(i_d, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self) :
        id = self.ui.id_lineEdit.text()
        origen_x  = self.ui.origen_x_spinBox.value()
        origen_y = self.ui.origen_y_spinBox.value()
        destino_x = self.ui.destino_x_spinBox.value()
        destino_y = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)