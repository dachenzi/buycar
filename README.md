# 购物车
###### 数据结构 ######
    goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
    ......
    ]

### 功能要求 ###
###### 基础要求 ######
- [x] 1. 启动程序后，输入用户名密码后，让用户输入工资，然后打印商品列表
- [x] 2. 允许用户根据商品编号购买商品
- [x] 3. 用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
- [x] 4. 可随时退出，退出时，打印已购买商品和余额
- [x] 5. 在用户使用过程中， 关键输出，如`余额`，`商品已加入购物车`等消息，需`高亮显示`

###### 扩展需求 ######
- [x] 1. 用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
- [x] 2. 允许查询之前的消费记录


### 程序说明 ###
###### 目录结构 ######
- bin: 可执行程序
- conf: 配置文件
- data: 用户历史记录存放目录
- db: 数据文件
    - user_db: 用户帐户文件(以用户名.db命名)
- libs：依赖库文件
- logs：日志存放目录

###### 运行 #######
python3 bin/main()

###### 用户 #######
用户初始密码为123456,当balance为None时，需要用户输入salsay!