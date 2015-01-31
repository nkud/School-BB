#include <iostream>
using namespace std;

// 食料品を扱うクラス
class GroceryManager {
  public:
    GroceryManager() { cout << "Initialize Grocery Manager." << endl; }
  private:
    string groceries;
};

// 伝票を作成するクラス
class SlipManager {
  public:
    SlipManager() { cout << "Initialize Slip Manager" << endl; }
  private:
};

// 顧客の情報を管理するクラス
class ClientInfoManager {
  public:
    ClientInfoManager() { cout << "Initialize Client Manager" << endl; }
  private:
};

int main() {
  cout << "バーチャルマーケットシステム" << endl;
  GroceryManager groceryManage;
  SlipManager slipManager;
  ClientInfoManager clientManger;

  return 0;
}
