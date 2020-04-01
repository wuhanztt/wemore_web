import page
from base.base import Base
from base.get_logger import GetLogger


#  获取log日志器
log = GetLogger().get_logger()


class PageLogin(Base):
    #  点击登录连接
    # def page_click_login_link(self):
    #     self.base_click(page.login_link)

    #  输入用户名方法
    def page_input_username(self, username):
        log.info("[page_login]对：{}元素输入用户名：{}操作".format(page.login_username, username))
        self.base_input(page.login_username, username)

    #  输入密码方法
    def page_input_password(self, password):
        log.info("[page_login]对：{}元素输入密码：{}操作".format(page.login_password, password))
        self.base_input(page.login_password, password)

    #  输入验证码方法
    # def page_input_verify_code(self, verify_code):
    #     self.base_input(page.login_verify_code, verify_code)

    #  点击login按钮方法
    def page_login_button(self):
        self.base_click(page.login_button)

    #  获取错误提示信息
    def page_get_error_text(self):
        return self.base_get_text(page.login_error_info)

    #  点击错误提示信息框_确定
    # def page_click_error_alret_ok(self):
    #     self.base_click(page.login_error_ok_button)

    #  判断是否登录成功
    def page_if_login_success(self):
        #  注意一定将元素的结果返回 True 存在
        return self.base_element_is_exist(page.login_success_info)

    #  点击头像退出
    def page_click_person_logout(self):
        self.base_find_element(page.login_person_logout)

    #  判断是否退出成功
    def page_if_logout_success(self):
        self.base_element_is_exist(page.login_button)

    #  组合业务方法
    def page_login(self, username, password):
        log.info("[page_login]正在执行登录操作，用户名:{},密码:{}".format(username, password))
        #  调用输入用户名方法
        self.page_input_username(username)
        #  调用输入密码方法
        self.page_input_password(password)
        #  调用点击login按钮方法
        self.page_login_button()

    #  组合登录业务方法 给登录成功后的admin平台其他操作依赖登录使用
    def page_login_success(self, username="ztt@qq.com", password="123456"):
        log.info("[page_login]正在执行组合登录业务方法，给登录成功后的admin平台其他操作依赖登录使用，用户名:{},密码:{}".format(username, password))
        #  调用输入用户名方法
        self.page_input_username(username)
        #  调用输入密码方法
        self.page_input_password(password)
        #  调用点击login按钮方法
        self.page_login_button()