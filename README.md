# Semantic-segmentation
## The pixel-wise classification projects

### Label tool: Labelme  
在電腦上安裝圖片標註工具labelme 的方法：  
1. ios 系統：  
（注意需先於 電腦上安裝 python，打開電腦之終端機，並依序輸入以下內容...）  
  pip install pyqt 或 brew install pyqt #pyqt 也可以為: pyqt5  
  pip install labelme me #下載結束  
  或使用套件管理工具 brew 下載...  
  brew install wkentaro/labelme/labelme  
  brew cask install wkentaro/labelme/labelme (下載結束)  
  
2. windows 系統：  
  (一樣須於 anaconda 內 安裝 python)  
  先安裝 anaconda 並在 anaconda prompt 內依序輸入以下內容...  
  for python2:  
  conda create --name=labelme python=2.7  
  source activate labelme  
  conda install pyqt  
  pip install labelme  
  #if you'd like to use the latest version. run below:  
  pip install git+https://github.com/wkentaro/labelme.git  
  for python3:  
  conda create --name=labelme python=3.6  
  source activate labelme  
  pip install pyqt5 #pyqt5 can be installed via pip on python3  
  pip install labelme  
  
安裝完畢後直接於 mac 之終端機或 anconda prompt內輸入 labelme 即可開啟 labelme  

### 以下的連結附有使用Deeplabv3+模型訓練前，用來處理資料集的相關檔案...  
* https://drive.google.com/open?id=14iVgd1fDy7KBt52Mrsr0O7oC8-1IQi-_  
  連結包含以下四個檔案:  
  converting.py  
  getPic.py  
  getGT.py  
  get.py  
  
以下對這四個檔案做些簡單的說明：  
* converting.py:  
  在使用labelme完成label後，會生成一個包含 [原圖、label色塊圖、label_overlay圖、以及另外兩個資料] 的json檔  
  該檔案的目的是為了解壓出json檔裡面的東西(一個json以一個directory儲存)  
  該檔案的引數有兩個，分別是: (json檔所在的path, 存放json解壓縮後內容物資料夾的path)  

* getPic.py:  
  該檔案用於提取所有json檔解壓後，其資料夾中的[原圖]  
  該檔案的引數只有一個: (存放json解壓縮後內容物資料夾的path)  
  
* getGT.py:  
  該檔案用於提取所有json檔解壓後，其資料夾中的[label色塊圖]  
  該檔案的引數只有一個: (存放json解壓縮後內容物資料夾的path)  
  
* get.py:  
  該檔案用於提取label色塊圖資料夾內的所有檔名(依序紀錄每張圖片名稱，不含format的部分)  
  該檔案的引數有兩個，分別是: (label 色塊圖檔所在資料夾的path, 欲存放色塊圖檔名冊的path)  
  
### 完成上述階段後，接下來需建立資料夾，名稱可任意，用於存放所有訓練資料...  
* Dataall-  
    +image  
    +mask  
    +index  
    +tfrecord  

在Dataall資料夾底下共有4個資料夾，其存放的內容分別是...  
* image: 放入所有原圖  
* mask: 放入所有色塊圖  
* index: 放入3個txt檔，分別是...  
  train.txt: 所有用來作為訓練集的照片名稱  
  trainval.txt: 作為validation用的照片名稱  
  val.txt: 作為test用的照片名稱  
  
### 接下來，要在電腦上安裝Deeplab相關檔案(均在以下連結中):  
* https://github.com/tensorflow/models/tree/master/research/deeplab  
  也可將這個project的所有內容載入本機儲存庫中，在終端打上...  
  git clone https://github.com/tensorflow/models.git
