from selenium.webdriver.common.by import By

"""以下为项目服务器地址"""
URL = "http://test.thewemore.com:9000/login"

"""以下为登录模块涉及元素配置信息"""
#  登录连接，wemore没有
# login_link = By.PARTIAL_LINK_TEXT, "登录"
#  1.用户名
login_username = By.XPATH, "//*[@type='text']"
#  2.密码
login_password = By.XPATH, "//*[@type='password']"
#  验证码，wemore没有
# login_verify_code = By.CSS_SELECTOR, "#verify_code"
#  3.login按钮
login_button = By.XPATH, "//*[@type='button']"
#  4.错误提示信息
login_error_info = By.CSS_SELECTOR, ".ivu-message-notice-content-text"
#  错误提示框，确定按钮，wemore没有
# login_error_ok_button = By.CSS_SELECTOR, ".layui_layer_btn0"
#  5.登录成功信息HOME
login_success_info = By.CSS_SELECTOR, "[class='one_head_span']"
#  6.点击头像退出
login_person_logout = By.CSS_SELECTOR, ".person"

"""以下为cod setting模块涉及元素配置信息"""
#  1.All Catalogs页面
CodSetting_all_catalogs_page = By.CSS_SELECTOR, "li.template-submenu:nth-child(2) > div:nth-child(1) > i:nth-child(3)"
#  2.商品名称输入框
CodSetting_catalog_name_textbox = By.CSS_SELECTOR, "div.search_head:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(3)"
#  3.勾选框
CodSetting_checkbox = By.CSS_SELECTOR, "[type='checkbox']"
#  4.COD Setting按钮
CodSetting_COD_button = By.XPATH, "//*[text()='COD Setting']"
#  5.select下拉框
CodSetting_drop_list_select = By.CSS_SELECTOR, "div.v-transfer-dom:nth-child(14) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > form:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)"
#  6.下拉框Available选项
CodSetting_drop_list_Available = By.CSS_SELECTOR, "body > div:nth-child(14) > div.ivu-modal-wrap.vertical-center-modal > div > div > div.ivu-modal-body > div > div:nth-child(1) > form > div > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(1)"
#  7.COD charge输入框
CodSetting_COD_charge_textbox = By.CSS_SELECTOR, "div.v-transfer-dom:nth-child(14) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input:nth-child(2)"
#  8.Confirm按钮
CodSetting_confirm_button = By.CSS_SELECTOR, "div.v-transfer-dom:nth-child(14) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1)"
#  9.设置成功信息(获取不到)
CodSetting_success_info = By.CSS_SELECTOR, ".ivu-message-notice-content-text"
#  10.view跳转链接
CodSetting_view_jump_link = By.XPATH, "//*[@id='product_scroll']/div/div[2]/ul/li[11]/p"
#  11.COD Charge的文本值
CodSetting_view_cod_charge_text = By.CSS_SELECTOR, "div.basic:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1)"
