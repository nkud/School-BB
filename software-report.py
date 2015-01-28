#! /usr/bin/python
# coding=utf-8

# クラスの定義
class GroceryManager(object):
    def __init__(self):
        """ 初期化する """
        print '- 食料品管理システム初期化'
        self.grocery = [
                '野菜', '肉', '魚', '果物', '乳製品',
                '冷凍食品', 'パン', '米', '弁当', 'その他' ]
        self.stock = [ 0,1,2,3,4,5,6,7,8,9 ]
        self.producer = [ 'Mr.A','Mr.A','Mr.A','Mr.A','Mr.A',
                'Mr.B','Mr.B','Mr.B','Mr.B','Mr.B' ]
        self.price = [ 100,200,300,400,500,600,700,800,900,1000 ]
    def stockWithNumber(num):
        """ 在庫を返す """
        return self.stock[num]
    def showTable():
        n = 0
        for g in self.grocery:
            print 'name' % (g, self.producer[n], self.stock[n], self.price[n])

class SlipManager():
    def __init__(self):
        print '- 伝票管理システム初期化'

class ClientInfoManager():
    def __init__(self):
        print '- 顧客管理システム初期化'

# メイン
if __name__ == '__main__':
    print '( バーチャルマーケットシステム )'
    groceryManager = GroceryManager()
    slipManager = SlipManager()
    clientInfoManager = ClientInfoManager()
