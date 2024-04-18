# 键盘监听且自动替换

## 功能

监听键盘输入,并自动替换为指定字符,直至按下预定退出键
类似于输入法中的自动替换.
可以替换的内容在 config.toml 中配置



## quick start

### 1、安装依赖

`pip install -r requirements.txt`

### 2、配置 config.toml

形式如:
```toml
dz_list = [
    ["key","value"],
]
# 该形式请参考 keyboard 库的按键
ESC_KEY = 'ctrl+alt+q'
```
### 3、运行

`python main.py`

### 4、输入内容

例如 `1-7` 加 `空格`

### 5、退出