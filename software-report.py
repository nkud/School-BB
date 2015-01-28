#! /usr/bin/python
# coding=utf-8

CATEGORY = [ '野菜', '肉', '魚', '果物', '乳製品', '冷凍食品', 'パン', '米', '弁当', 'その他' ]
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

# クラスの定義
class GroceryManager(object):
    def __init__(self):
        """ 初期化する """
        print '(食料品管理システム初期化)'
        self.category = CATEGORY
        self.grocery = GROCERY
    def stockWithNumber(num):
        """ 在庫を返す """
        return self.stock[num]
    def showTable(self):
        print '---------------- CATEGORY'
        n = 0
        for c in self.category:
            print '[%d] %s' % (n, c)
            n += 1
        print '----------------'


class SlipManager():
    def __init__(self):
        print '(伝票管理システム初期化)'

class ClientInfoManager():
    def __init__(self):
        print '(顧客管理システム初期化)'

# メイン
if __name__ == '__main__':
    print '( バーチャルマーケットシステム )'
    groceryManager = GroceryManager()
    slipManager = SlipManager()
    clientInfoManager = ClientInfoManager()

    groceryManager.showTable()