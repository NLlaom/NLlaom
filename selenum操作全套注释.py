import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # xpath需要导入的库
from selenium.webdriver.common.action_chains import ActionChains  # 鼠标操作需要导入的库
from selenium.webdriver.common.keys import Keys  # 操作键盘需要导入的库
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 异常库

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)  # 执行完成不自动关闭浏览器
# prefs = {'profile.default_content_settings.popups': 0, # 0 禁止弹出窗口。
#          'download.default_directory': '/Users/soar/victor'} #设置下载路径。
# option.add_experimental_option('prefs', prefs) #需要通过 add_experimental_option 添加 prefs 参数。
# option.add_argument('--headless')  # 添加无头浏览器
# option.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                     'Chrome/94.0.4606.71 Safari/537.36')  # 无头浏览器需要添加 ua
# option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 去除浏览器识别   (自动化正在控制浏览器)
web = webdriver.Chrome(options=option)
# web.get('https://www.csdn.net/')

# web.get('https://blog.csdn.net/qq_43965708')  # 在原来的标签上打开
# web.back() #后退
# web.forward() #前进
# js = "window.open('https://blog.csdn.net/qq_43965708')"  # 新标签中打开
# web.execute_script(js)  # 新标签中打开
# web.set_window_size(800, 800)  # 设置窗口
# web.refresh()  # 刷新页面
# windows = web.window_handles  # 获取打开的多个窗口句柄
# web.switch_to.window(windows[-1])  # 切换到当前最新打开的窗口
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys('python')  # send_keys()	模拟输入指定内容
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').clear()  # clear()	清除文本内容
# attribute = web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').get_attribute('id')  # get_attribute()	获取标签属性值
# size = web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').size  # size	返回元素的尺寸
# text = web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').text  # text	返回元素文本
'''
drag_and_drop()	拖动
move_to_element()	鼠标悬停
perform()'''
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys('python')
# web.find_element(By.XPATH, '//*[@id="toolbar-search-button"]').click() #click()  单击左键
# web.find_element(By.XPATH, '//*[@id="toolbar-search-button"]')double_click() #double_click() 双击
# button = web.find_element(By.XPATH, '//*[@id="toolbar-search-button"]')  # 定位搜索按钮
# ActionChains(web).context_click(button).perform()  # 鼠标右键点击搜索按钮
# ActionChains(web).double_click(button).perform()  # 鼠标执行双击动作
# source = web.find_element(By.XPATH, 'xxx')  # 定位要拖动的元素
# target = web.find_element(By.XPATH, 'xxx')  # 定位目标元素
# ActionChains(web).drag_and_drop_by_offset(source, source.s, )  # 执行拖动动作
# move_to_element = web.find_element(By.XPATH, '//*[@id="csdn-toolbar"]/div/div/div[3]/div/div[3]/a')  # 定位历史栏
# ActionChains(web).move_to_element(move_to_element).perform() # 悬停至收藏标签处
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys('python')  # 定位输入框并输入文本
# web.find_element(By.XPATH, '//*[@id="toolbar-search-button"]').send_keys(Keys.ENTER) # 模拟回车键进行跳转（输入内容后）
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys(Keys.BACK_SPACE)  # 使用 Backspace 来删除一个字符
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys(Keys.CONTROL, 'a')  # Ctrl + A 全选输入框中内容
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys(Keys.CONTROL, 'c')  # Ctrl + C 复制输入框中内容
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys(Keys.CONTROL, 'v')  # Ctrl + V 粘贴输入框中内容
# web.find_element(By.XPATH, '//*[@id="toolbar-search-input"]').send_keys(Keys.CONTROL, 'x')  # Ctrl + X 粘贴输入框中内容
'''Keys.F1	F1键
Keys.SPACE	空格
Keys.TAB	Tab键
Keys.ESCAPE	ESC键
Keys.ALT	Alt键
Keys.SHIFT	Shift键
Keys.ARROW_DOWN	向下箭头
Keys.ARROW_LEFT	向左箭头
Keys.ARROW_RIGHT	向右箭头
Keys.ARROW_UP	向上箭头'''
# element = WebDriverWait(driver=web, timeout=5, poll_frequency=0.5).until(
#     EC.presence_of_element_located((By.ID, 'kw')), message='超时啦！'
# ) # 显示等待
# web.implicitly_wait(5)  # 隐示等待时间5秒

'''
find_elements 的用法
all = web.find_elements(By.XPATH,'//div[@data-v-0045335f]/div/a')
    for i in all:
        a = i.text
        print(a)'''
# web.find_element(By.XPATH,
#                  '//*[@id="floor-www-index_558"]/div/div[3]/div[1]/div[2]/div[1]/div[2]/div/div[1]/a[1]').click()
# print(web.current_window_handle)  # 当前窗口
# web.switch_to.window(web.window_handles[-1])  # 切换窗口操作

'''很多页面也会用带 frame/iframe 表单嵌套，对于这种内嵌的页面 selenium 是无法直接定位的，
需要使用 switch_to.frame() 方法将当前操作的对象切换成 frame/iframe 内嵌的页面。

switch_to.frame() 默认可以用的 id 或 name 属性直接定位，但如果 iframe 没有 id 或 name ，
这时就需要使用 xpath 进行定位。下面先写一个包含 iframe 的页面做测试用。
from selenium import webdriver
from pathlib import Path


driver = webdriver.Chrome()
# 读取本地html文件
driver.get('file:///' + str(Path(Path.cwd(), 'iframe测试.html')))

# 1.通过id定位
driver.switch_to.frame('CSDN_info')
# 2.通过name定位
# driver.switch_to.frame('Dream丶Killer')
# 通过xpath定位
# 3.iframe_label = driver.find_element_by_xpath('/html/body/iframe')
# driver.switch_to.frame(iframe_label)

driver.find_element_by_xpath('//*[@id="csdn-toolbar"]/div/div/div[1]/div/a/img').click()

'''
web.get('https://bot.sannysoft.com/')
# web.find_element(By.ID, 'alert').click()
# alert = web.switch_to.alert  # 弹出框
# cookie = web.get_cookies()  # 获取cookies
# js = 'window.scrollTo(0,500);'  # 滑动滚动条
# web.execute_script(js)  # 执行
# a = web.current_url  # 获取当前页面URL
'''# 获取当前页面url
driver.current_url

# 获取当前html源码
driver.page_source

# 获取当前页面标题
driver.title

# 获取浏览器名称(chrome)
driver.name

# 对页面进行截图，返回二进制数据
driver.get_screenshot_as_png()

# 设置浏览器尺寸
driver.get_window_size()

# 获取浏览器尺寸，位置
driver.get_window_rect()

# 获取浏览器位置(左上角)
driver.get_window_position()

# 设置浏览器尺寸
driver.set_window_size(width=1000, height=600)

# 设置浏览器位置(左上角)
driver.set_window_position(x=500, y=600)

# 设置浏览器的尺寸，位置
driver.set_window_rect(x=200, y=400, width=1000, height=600)
'''

# with open('stealth.min.js') as f:
#     js = f.read()
#
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": js
# })    # 通过 stealth.min.js 的隐藏，可以看到这次使用无头浏览器特征基本都以隐藏，已经十分接近人工打开浏览器了。
# 解决特征识别.因为服务器识别到的selenium的特征。使用该两行代码更改了特征，即可以顺利通过识别
# script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
# web.execute_script(script)

