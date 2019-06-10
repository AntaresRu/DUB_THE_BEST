from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import requests

app = QtWidgets.QApplication([])
dlg = uic.loadUi("main_ui.ui")

url_itemsinstock = str('http://127.0.0.1:8000/api/ItemsInStock/')
url_itemforbuyer = str('http://127.0.0.1:8000/api/ItemForBuyer')
url_stock = str('http://127.0.0.1:8000/api/Stock')
url_seller = str('http://127.0.0.1:8000/api/Seller')
url_buyer = str('http://127.0.0.1:8000/api/Buyer')
url_item = str('http://127.0.0.1:8000/api/Item')


# ===================================ПОСТАВЩИК===================================#


def reloadSeller():
    dlg.list_seller.clear()
    dlg.text_sellerSeller.setText(str(''))
    dlg.text_sellerName.setText(str(''))
    dlg.text_sellerPhone.setText(str(''))
    dlg.text_sellerAdres.setText(str(''))
    dlg.text_sellerOGRN.setText(str(''))
    dlg.text_sellerINN.setText(str(''))
    dlg.list_seller.setSelectionMode(QAbstractItemView.SingleSelection)

    r = requests.get(str('http://127.0.0.1:8000/api/Seller/'))
    data = r.json()

    for x in data:
        newSeller = QListWidgetItem()
        newSeller.setData(1, x)
        newSeller.setText(str(newSeller.data(1)['seller']))
        dlg.list_seller.addItem(newSeller)


def sellerFocusChanged():
    for x in range(dlg.list_seller.count()):
        itm = dlg.list_seller.item(x)
        if itm.isSelected():
            if itm.data(1) is not None:
                dlg.text_sellerSeller.setText(itm.data(1)['seller'])
                dlg.text_sellerName.setText(itm.data(1)['seller_name'])
                dlg.text_sellerPhone.setText(itm.data(1)['phone'])
                dlg.text_sellerAdres.setText(itm.data(1)['adres'])
                dlg.text_sellerOGRN.setText(itm.data(1)['OGRN'])
                dlg.text_sellerINN.setText(itm.data(1)['INN'])
            else:
                dlg.text_sellerSeller.setText(str(''))
                dlg.text_sellerName.setText(str(''))
                dlg.text_sellerPhone.setText(str(''))
                dlg.text_sellerAdres.setText(str(''))
                dlg.text_sellerOGRN.setText(str(''))
                dlg.text_sellerINN.setText(str(''))


def createSeller():
    newSeller = QListWidgetItem()
    dlg.text_sellerName.setText(str('Без имени'))
    newSeller.setText(str('Без имени'))
    dlg.list_seller.addItem(newSeller)


def addSeller():
    if not dlg.lineEdit_seller.text() == "":
        dlg.listWidget.addItem(dlg.lineEdit_seller.text())
        show_message('Успех!', 'Новый поставщик добавлен!')
    else:
        show_message('Ошибка!', 'Невозможно добать пустое поле')

    dlg.lineEdit_seller.setText("")


def saveSeller():
    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()

    for x in range(dlg.list_seller.count()):
        itm = dlg.list_seller.item(x)
        if itm.data(1) is None:
            obj = {}

            obj['seller'] = dlg.text_sellerSeller.text()
            obj['seller_name'] = dlg.text_sellerName.text()
            obj['phone'] = dlg.text_sellerPhone.text()
            obj['adres'] = dlg.text_sellerAdres.text()
            obj['OGRN'] = dlg.text_sellerOGRN.text()
            obj['INN'] = dlg.text_sellerINN.text()

            r = requests.post('http://127.0.0.1:8000/api/Seller/', data=obj)


dlg.btn_sellerReload.clicked.connect(reloadSeller)
dlg.btn_sellerCreate.clicked.connect(createSeller)
dlg.btn_sellerSave.clicked.connect(saveSeller)
dlg.list_seller.itemSelectionChanged.connect(sellerFocusChanged)



# ===================================КНИГИ===================================#



def reloadSeller():
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
        show_message('Успех!', 'Новая книга добавлена')
    else:
        show_message('Ошибка!', 'Невозможно добать пустое поле')

    dlg.lineEdit_item.setText("")


def saveItems():
    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()

    for x in range(dlg.list_item.count()):
        itm = dlg.list_item.item(x)
        if itm.data(1) is None:
            obj = {}
            obj['name'] = dlg.text_itemName.text()
            flag = 1 == 3
            for y in sell:
                if y['seller_name'] == dlg.text_ItemSeller.text():
                    flag = 1==1
                    obj['seller'] = y['id']
            if not flag:
                QMessageBox.warning(dlg, "Ошибка", "Неверно указано имя издателя или такого издателя не существует!")
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
            r = requests.post('http://127.0.0.1:8000/api/Item/', data=obj)


dlg.btn_ItemReload.clicked.connect(reloadSeller)
dlg.btn_ItemCreate.clicked.connect(createItem)
dlg.btn_itemSave.clicked.connect(saveItems)
dlg.list_item.itemSelectionChanged.connect(itemFocusChanged)


