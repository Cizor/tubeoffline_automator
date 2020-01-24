from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


def form_urls_and_download():
    url_list = list()
    for i in range(7, 10):
        url_list.append(f"https://www.thewatchcartoononline.tv/black-clover-episode-{i}-english-dubbed")
    for i in url_list:
        get_vid(i)


def get_vid(url):
    options = webdriver.ChromeOptions()
    options.add_argument("download.default_directory=C:/Users/yourc/OneDrive/Desktop/block-clover-episodes")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.tubeoffline.com/download-WatchCartoonOnline-videos.php")
    inputUrl = driver.find_elements_by_id("video")
    inputUrl[0].send_keys(url)
    inputUrl[0].send_keys(Keys.ENTER)
    time.sleep(3)
    anchor = driver.find_elements_by_partial_link_text('wcostream')
    time.sleep(3)
    driver.get(anchor[0].get_property('href'))
    time.sleep(3)
    driver.execute_script("function test(){var openWindow=window.open('');var url=window.document.URL.toString();var src=document.documentElement.innerHTML;var note='book';form=document.createElement('form');form.setAttribute('method','POST');form.setAttribute('action','https://www.tubeoffline.com/downloadFrom.php');form.setAttribute('onsubmit','Submit.disabled = true;return true;');srcPlaceholder=document.createElement('input');srcPlaceholder.setAttribute('name','src');srcPlaceholder.setAttribute('type','hidden');srcPlaceholder.setAttribute('value',src);form.appendChild(srcPlaceholder);urlPlaceholder=document.createElement('input');urlPlaceholder.setAttribute('name','url');urlPlaceholder.setAttribute('type','hidden');urlPlaceholder.setAttribute('value',url);form.appendChild(urlPlaceholder);notePlaceholder=document.createElement('input');notePlaceholder.setAttribute('name','note');notePlaceholder.setAttribute('type','hidden');notePlaceholder.setAttribute('value',note);form.appendChild(notePlaceholder);divPlaceholder=document.createElement('div');divPlaceholder.setAttribute('name','label');divPlaceholder.setAttribute('type','div');divPlaceholder.style.textAlign='center';divPlaceholder.style.fontWeight='bold';divPlaceholder.style.fontSize='18px';divPlaceholder.style.fontFamily='arial';divPlaceholder.innerHTML='<br><br>Click%20the%20below%20button%20to%20Continue.<br>If%20your%20download%20does%20not%20work,%20please%20send%20feedback%20so%20we%20fix%20it%20for%20you.<br><br>';form.appendChild(divPlaceholder);btn=document.createElement('input');btn.setAttribute('name','Submit');btn.setAttribute('type','submit');btn.setAttribute('value','Go%20To%20TubeOffline%20download%20page%20>>');btn.style.fontSize='24px';btn.style.fontWeight='bold';btn.style.color='#FA8507';btn.style.width='600px';btn.style.height='100px';btn.style.display='table';btn.style.margin='0 auto';btn.setAttribute('onclick',\"this.value='Converting Video, Please wait...'\");form.appendChild(btn);openWindow.document.body.appendChild(form)}; test();")
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    submit = driver.find_elements_by_name('Submit')
    submit[0].send_keys(Keys.ENTER)
    time.sleep(3)
    anchor = driver.find_elements_by_partial_link_text('wcostream')
    driver.get(anchor[0].get_property('href'))
    time.sleep(3)
    element = driver.find_elements_by_xpath("//*[contains(@id, 'video-js_html5_api')]")
    webdriver.ActionChains(driver).move_to_element(element[0]).click(element[0]).perform()
    time.sleep(10)
    webdriver.ActionChains(driver).move_to_element(element[0]).context_click(element[0]).perform()
    pyautogui.typewrite(['down','down','down','down','enter'])
    time.sleep(2)
    pyautogui.write(url[37:-15])
    time.sleep(2)
    pyautogui.typewrite(['enter'])
    print('END')


form_urls_and_download()