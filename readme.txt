晓猛笔记
一、项目介绍
接口文档：
https://wiki.prometheanjira.com/display/PANM/API+Documents

1.运行项目要在python2.7 上
2.修改项目路径下的venv->lib->orig-prefix.txt 内容为本电脑安装的python 解释器的路径
3.选择File->settings->Python Interpreter->选择当前在项目内部的虚拟环境，
内部虚拟环境已经安装了依赖包ndlib-3.3.16 ，

2.pip install rsa
  pip install ddt

3.对应的运行计划地址是
https://bamboo.prometheanjira.com/browse/RL-LSAD-431

4.启动项目的命令python runner.py case_xq_test1(这个是运行开发环境的用例)
5、修改看看

api-auto-test-script1
api_call      都是相关接口，一个页面的多个接口每一个接口一个方法，里面有url、参数、payload等相关信息
--base
---txt_opera  一些接口使用的公共类，如登录后把cookie、token等一些数据写到txt文件当中，后续方法需要使用的时候再读取出来
              可以使用相对路径把读取AuthorizationToken数据存放到指定的位置

config
--production
---config
----cfg.ini    接口测试的URL地址配置[dev]    [sandbox]     [staging]   [pro]   [prod]
----gbl.py     设置页面encoding默认utf-8，把ini文件里面的url赋值给常量DEV SANDBOX STAGING

data_struct
---util.py     http状态码宏定义/数据宏定义/数据类公共方法

runner
--runner.py    取当前文件的绝对路径，run当前的文件
--suites.json  配置要运行的接口测试用例名字，用到的要运行的testcase里面写的测试用例代码

testcases      与前面api相关的接口调用



二、使用方法
1.例子：在api_call的xiaomeng里面先配置base去登录后获取到token值，
2.配置api接口内容
3.配置suite.json添加对应的要运行的测试用例
4.使用python runner.py XXX测试用例名字






