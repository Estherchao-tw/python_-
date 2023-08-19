# Python | Create a digital clock using Tkinter

Tkinter 用於創建各種 GUI（圖形用戶界面）應用程序。

GUI 基本知識可以往這邊簡單看一下操作: [PyAutoGUI](爬蟲/GUI/PyAutoGUI.py)

我們將學習如何使用 Tkinter 創建數字時鐘。

> 先決條件：
>
>  Python 函數 
>
> Tkinter 基礎知識（標籤小部件） 
>
> 時間模塊(time module)

使用 Tkinter 中的 Label 小部件和時間模塊： 在下面的應用程序中，我們將使用標籤小部件，並且還將使用時間模塊，我們將用它來檢索系統時間。 下面是實現：

```
![demo](爬蟲/Tkinter_basic/demo.mp4)
```

Method:

1. 定義產生不同時區時間的函式

   - dt.timedelta(時間差):取得我們的時區(+8)。

   - specify the tz argument to a valid time zone object

2. 創建視窗
3. 在視窗中創建字串string 
   1. 創建要顯示的國家名稱(4個國家)
   2. 國家名稱:使用串列生成式，產生一個內容包含四個 tk 文字變數的串列
4. 定義顯示時間的函式
   1. 取得定義時間
   2. 國家時間:設定文字變數，要放進arr變數 converts to tk文字變數string
5. 利用迴圈跑4次，在視窗中顯示地區與時間
6. 顯示時間，並且重複運行