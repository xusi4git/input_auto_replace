import toml
from pathlib import Path

class Config():
    
    def __init__(self, file_url:str = None, auto_create: bool = True, auto_save: bool = True, auto_cover: bool = True) -> None:
        """初始化配置文件,文件不存在的话自动创建一个settings.toml

        Args:
            file_url (str): 文件地址
            auto_create(bool) : 不存在是是否自动创建
            auto_save (bool, optional): 自动保存
            auto_cover (bool, optional): 添加属性时,同属性覆盖或者抛出异常

        Raises:
            Exception: _description_
            Exception: _description_
        """
        # 存在 或者 创建
        if file_url is None:
            file_url = Path('.').joinpath('settings.toml')
        
        if Path(file_url).exists():
            pass
        else:
            if auto_create:
                Path(file_url).touch()
            else:
                raise Exception("File not found")
        
    
            
        # 初始化属性
        self.file_url = Path(file_url).absolute()
        self.auto_save = auto_save
        self.auto_cover = auto_cover
        # 读取配置
        try:
            self.settings = toml.load(file_url)
        except Exception as e:
            raise Exception(f"Error reading file:\t {e}")
        # 转化为属性 可以使用 config.name 的形式获取
        # 也可以使用 config.settings['name'] 的形式获取
        for key, value in self.settings.items():
            setattr(self, key, value)
        pass
    
    def set(self, key, value):
        try:
            if not self.auto_cover and self.settings.get(key):
                raise Exception("Already exists")
            self.settings[key] = value
            setattr(self, key, value)
            # 保存配置
            if self.auto_save:
                self.save()
        except Exception as e:
            raise Exception(f"Error adding value:\t {e}")
    
    def get(self, key: str, default=None) -> any:
        return self.settings.get(key,default)
    def save(self):
        # 保存配置
        with open(self.file_url, 'w') as f:
            toml.dump(self.settings, f)
    def _close(self):
        # 关闭时应当调用
        if self.auto_save:
            self.save()
    
    def _test(self):
        self.set("age",123)
        self.set("name","test")
        print(self.name,self.age)
    
    def __repr__(self) -> str:
        return f"<common_util.config.Config> {self.settings}"
        
    def items(self) -> dict[str, any]:
        return self.settings.items()
    
    def keys(self) -> dict[str, any]:
        return self.settings.keys()
    
    def values(self) -> dict[str, any]:
        return self.settings.values()
    
    
    def __getattr__(self,key:str):
        return None