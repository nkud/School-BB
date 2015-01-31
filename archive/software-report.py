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
        n = 0
        print ">>> (%s) 商品一覧を表示します。" % (CATEGORY[num])
        for g in groceries:
            print '- [%d] 商品名: %s | 価格: %s | 生産者:　%s | 在庫量: %s' % (n, g[0], g[1], g[2], g[3])
            n += 1

# 伝票を管理するクラス
class SlipManager(object):
    def __init__(self):
        pass
    def createReceptionCode(self, clientdata, categorynum, grocerynum):
        """ 受注コードを作成して返す """
        receptioncode = "%s-%s-%s-%s-%d-%d" % (clientdata[0], clientdata[1], clientdata[2], clientdata[3], categorynum, grocerynum)
        return receptioncode

# 顧客情報を管理するクラス
class ClientInfoManager(object):
    def __init__(self):
        self.client_data = []

    def appendNewClient(self, name, address, tel, mail):
        """ 新しい顧客を登録する """
        clientdata = [name, address, tel, mail]
        self.client_data.append(clientdata)

    def inputClientInformation(self):
        """ 氏名、住所、電話番号、メールアドレスを入力して、その情報を返す """
        name = ''
        address = ''
        tel = ''
        mail = ''
        while True:
            name = raw_input("[ name ] ")
            address = raw_input("[ address ] ")
            tel = raw_input("[ tel ] ")
            mail = raw_input("[ mail ] ")
            print '---------------- 確認画面'
            print('- 氏名: %s\n- 住所: %s\n- 電話番号: %s\n- E-mail: %s') % (name, address, tel, mail)
            print '----------------'
            ok = raw_input(">>> OK? (y/n) ")
            if ok == 'y':
                break
        return name, address, tel, mail

# 入出力を管理するクラス
class ViewController(object):
    def __init__(self):
        self.gm = GroceryManager()
        self.sm = SlipManager()
        self.cm = ClientInfoManager()

    def startOrder(self):
        # 顧客情報を入力する
        print ">>> 発注を開始します。"
        print ">>> 個人情報を入力してください"
        clientdata = self.cm.inputClientInformation()
        print ">>> 登録を完了しました。"
        self.cm.appendNewClient(clientdata[0], clientdata[1], clientdata[2], clientdata[3])

        # 商品メニューを表示したあと
        # 商品カテゴリーを入力する
        print ">>> 商品カテゴリーを選択してください。"
        self.gm.showTable()
        choicecategory = raw_input(">>> カテゴリーナンバー: ")
        print ">>> (%s) が選択されました。" % CATEGORY[int(choicecategory)]

        # 商品リストを表示したあと
        # 商品を選んでもらう
        print ">>> 商品を選択してください。"
        self.gm.showStockWithNumber(int(choicecategory))
        choicegrocery = raw_input(">>> 商品ナンバー: ")
        print ">>> (%s) が選択されました。" % GROCERY[int(choicecategory)][int(choicegrocery)][0]

        code = self.sm.createReceptionCode(clientdata, int(choicecategory), int(choicegrocery))
        print ">>> [受注コード] %s" % code

# メイン
if __name__ == '__main__':
    print '// ソフトウェア特論レポート'
    print '// バーチャルマーケットシステム'
    print '// 数理工学科　植田　尚克\n'
    vc = ViewController()

    # 発注を開始する
    vc.startOrder()