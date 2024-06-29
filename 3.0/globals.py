class Globals:
    '''
    全局游戏信息
    '''
    texture = None  # 贴图
    localmap = None  # 本地地图
    window = None  # 窗口
    player = None  # 玩家信息
    structures = []  # 结构
    animals = []  # 动物
    items = []  # 其他的item,比如掉落物
    chinesemap = {  # 转换成中文
        'name': '名称',
        'realname': '实际名称',
        'value': "价值",
        'weight': '重量',
        'head': '头',
        'body': '身体',
        'leg': '腿',
        'foot': '脚',
        'lefthand': '左手',
        'righthand': '右手',
        "attack": "攻击力",
        "defense": "防御力",
        'heart':"生命值",
        'money':"金币",
        'hungry':'饥饿度',
        'thirsty':"口渴度",
        "eat":"可恢复的饥饿度",
        "drink":"可恢复的口渴度"
    }
    englishmap = {  # 再转换成英文
        cn: en for en, cn in chinesemap.items()
    }
