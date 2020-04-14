# PTT 貓版爬蟲
### 使用簡單的 python 程式進行爬蟲 (網站未經 JS 渲染)
對網站發出請求
```python
import requests
response = requests.get(url)
```
解析 HTML
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text,'html.parser')
```