# ===================================ПОКУПАТЕЛЬ===================================#
'''

def reloadSeller():
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
        show_message('Успех!', 'Новая книга добавлена')
    else:
        show_message('Ошибка!', 'Невозможно добать пустое поле')

    dlg.lineEdit_item.setText("")


def saveItems():
    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()

    for x in range(dlg.list_item.count()):
        itm = dlg.list_item.item(x)
        if itm.data(1) is None:
            obj = {}
            obj['name'] = dlg.text_itemName.text()
            flag = 1 == 3
            for y in sell:
                if y['seller_name'] == dlg.text_ItemSeller.text():
                    flag = 1==1
                    obj['seller'] = y['id']
            if not flag:
                QMessageBox.warning(dlg, "Ошибка", "Неверно указано имя издателя или такого издателя не существует!")
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
            r = requests.post('http://127.0.0.1:8000/api/Item/', data=obj)


dlg.btn_ItemReload.clicked.connect(reloadSeller)
dlg.btn_ItemCreate.clicked.connect(createItem)
dlg.btn_itemSave.clicked.connect(saveItems)
dlg.list_item.itemSelectionChanged.connect(itemFocusChanged)


# ===================================СКЛАД===================================#


def reloadSeller():
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
        show_message('Успех!', 'Новая книга добавлена')
    else:
        show_message('Ошибка!', 'Невозможно добать пустое поле')

    dlg.lineEdit_item.setText("")


def saveItems():
    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()

    for x in range(dlg.list_item.count()):
        itm = dlg.list_item.item(x)
        if itm.data(1) is None:
            obj = {}
            obj['name'] = dlg.text_itemName.text()
            flag = 1 == 3
            for y in sell:
                if y['seller_name'] == dlg.text_ItemSeller.text():
                    flag = 1==1
                    obj['seller'] = y['id']
            if not flag:
                QMessageBox.warning(dlg, "Ошибка", "Неверно указано имя издателя или такого издателя не существует!")
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
            r = requests.post('http://127.0.0.1:8000/api/Item/', data=obj)


dlg.btn_ItemReload.clicked.connect(reloadSeller)
dlg.btn_ItemCreate.clicked.connect(createItem)
dlg.btn_itemSave.clicked.connect(saveItems)
dlg.list_item.itemSelectionChanged.connect(itemFocusChanged)


# ===================================ПОКУПКИ===================================#


def reloadSeller():
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
        show_message('Успех!', 'Новая книга добавлена')
    else:
        show_message('Ошибка!', 'Невозможно добать пустое поле')

    dlg.lineEdit_item.setText("")


def saveItems():
    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()

    for x in range(dlg.list_item.count()):
        itm = dlg.list_item.item(x)
        if itm.data(1) is None:
            obj = {}
            obj['name'] = dlg.text_itemName.text()
            flag = 1 == 3
            for y in sell:
                if y['seller_name'] == dlg.text_ItemSeller.text():
                    flag = 1==1
                    obj['seller'] = y['id']
            if not flag:
                QMessageBox.warning(dlg, "Ошибка", "Неверно указано имя издателя или такого издателя не существует!")
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
            r = requests.post('http://127.0.0.1:8000/api/Item/', data=obj)


dlg.btn_ItemReload.clicked.connect(reloadSeller)
dlg.btn_ItemCreate.clicked.connect(createItem)
dlg.btn_itemSave.clicked.connect(saveItems)
dlg.list_item.itemSelectionChanged.connect(itemFocusChanged)


# ===================================ПОСТАВКИ===================================#


def reloadSeller():
    dlg.list_seller.clear()
    dlg.text_sellerseller.setText(str(''))
    dlg.text_sellersellerName.setText(str(''))
    dlg.text_sellerPhone.setText(str(''))
    dlg.text_sellerAdres.setText(str(''))
    dlg.text_sellerOGRN.setText(str(''))
    dlg.text_sellerINN.setText(str(''))
    dlg.list_seller.setSelectionMode(QAbstractItemView.SingleSelection)

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
        show_message('Успех!', 'Новая книга добавлена')
    else:
        show_message('Ошибка!', 'Невозможно добать пустое поле')

    dlg.lineEdit_item.setText("")


def saveItems():
    sell = requests.get(str('http://127.0.0.1:8000/api/Seller/')).json()

    for x in range(dlg.list_item.count()):
        itm = dlg.list_item.item(x)
        if itm.data(1) is None:
            obj = {}
            obj['name'] = dlg.text_itemName.text()
            flag = 1 == 3
            for y in sell:
                if y['seller_name'] == dlg.text_ItemSeller.text():
                    flag = 1==1
                    obj['seller'] = y['id']
            if not flag:
                QMessageBox.warning(dlg, "Ошибка", "Неверно указано имя издателя или такого издателя не существует!")
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
            r = requests.post('http://127.0.0.1:8000/api/Item/', data=obj)


dlg.btn_ItemReload.clicked.connect(reloadSeller)
dlg.btn_ItemCreate.clicked.connect(createItem)
dlg.btn_itemSave.clicked.connect(saveItems)
dlg.list_item.itemSelectionChanged.connect(itemFocusChanged)

'''


def show_message(title="Error", message="Error"):
    QMessageBox.information(None, title, message)


dlg.show()
app.exec()
