from selenium.webdriver.common.by import By

class BasePageLocators(object):
    LOADING_MASK = (By.CSS_SELECTOR, ".loading-mask")
    MANAGE_MENU = (By.ID, "menu-control")
    SAVE_EDITS_BUTTON = (By.XPATH, "//*[@id='content-container']/div/div[4]/div[3]/span/button[2]")

class CardPageLocators(BasePageLocators):
    def __init__(self):
        super(BasePageLocators, self).__init__()

class NodePageLocators(BasePageLocators):
    def __init__(self):
        super(BasePageLocators, self).__init__()

    NEW_NODE_BUTTON = (By.XPATH, "//*[@id='node-crud']/ul/li[2]/a")
    ADD_NODE_LIST_BUTTON = (By.XPATH, "//div[@id='branch-library']//div//div[@class='library-card']")
    ADD_BRANCH_LIST_BUTTON = (By.XPATH, "//*[@id='branch-library']/div/div[3]/div[3]")
    APPEND_BUTTON = (By.XPATH, "//*[@id='branch-append']")
    SELECTED_NODE_IN_LEFT_CONTAINER = (By.XPATH, "//*[@id='node-form']/div[1]/div/div[2]/div[2]/div/a")
    SAVE_EDITS_BUTTON = (By.XPATH, "//*[@id='content-container']/div/div[4]/div[3]/span/button[2]")
    NODE_ELEMENT_IN_SELECTED_NODE_IN_LEFT_CONTAINER = (By.XPATH, "//*[@id='node-listing']/div[2]/div[1]/div[2]/a")
    CARD_MANAGER_LINK = (By.XPATH, "//*[@id='card-manager']")

class GraphPageLocators(BasePageLocators):
    def __init__(self):
        super(BasePageLocators, self).__init__()

    ADD_BUTTON = (By.XPATH, "//button[@type='button']")
    STATUS_TAB = (By.XPATH, "//*[@id='xx-meta-tab']")
    ACTIVE_STATUS_BUTTON = (By.XPATH, "//*[@id='meta-card']/div/div/div[2]/div[1]/div/div[2]/div/label[1]")
    SAVE_EDITS_BUTTON = (By.XPATH, "//*[@id='content-container']/div/div[4]/div[3]/button[2]")

class MapWidgetPageLocators(BasePageLocators):
    def __init__(self):
        super(BasePageLocators, self).__init__()

    MAP_TOOLS_BUTTON = (By.ID, "map-tools")
    MAP_TOOLS_BASEMAPS = (By.XPATH, "//*[@id='map-widget-toolbar']/ul/li[1]")
    SATELLITE_BASE_MAP = (By.XPATH, "//*[@id='map-widget-basemaps']/div[3]")
    MAP_TOOLS_OVERLAYS = (By.ID, "btn-overlays")
    OVERLAY_LIBRARY_BUTTON = (By.XPATH, "//*[@id='overlays-panel']/div[1]/h4/i")
    OVERLAY_TO_ADD = (By.XPATH, "//*[@id='overlay-grid']/div[1]")
    ADDED_OVERLAYS = (By.CSS_SELECTOR, "#overlays-panel .map-widget-overlay-item .map-overlay-name")

class FormPageLocators(BasePageLocators):
    ADD_FORM_BUTTON = (By.XPATH, "//*[@id='report-image-grid']/div[1]")
    ADD_FORM_CARD_BUTTON = (By.XPATH, "//*[@id='report-image-grid']/div/div/div[4]/a")
    FORM_NAME_INPUT = (By.XPATH, "//*[@id='form-id-card']/div/div/div[2]/form/div[1]/div/div[2]/input")