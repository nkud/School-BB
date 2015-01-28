#! /usr/bin/python
# coding=utf-8

### データ
# 商品のカテゴリー
CATEGORY = [ '野菜', '肉', '魚', '果物', '乳製品', '冷凍食品', 'パン', '米', '弁当', 'その他' ]

# 各カテゴリーの商品
GROCERY = [ 
[['Yasai1', '100yen', 'Mr.A', '0'],['Yasai2', '100yen', 'Mr.A', '0'],['Yasai3', '100yen', 'Mr.A', '0']],
[['Niku1', '100yen', 'Mr.A', '0'],['Niku2', '100yen', 'Mr.A', '0'],['Niku3', '100yen', 'Mr.A', '0']],
[['Sakana1', '100yen', 'Mr.A', '0'],['Sakana2', '100yen', 'Mr.A', '0'],['Sakana3', '100yen', 'Mr.A', '0']],
[['Kudamono1', '100yen', 'Mr.A', '0'],['Kudamono2', '100yen', 'Mr.A', '0'],['Kudamono3', '100yen', 'Mr.A', '0']],
[['Nyuseihin1', '100yen', 'Mr.A', '0'],['Nyuseihin2', '100yen', 'Mr.A', '0'],['Nyuseihin3', '100yen', 'Mr.A', '0']],
[['Reitou1', '100yen', 'Mr.A', '0'],['Reitou2', '100yen', 'Mr.A', '0'],['Reitou3', '100yen', 'Mr.A', '0']],
[['Pan1', '100yen', 'Mr.A', '0'],['Pan2', '100yen', 'Mr.A', '0'],['Pan3', '100yen', 'Mr.A', '0']],
[['Kome1', '100yen', 'Mr.A', '0'],['Kome2', '100yen', 'Mr.A', '0'],['Kome3', '100yen', 'Mr.A', '0']],
[['Bentou1', '100yen', 'Mr.A', '0'],['Bentou2', '100yen', 'Mr.A', '0'],['Bentou3', '100yen', 'Mr.A', '0']],
[['Sonota1', '100yen', 'Mr.A', '0'],['Sonota2', '100yen', 'Mr.A', '0'],['Sonota3', '100yen', 'Mr.A', '0']],
]

# 配送可能な地域
AREA = [ 'area-A', 'area-B', 'area-C']

### クラスの定義
# 食料品を管理するクラス
class GroceryManager(object):
    def __init__(self):
        """ 初期化する """
        self.category = CATEGORY
        self.grocery = GROCERY

    def showTable(self):
        """ 商品メニューを表示する """
        print '---------------- CATEGORY'
        n = 0
        for c in self.category:
            print '- [%d] %s' % (n, c)
            n += 1
        print '----------------'

    def showStockWithNumber(self, num):
        """ 在庫を表示する """
        groceries = self.grocery[num]
        for g in groceries:
            print '- [商品名] %s | [価格] %s | [生産者]　%s | [在庫量] %s' % (g[0], g[1], g[2], g[3])

# 伝票を管理するクラス
class SlipManager(object):
    def __init__(self):
        pass

# 顧客情報を管理するクラス
class ClientInfoManager(object):
    def __init__(self):
        self.client_data = []

    def appendNewClient(self, name, address, tel, mail):
        """ 新しい顧客を登録する """
        clientdata = [name, address, tel, mail]
        self.client_data.append(clientdata)

    def inputClientInformation(self):
        """ 氏名、住所、電話番号、メールアドレスを入力する """
        print ">>> 登録開始"
        name = ''
        address = ''
        tel = ''
        mail = ''
        while True:
            name = raw_input("[ name ] ")
            address = raw_input("[ address ] ")
            tel = raw_input("[ tel ] ")
            mail = raw_input("[ mail ] ")
            print '----------------'
            print('- 氏名: %s\n- 住所: %s\n- 電話番号: %s\n- E-mail: %s') % (name, address, tel, mail)
            print '----------------'
            ok = raw_input(">>> OK?(y/n) ")
            if ok == 'y':
                break
        self.appendNewClient(name, address, tel, mail)
        print ">>> 登録完了"

# 入出力を管理するクラス
class ViewController(object):
    def __init__(self):
        pass

# メイン
if __name__ == '__main__':
    print '( バーチャルマーケットシステム )'
    groceryManager = GroceryManager()
    slipManager = SlipManager()
    clientInfoManager = ClientInfoManager()

    groceryManager.showTable()
    groceryManager.showStockWithNumber(0)
    clientInfoManager.inputClientInformation()