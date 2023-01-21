import pkgutil


from creart import create
from graia.saya import Saya

saya = create(Saya)


class load_module():  # 加载模块
    def fun(path: str):
        try:
            with saya.module_context():
                for module_info in pkgutil.iter_modules([path]):
                    saya.require(f"{path}.{module_info.name}") # load moduels
                    print(f"Success Loaded {path}.{module_info.name}") # print Load moduels success status
        except Exception as Err:
            print(f"{Err} Load {path}.{module_info.name}") # print load moduels failed status

    fun("group_module") # load moduel
    fun("friend_module") # load moduel
    fun("Console")


if __name__ == "__main__":
    load_module() # Load Modyel
