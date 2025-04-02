from email.policy import default
from selenium import webdriver
import pytest
import os

driver = None

#### Registering command line options (Mandatory)
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome" , help= "Browser Selection"
    )

@pytest.fixture( scope="function" )
def browserInstance(request):
    #fetching cli option in fixture
    global driver  #using global variable driver
    browser_name = request.config.getoption("browser_name")   # command line option namer
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    #below yield works as a teardown statements
    driver.close()

# #this hook is automatically called when test fails and takes screenshot
# @pytest.hookimpl( hookwrapper=True )
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin( 'html' )
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr( report, 'extra', [] )

#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr( report, 'wasxfail' )
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
#             file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
#             print( "file name is " + file_name )
#             _capture_screenshot( file_name )
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append( pytest_html.extras.html( html ) )
#         report.extras = extra


# def _capture_screenshot(file_name):
#     driver.get_screenshot_as_file(file_name)

