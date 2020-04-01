from time import sleep

import page
from base.base import Base


class PageCodSetting(Base):
    #  打开All Catalogs页面
    def page_CodSetting_all_catalogs(self):
        self.base_open_all_catalogs(page.CodSetting_all_catalogs_page)

    #  输入商品名称
    def page_CodSetting_input_catalog_name(self, catalog_name):
        self.base_input(page.CodSetting_catalog_name_textbox, catalog_name)

    #  按Enter键进行搜索
    def page_CodSetting_enter_search(self):
        self.base_keyboard_enter(page.CodSetting_catalog_name_textbox)

    #  勾选搜索到的商品
    def page_CodSetting_search_click(self):
        self.base_click(page.CodSetting_checkbox)

    #  点击COD Setting按钮
    def page_CodSetting_click_COD_button(self):
        self.base_click(page.CodSetting_COD_button)

    #  点击select下拉框
    def page_CodSetting_click_select(self):
        self.base_click(page.CodSetting_drop_list_select)

    #  Support COD下拉框中选择Available
    def page_CodSetting_support(self):
        self.base_drop_list_select(page.CodSetting_drop_list_Available)

    #  COD charge输入框输入金额
    def page_CodSetting_input_charge(self, money):
        self.base_input(page.CodSetting_COD_charge_textbox, money)

    #  点击Confirm按钮
    def page_CodSetting_click_confirm(self):
        self.base_click(page.CodSetting_confirm_button)

    #  获取设置成功信息
    def page_CodSetting_success_info(self):
        self.base_get_text(page.CodSetting_success_info)

    #  获取view跳转链接中的cod charge文本值
    def page_CodSetting_view_cod_charge(self):
        sleep(3)
        self.base_click(page.CodSetting_view_jump_link)
        sleep(3)
        self.base_get_text(page.CodSetting_view_cod_charge_text)

    #  组合业务调用方法
    def page_CodSetting(self, catalog_name, money):
        sleep(3)
        self.page_CodSetting_input_catalog_name(catalog_name)
        sleep(3)
        self.page_CodSetting_enter_search()
        sleep(3)
        self.page_CodSetting_search_click()
        sleep(3)
        self.page_CodSetting_click_COD_button()
        sleep(3)
        self.page_CodSetting_click_select()
        sleep(3)
        self.page_CodSetting_support()
        sleep(3)
        self.page_CodSetting_input_charge(money)
        sleep(3)
        self.page_CodSetting_click_confirm()


