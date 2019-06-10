from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests, json, sqlite3

# Отображение окна приложения из файла .ui
app = QtWidgets.QApplication([])
dlg = uic.loadUi("main_ui.ui")

url_itemsinstock = str('http://127.0.0.1:8000/api/ItemsInStock/')
url_itemforbuyer = str('http://127.0.0.1:8000/api/ItemForBuyer')
url_stock = str('http://127.0.0.1:8000/api/Stock')
url_seller = str('http://127.0.0.1:8000/api/Seler')
url_buyer = str('http://127.0.0.1:8000/api/Buyer')
url_item = str('http://127.0.0.1:8000/api/Item')



def reloadItems():
    dlg.list_item.clear()
    dlg.text_itemName.setText(str(''))
    dlg.text_ItemSeller.setText(str(''))
    dlg.text_itemAuthor.setText(str(''))
    dlg.text_itemISBN.setText(str(''))
    dlg.text_itemArticul.setText(str(''))
    dlg.text_itemPG.setText(str(''))
    dlg.text_itemYear.setText(str(''))
    dlg.text_itemPage.setText(str(''))
    dlg.text_itemType.setText(str(''))
    dlg.text_itemFormat.setText(str(''))
    dlg.text_itemMass.setText(str(''))
    dlg.text_itemPrise.setText(str(''))
    dlg.list_item.setSelectionMode(QAbstractItemView.SingleSelection)

    r = requests.get(str('http://127.0.0.1:8000/api/Item/'))

    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()
    data = r.json()

    for x in data:
        newItem = QListWidgetItem()
        newItem.setData(1, x)

        for y in sell:
            if y['id'] == x['seller']:
                newItem.setData(3, y)

        newItem.setText(newItem.data(1)['name'])
        # newItem.setText(newItem.data(2)['seller_name'])
        dlg.list_item.addItem(newItem)


def itemFocusChanged():
    for x in range(dlg.list_item.count()):
        itm = dlg.list_item.item(x)
        if itm.isSelected():
            if itm.data(1) is not None:
                dlg.text_itemName.setText(itm.data(1)['name'])
                dlg.text_ItemSeller.setText(itm.data(3)['seller_name'])
                dlg.text_itemAuthor.setText(itm.data(1)['avtor'])
                dlg.text_itemISBN.setText(itm.data(1)['ISBN'])
                dlg.text_itemArticul.setText(itm.data(1)['articul'])
                dlg.text_itemPG.setText(itm.data(1)['PG'])
                dlg.text_itemYear.setText(itm.data(1)['year'])
                dlg.text_itemPage.setText(str(itm.data(1)['pages']))
                dlg.text_itemType.setText(itm.data(1)['type'])
                dlg.text_itemFormat.setText(itm.data(1)['format'])
                dlg.text_itemMass.setText(str(itm.data(1)['mass']))
                dlg.text_itemPrise.setText(str(itm.data(1)['price']))
            else:
                dlg.text_itemName.setText(str(''))
                dlg.text_ItemSeller.setText(str(''))
                dlg.text_itemAuthor.setText(str(''))
                dlg.text_itemISBN.setText(str(''))
                dlg.text_itemArticul.setText(str(''))
                dlg.text_itemPG.setText(str(''))
                dlg.text_itemYear.setText(str(''))
                dlg.text_itemPage.setText(str(''))
                dlg.text_itemType.setText(str(''))
                dlg.text_itemFormat.setText(str(''))
                dlg.text_itemMass.setText(str(''))
                dlg.text_itemPrise.setText(str(''))


def createItem():
    newItem = QListWidgetItem()
    dlg.text_itemName.setText(str('Без имени'))
    newItem.setText(str('Без имени'))
    dlg.list_item.addItem(newItem)

def addItem():
    if not dlg.lineEdit_item.text() == "":
        dlg.listWidget.addItem(dlg.lineEdit_item.text())
    else:
        show_message('Ошибка!', 'невозможно добать пустое поле')

    dlg.lineEdit_item.setText("")


def saveItems():
    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()

    for x in range(dlg.list_item.count()):
        itm = dlg.list_item.item(x)
        # obj = itm.data(1)
        if itm.data(1) is None:
            obj = {}
            # obj['name'] = dlg.text_itemName.text()
            obj['name'] = dlg.text_itemName.text()
            # obj['seller_name'] = dlg.text_ItemSeller.text()

            flag = 1 == 3
            for y in sell:
                if y['seller_name'] == dlg.text_ItemSeller.text():
                    flag = 1==1
                    obj['seller'] = y['id']
            if not flag:
                QMessageBox.warning(dlg, "Ячейка", "Неверно указано имя издателя")
                return

            obj['avtor'] = dlg.text_itemAuthor.text()
            obj['ISBN'] = dlg.text_itemISBN.text()
            obj['articul'] = dlg.text_itemArticul.text()
            obj['PG'] = dlg.text_itemPG.text()
            obj['year'] = dlg.text_itemYear.text()
            obj['pages'] = dlg.text_itemPage.text()
            obj['type'] = dlg.text_itemType.text()
            obj['format'] = dlg.text_itemFormat.text()
            obj['mass'] = dlg.text_itemMass.text()
            obj['price'] = dlg.text_itemPrise.text()
            # my_objects.append(obj)
            r = requests.post('http://127.0.0.1:8000/api/Item/', data=obj)

def show_message(title="Error", message="Error"):
    QMessageBox.information(None, title, message)


dlg.btn_ItemReload.clicked.connect(reloadItems)
dlg.btn_ItemCreate.clicked.connect(createItem)
dlg.btn_itemSave.clicked.connect(saveItems)
dlg.list_item.itemSelectionChanged.connect(itemFocusChanged)
dlg.show()
app.exec()
