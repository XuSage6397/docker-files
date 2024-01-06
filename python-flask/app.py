from flask import Flask
import importlib
import pkgutil

app = Flask(__name__)

# 动态加载并注册所有 api 模块
for (_, name, _) in pkgutil.iter_modules(['api']):
    # 导入模块
    module = importlib.import_module(f'api.{name}')
    # 注册蓝图
    app.register_blueprint(getattr(module, name))