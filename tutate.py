from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
from random import randint
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from os.path import basename
import time
from urllib.request import urlretrieve, urlopen
from cv2 import cv2
import imutils
import json

#
# user_log = {}
# user_log[] = []
# user_log[].append({
#
# })


driver = webdriver.Chrome()
# make sure path is correct on corresponding OS
driver = webdriver.Chrome(executable_path='C:/Users/gabe4/Desktop/WORK/furry-octo-funicular/IG/chrome_driver/chromedriver')

# class AppSettings:
#     def __init__(self, config_array):
#         self.users = []
#
#         self.config = config_array
#
#         self.three_letter_code = self.config[0]
#         self.logins_count = self.config[1]
#         self.max_daily_accounts_created = self.config[2]
#         self.leech_page_url = self.config[3]
#         self.share_post_page_url = self.config[4]
#         self.your_page_url = self.config[5]
#         self.add_friends_count = self.config[6]
#         self.suggest_likes_count = self.config[7]
#         self.clear_friend_requests_count = self.config[8]
#         self.sleep_time = self.config[9]
#         self.padding_time = self.config[10]
#         self.cap_wait_minutes = self.config[11]
#         self.creator_pics_count = self.config[12]
#
#         cloud_database.three_letter_code = self.three_letter_code
#
#         self.logins = cloud_database.get_logins()
#
#         for login in self.logins:
#             user = User()
#             user.name = login[0]
#             user.username = login[1]
#             user.password = login[2]
#             user.days = login[3]
#             self.users.append(user)

# class SeleniumServer:
#     def __init__(self):
#         self.fp = (r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\6i2jhdox.default')
#         self.opts = Options()
#         self.opts.profile = self.fp
#         self.ffprof = webdriver.FirefoxProfile()
#         self.ffprof.set_preference('dom.webnotifications.enabled', False)
#         self.ffprof.set_preference('dom.push.enabled', False)
#         self.capa = webdriver.DesiredCapabilities.FIREFOX.copy()
#         self.capa['marionette'] = False
#         self.capa['firefox_profile'] = self.ffprof.encoded
#         self.ec2conn = EC2Connection(aws_access_key, aws_secret_key)
#
#     def create_node(self):
#         # Returns the instance ID in string form
#         reservation = self.ec2conn.run_instances(
#             'ami-17689d01',
#             key_name='Second',
#             instance_type='t2.micro',
#             security_groups=['Node'])
#         instance_id = reservation.instances[0]
#         instance_id = str(instance_id)
#         instance_id = instance_id.replace("Instance:", "")
#         print("Created instance: " + instance_id)
#         return instance_id
#
#     def create_creator_instance(self):
#         # Returns the instance ID in string form
#         reservation = self.ec2conn.run_instances(
#             creator_instance_image_id,
#             key_name='Second',
#             instance_type='t2.micro',
#             security_groups=['Creator'])
#         instance_id = reservation.instances[0]
#         instance_id = str(instance_id)
#         instance_id = instance_id.replace("Instance:", "")
#         print("Created instance: " + instance_id)
#         return instance_id
#
#     def get_all_running_instances(self):
#         reservations = self.ec2conn.get_all_instances()
#         running_instances = [i.id for r in reservations for i in r.instances if (i.state == u'running')]
#         return running_instances
#
#     def get_all_running_leader_instances(self):
#         reservations = self.ec2conn.get_all_instances()
#         running_instances = [i.id for r in reservations for i in r.instances for g in i.groups if
#                              (i.state == u'running') and g.id == "sg-b7ec4bcb"]
#         return running_instances
#
#     def get_all_pending_creator_instances(self):
#         reservations = self.ec2conn.get_all_instances()
#         pending_instances = [i.id for r in reservations for i in r.instances for g in i.groups if
#                              (i.state == u'pending') and g.id == "sg-8604c6f9"]
#         return pending_instances
#
#     def get_all_running_creator_instances(self):
#         reservations = self.ec2conn.get_all_instances()
#         running_instances = [i.id for r in reservations for i in r.instances for g in i.groups if
#                              (i.state == u'running') and g.id == "sg-8604c6f9"]
#         return running_instances
#
#     def get_all_shutting_down_creator_instances(self):
#         reservations = self.ec2conn.get_all_instances()
#         shutting_down_instances = [i.id for r in reservations for i in r.instances for g in i.groups if
#                              (i.state == u'shutting-down') and g.id == "sg-8604c6f9"]
#         return shutting_down_instances
#
#     def get_current_instance(self):
#         reservations = self.ec2conn.get_all_instances()
#         my_ip = str(urlopen('http://ip.42.pl/raw').read())
#         my_ip = my_ip.replace("b\'", "").replace("\'", "")
#         current_instance = [i.id for r in reservations for i in r.instances if i.ip_address == my_ip]
#         return current_instance
#
#     def get_current_security_group(self):
#         reservations = self.ec2conn.get_all_instances()
#         my_ip = str(urlopen('http://ip.42.pl/raw').read())
#         my_ip = my_ip.replace("b\'", "").replace("\'", "")
#         security_groups = [i.groups for r in reservations for i in r.instances if i.ip_address == my_ip]
#         security_group_name = security_groups[0][0].name
#         return security_group_name
#
#     def get_all_stopped_instances(self):
#         minute_counter = 0
#         while minute_counter < 5:
#             reservations = self.ec2conn.get_all_instances()
#             stopping_instances = [i.id for r in reservations for i in r.instances if (i.state == u'stopping')]
#             if len(stopping_instances) > 0:
#                 print("Waiting for stopping instances...")
#                 time.sleep(30)
#                 minute_counter += 0.5
#             else:
#                 print("No stopping instances.")
#                 break
#         if minute_counter >= 5:
#             print("Instances were stopping for over 5 minutes.")
#         reservations = self.ec2conn.get_all_instances()
#         stopped_instances = [i.id for r in reservations for i in r.instances if (i.state == u'stopped')]
#         if len(stopped_instances) == 1:
#             print("Found one stopped instance. Continuing...")
#             return stopped_instances
#         elif len(stopped_instances) > 1:
#             print("Found too many stopped instances. Giving up.")
#             return False
#         else:
#             print("Found 0 stopped instances. Giving up.")
#             return False
#
#     def get_all_stopped_slave_instances(self):
#         minute_counter = 0
#         while minute_counter < 5:
#             reservations = self.ec2conn.get_all_instances()
#             stopping_instances = [i.id for r in reservations for i in r.instances for g in i.groups if
#                                   (i.state == u'stopping') and g.id == "sg-95ec4be9"]
#             if len(stopping_instances) > 0:
#                 print("Waiting for stopping instances...")
#                 time.sleep(30)
#                 minute_counter += 0.5
#             else:
#                 print("No stopping instances.")
#                 break
#         if minute_counter >= 5:
#             print("Instances were stopping for over 5 minutes.")
#         reservations = self.ec2conn.get_all_instances()
#         stopped_instances = [i.id for r in reservations for i in r.instances for g in i.groups if
#                              (i.state == u'stopped') and g.id == "sg-95ec4be9"]
#         if len(stopped_instances) == 1:
#             print("Found one stopped instance. Continuing...")
#             return stopped_instances
#         elif len(stopped_instances) > 1:
#             print("Found too many stopped instances. Giving up.")
#             return False
#         else:
#             print("Found 0 stopped instances. Giving up.")
#             return False
#
#     def get_running_instance_count(self):
#         reservations = self.ec2conn.get_all_instances()
#         hosts = [i.public_dns_name + ":8080" for r in reservations for i in r.instances if (i.state == u'running')]
#         return len(hosts)
#
#     def delete_all_inactive_volumes(self):
#         reservations = self.ec2conn.get_all_volumes()
#         for volume in reservations:
#             if volume.attach_data.instance_id is None:
#                 volume_id = str(volume).replace("Volume:", "")
#                 self.ec2conn.delete_volume(volume_id)
#
#     def delete_current_volume(self):
#         current_instance = str(selenium_server.get_current_instance())
#         current_instance = current_instance.replace("[\'", "").replace("\']", "")
#         reservations = self.ec2conn.get_all_volumes()
#         for volume in reservations:
#             if volume.attach_data.instance_id == current_instance:
#                 volume_id = str(volume).replace("Volume:", "")
#                 self.ec2conn.delete_volume(volume_id)
#
#     def find_node(self):
#
#         print("[Finding Node] Searching...")
#
#         loop_counter = 0
#         while self.get_running_instance_count() < 2:
#             print("[Finding Node] Seconds: " + str(loop_counter))
#             time.sleep(5)
#             loop_counter += 5
#             if loop_counter > 60:
#                 print("[Finding Node] No node has been found. Giving up.")
#                 return False
#
#         print("[Finding Node] Node Exists.")
#         return True
#
#     def connect_to_node(self):
#         connection_counter = 0
#         print("[Connecting to Node] Connecting...")
#         while connection_counter < 10:
#             time.sleep(60)
#             try:
#                 print("[Connecting to Node] Attempting connection...")
#                 driver = webdriver.Remote(command_executor="http://localhost:4445/wd/hub",
#                                           desired_capabilities=self.capa)
#                 print("[Connecting to Node] Successfully connected.")
#                 return driver
#             except:
#                 print("[Connecting to Node] Connection failed.")
#                 connection_counter += 1
#                 print("[Connecting to Node] Minutes: " + str(connection_counter))
#
#         print("[Connecting to Node] Connection failed. Giving up.")
#         return False
#
#     def terminate_an_instance(self, instance_id):
#         self.ec2conn.terminate_instances(instance_id)
#         return True
#
#     def do_stuff(self, driver):
#         # try:
#         #     print("Going to google.")
#         #     driver.get("https://google.com")
#         #     print("Successfully reached google.")
#         # except:
#         #     print("Failed to reach google.")
#         #     return False
#         # try:
#         #     print("Attempting to find element.")
#         #     driver.find_element_by_css_selector(".jsb")
#         #     print("Successfully found element.")
#         # except:
#         #     print("Failed to find element.")
#         #     return False
#         # try:
#         #     print("Attempting to close firefox.")
#         #     driver.close()
#         #     print("Successfully closed firefox.")
#         # except:
#         #     print("Failed to close firefox.")
#         #     return False
#         # return True
#
#         try:
#             print("Going to whatsmyip.org")
#             driver.get("https://whatsmyip.org")
#             print("Successfully reached whatsmyip.org")
#         except:
#             print("Failed to reach whatsmyip.org")
#             return False
#         try:
#             print("Attempting to find IP text element.")
#             ip_text = driver.find_element_by_id("ip").text
#             print("Successfully found IP text element.")
#             print("IP: " + ip_text)
#         except:
#             print("Failed to find IP text element.")
#             return False
#         try:
#             print("Attempting to close firefox.")
#             driver.close()
#             print("Successfully closed firefox.")
#         except:
#             print("Failed to close firefox.")
#             return False
#         return True
#
#     def magic_wrapper_rebirth(self):
#         i = 0
#         while i < 2:
#             node = self.create_node()
#             node_driver = self.connect_to_node()
#             if node_driver:
#                 self.do_stuff(node_driver)
#             self.terminate_an_instance(node)
#             i += 1
#
#         self.delete_all_inactive_volumes()
#
#         print("Finished.")
#
#     def magic_wrapper_recycle(self):
#         i = 0
#         while i < 3:
#             node = self.get_all_stopped_instances()
#             if node:
#                 self.ec2conn.start_instances(node)
#                 node_driver = self.connect_to_node()
#                 if node_driver:
#                     self.do_stuff(node_driver)
#                 self.ec2conn.stop_instances(node)
#             i += 1




# class SeleniumActions:
#     def __init__(self):
#         self.hit_max_outgoing_requests = False
#         self.likes_link_index = 1
#         self.friend_add_loop_index = 0
#         self.magic_friends_added = 0
#         self.magic_friends_invited = 0
#         self.magic_friend_count = 0
#         self.already_in_database_count = 0
#         self.page_likes_count = 0
#         self.post_id = ""
#         self.banned_user_count = 0

class SeleniumAPI:
    @staticmethod
    def wait_and_click_element(how, what, elem, driver_param=None, timeout=30, parent_element=None):
        seconds = 0
        if driver_param:
            while seconds < timeout:
                try:
                    driver_param.find_elements(by=how, value=what)[elem].click()
                    return True
                except:
                    time.sleep(1)
                    seconds += 1
            print("Could not click element for " + str(timeout) + " seconds.")
            return False
        else:
            if parent_element:
                while seconds < timeout:
                    try:
                        element_list = parent_element.find_elements(by=how, value=what)[elem].click()
                        return True
                    except:
                        time.sleep(1)
                        seconds += 1
                print("Could not click element for " + str(timeout) + " seconds.")
                return False
            else:
                while seconds < timeout:
                    try:
                        driver.find_elements(by=how, value=what)[elem].click()
                        return True
                    except:
                        time.sleep(1)
                        seconds += 1
                print("Could not click element for " + str(timeout) + " seconds.")
                return False

    @staticmethod
    def wait_and_send_keys_on_element(how, what, driver_param=None, timeout=30, parent_element=None,
                                      key=Keys.ENTER):
        seconds = 0
        if driver_param:
            while seconds < timeout:
                try:
                    driver_param.find_element(by=how, value=what).send_keys(key)
                    return True
                except:
                    time.sleep(1)
                    seconds += 1
            print("Could not send keys on element for " + str(timeout) + " seconds.")
            return False
        else:
            if parent_element:
                while seconds < timeout:
                    try:
                        element_list = parent_element.find_element(by=how, value=what).send_keys(key)
                        return True
                    except:
                        time.sleep(1)
                        seconds += 1
                print("Could not send keys on element for " + str(timeout) + " seconds.")
                return False
            else:
                while seconds < timeout:
                    try:
                        driver.find_element(by=how, value=what).send_keys(key)
                        return True
                    except:
                        time.sleep(1)
                        seconds += 1
                print("Could not send keys on element for " + str(timeout) + " seconds.")
                return False

    @staticmethod
    def wait_for_element(how, what, driver_param=None, timeout=30, parent_element=None):
        seconds = 0
        if driver_param:
            while seconds < timeout:
                try:
                    element = driver_param.find_element(by=how, value=what)
                    return element
                except:
                    time.sleep(1)
                    seconds += 1
            print("Could not find element for " + str(timeout) + " seconds.")
            return False
        else:
            if parent_element:
                while seconds < timeout:
                    try:
                        element = parent_element.find_element(by=how, value=what)
                        return element
                    except:
                        time.sleep(1)
                        seconds += 1
                print("Could not find element for " + str(timeout) + " seconds.")
                return False
            else:
                while seconds < timeout:
                    try:
                        element = driver.find_element(by=how, value=what)
                        return element
                    except:
                        time.sleep(1)
                        seconds += 1
                print("Could not find element for " + str(timeout) + " seconds.")
                return False

    @staticmethod
    def element_is_clickable(how, what, elem, driver_param=None, parent_element=None):
        if driver_param:
            try:
                driver_param.find_elements(by=how, value=what)[elem].click()
                return True
            except:
                return False
        else:
            if parent_element:
                try:
                    parent_element.find_elements(by=how, value=what)[elem].click()
                    return True
                except:
                    return False
            else:
                try:
                    driver.find_elements(by=how, value=what)[elem].click()
                    return True
                except:
                    return False

    @staticmethod
    def given_element_is_clickable(given_element):
        try:
            given_element.click()
            return True
        except:
            return False

    @staticmethod
    def element_is_present(how, what, driver_param=None):
        if driver_param:
            try:
                driver_param.find_element(by=how, value=what)
                return True
            except:
                return False
        else:
            try:
                driver.find_element(by=how, value=what)
                return True
            except:
                return False

    @staticmethod
    def element_is_present_multi(how, what, elem):
        try:
            spam_variable = driver.find_elements(by=how, value=what)[elem]
            return True
        except:
            return False

    @staticmethod
    def element_child_is_present(parent, how, what):
        try:
            parent.find_element(by=how, value=what)
            return True
        except:
            return False

# for config in cloud_database.get_config():
# app_settings = AppSettings(config)
# global_stats = GlobalStats()
selenium_actions = SeleniumActions()
selenium_api = SeleniumAPI()
# database_stuff = DatabaseStuff()
    # dialog = AppDialog()
    # dialog.show()
    # app.exec_()
# magic = Magic()

def get_time_from_image(image_filename):

    large_image = cv2.imread(image_filename)
    small_image = cv2.imread(r"C:/Users/gabe4/Desktop/WORK/furry-octo-funicular/IG/captcha/clock.png")

    # find clock x and y and scale
    scale = 1.00
    best_acc = 10000
    answer = []
    down = True
    upper_bound = 1.50
    lower_bound = 0.50
    # cannot suppress cv errors
    while scale < upper_bound:
        try:
            if down is True:
                scale -= 0.01
                if scale < lower_bound:
                    down = False
            else:
                scale += 0.01
            scaled_image = cv2.resize(small_image, (0,0), fx=scale, fy=scale)
            result = cv2.matchTemplate(scaled_image, large_image, cv2.TM_SQDIFF_NORMED)
            result2 = np.reshape(result, result.shape[0]*result.shape[1])
            sort = np.argsort(result2)
            accuracy = result2[sort[0]]
            if accuracy < best_acc:
                best_acc = accuracy
                (y, x) = np.unravel_index(sort[0], result.shape)
                trows, tcols = scaled_image.shape[:2]
                answer = [x, y, tcols, trows, scale, accuracy]
        except:
            pass
    # scale it to where it matches our clock example png
    rescale = answer[4]
    cropped_image = large_image[answer[1]:answer[1] + answer[3], answer[0]: answer[0] + answer[2]]
    scaled_cropped_image = cv2.resize(cropped_image, (0,0), fx=(1 / rescale), fy=(1 / rescale))
    # -1 if it is not found
    answer_hour = -1
    # this is a threshold for hour hand capture
    hour_acc = 180
    i = -1
    for angle in np.arange(0, 360, 30):
        i += 1
        rotated = imutils.rotate(scaled_cropped_image, angle)
        point = rotated[14, 34]
        if point[0] < 255:
            answer_minutes = i
            # dont record hour hand as minute hand
            continue
        hour_points = rotated[26:27, 34:39]
        total_darkness = 0
        for hour_point in hour_points[0]:
            total_darkness += hour_point[0]
        total_darkness_avg = total_darkness / len(hour_points[0])
        if total_darkness_avg < hour_acc:
            hour_acc = total_darkness_avg
            answer_hour = i
    # if hour was never found, it must be under the minute hand
    if answer_hour == -1:
        answer_hour = answer_minutes
    answer_minutes = answer_minutes * 5
    # 0 o clock = 12 o clock
    if answer_hour == 0:
        answer_hour = 12
    # stringify answer
    answer_hour = str(answer_hour)
    answer_minutes = str(answer_minutes)
    if len(answer_minutes) < 2:
        answer_minutes = "0" + answer_minutes
    if len(answer_hour) < 2:
        answer_hour = "0" + answer_hour
    time_answer = answer_hour + ":" + answer_minutes
    return time_answer

def wait():
    time.sleep(randint(6,10)/10)

def create_account(self):

    signup_first_name_xpath = ".//input[@class='inputtext _58mg _5dba _2ph-' and @aria-label='First name']"
    signup_last_name_xpath = ".//input[@class='inputtext _58mg _5dba _2ph-' and @aria-label='Last name']"
    signup_username_xpath = (".//input[contains(@class, 'inputtext _58mg _5dba _2ph-') "
                             "and @aria-label='Mobile number or email']")
    # signup_username_alternate_xpath = (".//input[@class='inputtext _58mg _5dba _2ph- focused' "
    #                          "and @aria-label='Mobile number or email']")
    signup_username_confirm_xpath = (".//input[contains(@class, 'inputtext _58mg _5dba _2ph-') "
                                     "and contains(@aria-label, 'Re-enter')]")
    signup_password_xpath = ".//input[@class='inputtext _58mg _5dba _2ph-' and @aria-label='New password']"
    signup_month_id = "month"
    signup_day_id = "day"
    signup_year_id = "year"
    signup_sex_female_xpath = ".//input[@name='sex' and @value='1']"
    # Confirm button can be "Sign Up" or "Create Account" so its better to use css
    signup_confirm_button_css = "._6j.mvm._6wk._6wl._58mi._3ma._6o._6v"
    signup_confirm_button_xpath = ".//button[text()='Create Account']"
    # Cant use the signup_confirm_button_css for this one since the old element still exists
    signup_captcha_confirm_button_xpath = ".//button[@id='u_0_n']"
    # Can use it now?
    signup_captcha_confirm_button_css = "._6j.mvm._6wk._6wl._58me._58mi._3ma._6o._6v"

    signup_find_your_friends_xpath = ".//span[text()='Find your friends']"
    fb_early_code_entry_check_xpath = ".//h2[text()='Enter the code from your email']"
    fb_early_code_entry_not_now_button_css = ".mls._42ft._4jy0._4jy4._517h._51sy"
    fb_early_code_entry_not_now_link_xpath = ".//a[text()='Not Now']"
    fb_needs_phone_verification_check_xpath = ".//div[text()='Use a phone to verify your account']"

    tuta_signup_email_xpath = ".//input[@id='mailAddress']"
    tuta_signup_password_xpath = ".//input[@id='newpassword']"
    tuta_signup_password_confirm_xpath = ".//input[@id='newpassword2']"
    tuta_signup_terms_checkbox_xpath = ".//input[@id='termsInput']"
    tuta_signup_age_checkbox_xpath = ".//input[@id='ageInput']"
    tuta_signup_confirm_button_xpath = ".//button[@class='single fontImage confirm' and @type='submit']"
    tuta_signup_captcha_textbox_xpath = ".//input[@id='captchaInput']"
    tuta_signup_captcha_image_xpath = ".//img[@id='captchaDisplay']"

    fb_signup_captcha_image_xpath = ".//img[@style='display:block;']"
    fb_signup_captcha_textbox_xpath = ".//input[@id='captcha_response']"

    tuta_signup_loading_alert_xpath = ".//h2[text()='Loading Tutanota...']"
    tuta_signup_creating_account_alert_xpath = ".//h2[text()='Account is being created ...']"

    tuta_signup_ip_ban_alert_message = "Registration is temporarily blocked"

    tuta_signup_ip_ban_alert_xpath = ".//div[contains(text(), '%s')]" % tuta_signup_ip_ban_alert_message

    tuta_fb_confirmation_number_xpath = ".//div[contains(text(), 'is your Facebook confirmation code')]"
    tuta_fb_confirmation_subject2_xpath = ".//div[contains(text(), 'Just one more step to get started')]"
    tuta_fb_confirmation_number2_xpath = ".//td[contains(@style, 'lucidagrande')]"

    fb_enter_code_xpath = ".//a[text()='Enter Code']"
    fb_code_textbox_xpath = ".//input[@name='code']"
    fb_code_confirm_button_css = "._42ft._4jy0.layerConfirm._2z1w.uiOverlayButton._4jy3._4jy1.selected._51sy"
    fb_code_confirm_button_xpath = ".//button[@type='submit']"
    "_42ft mls _4jy0 _4jy4 _4jy1 selected _51sy"
    fb_account_confirmed_xpath = ".//div[text()='Account Confirmed']"
    fb_account_confirmed_okay_button_xpath = ".//a[@data-testid='confirm_code_dialog_submit_close']"
    fb_account_confirmed_okay_button_css = "._42ft._42fu.layerCancel.uiOverlayButton.selected._42g-._42gy"
    fb_top_left_icon_css = "._2md"
    fb_find_friends_next_button_xpath = ".//a[text()='Next']"
    fb_find_friends_next_button_css = "._42ft._4jy0.rfloat._ohf._4jy4._517h._51sy"
    fb_find_friends_skip_button_xpath = ".//a[text()='Skip step']"
    fb_find_friends_skip_button_css = "._42ft._4jy0.layerConfirm.uiOverlayButton._4jy3._517h._51sy"
    fb_enter_mobile_number_button_css = "._42ft._42fu.selected._42g-"
    fb_phone_number_entry_textbox_css = ".inputtext"
    fb_phone_number_confirm_button_css = "._42ft._42fu.layerConfirm.uiOverlayButton.selected._42g-._42gy"
    fb_phone_code_entry_textbox_css = ".inputtext.mts"
    # You can reuse the confirm button for this one. The first one is "Continue" and this one is "Confirm", if need

    tuta_login_email_textbox_xpath = ".//input[@id='loginMailAddress']"
    tuta_login_password_textbox_xpath = ".//input[@id='loginPassphrase']"
    tuta_login_confirm_button_xpath = ".//button[@id='submitLogin']"

    first_names = ["Emily", "Emma", "Madison", "Abigail", "Olivia", "Isabella", "Hannah", "Samantha", "Ava",
                   "Ashley", "Sophia", "Elizabeth", "Eli", "Alexis", "Grace", "Sarah", "Alyssa", "Natalie",
                   "Chloe", "Bri", "Lauren", "Ella", "Anna", "Kayla", "Hailey", "Jessica", "Victoria", "Jasmine",
                   "Sydney", "Julia", "Morgan", "Kaitlyn", "Savannah", "Katherine", "Alexandra", "Rachel", "Lily",
                   "Megan", "Kaylee", "Jennifer", "Angelina", "Makayla", "Allison", "Brooke", "Lillian", "Faith"]
    last_names = ["Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
                  "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Robinson", "Clark",
                  "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Hill", "Green", "Adams",
                  "Baker", "Nelson", "Carter", "Mitchell", "Roberts", "Turner", "Phillips", "Campbell", "Parker"]

    first_name_index = randint(0, len(first_names) - 1)
    last_name_index = randint(0, len(last_names) - 1)
    first_name = first_names[first_name_index]
    last_name = last_names[last_name_index]

    email_rand_int = randint(100, 99999)
    email = first_name + last_name + str(email_rand_int) + "@tutanota.com"
    tuta_email = first_name + last_name + str(email_rand_int)
    full_name = first_name + " " + last_name

    # user_log.append(full_name)
    # user_log.append(email)

    print(email)

    with open('user_log.txt', 'w') as outfile:
        json.dump(email, outfile)

    captcha_exists = False
    tuta_pass = "idontkn0w22"
    fb_pass = str(randint(1000000, 9999999))
    captcha_id = str(randint(1000000, 9999999))
    captcha_id_fb = str(randint(1000000, 9999999))

    try:

        # Tuta Signup

        driver.get("https://app.tutanota.com/#register")
        time.sleep(5)
        # Wait for the loading alert to appear then disappear
        # i = 0
        # while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_loading_alert_xpath, 0):
        #     print("Loading alert has not appeared yet.")
        #     time.sleep(1)
        #     i += 1
        #     if i > 30:
        #         print("Been waiting for loading alert to appear for 30 seconds. Giving up")
        #         break
        # i = 0
        # while selenium_api.element_is_clickable(By.XPATH, tuta_signup_loading_alert_xpath, 0):
        #     print("Loading alert is still active")
        #     time.sleep(1)
        #     i += 1
        #     if i > 30:
        #         print("Been waiting for loading alert to disappear for 30 seconds. Giving up.")
        #         break
        # time.sleep(3)  # Wait after the alert is gone for good measure

        # Start filling in the signup form
        # wait()
        # selenium_api.wait_and_send_keys_on_element(By.XPATH, tuta_signup_email_xpath, key=tuta_email)
        # wait()
        driver.find_element_by_xpath(tuta_signup_email_xpath).send_keys(tuta_email)
        wait()
        driver.find_element_by_xpath(tuta_signup_password_xpath).send_keys(tuta_pass)
        wait()
        driver.find_element_by_xpath(tuta_signup_password_confirm_xpath).send_keys(tuta_pass)
        wait()
        driver.find_element_by_xpath(tuta_signup_terms_checkbox_xpath).click()
        wait()
        driver.find_element_by_xpath(tuta_signup_age_checkbox_xpath).click()
        wait()

        # Wait for the confirm button to be active, then click on it
        i = 0
        # driver was selenium_api
        # waiting = WebDriverWait(driver, 10)
        # element = waiting.until(EC.element_to_be_clickable((By.XPATH, tuta_signup_confirm_button_xpath)))
        # element.click
        signup_button1 = driver.find_element_by_xpath(tuta_signup_confirm_button_xpath).click()


        # while not driver.element_is_clickable(By.XPATH, tuta_signup_confirm_button_xpath, 0):
        #     time.sleep(1)
        #     i += 1
        #     if i > 30:
        #         print("Couldn't click on tuta signup confirm button for over 30 seconds. Giving up.")
        #         return "Couldn't click on tuta signup confirm button for over 30 seconds"
        #
        wait()

        # Wait for the creating account alert to appear unless the captcha or IP ban elements are present
        i = 0
        while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_creating_account_alert_xpath, 0):
            if selenium_api.element_is_present(By.XPATH, tuta_signup_captcha_textbox_xpath):
                print("Captcha element exists")
                captcha_exists = True
                break
            if selenium_api.element_is_present(By.XPATH, tuta_signup_ip_ban_alert_xpath):
                print("IP Ban alert exists")
                return "Tuta IP Ban"
            print("Creating account alert has not appeared yet. Captcha element has not appeared yet.")
            time.sleep(1)
            i += 1
            if i > 30:
                print("Been waiting for creating account alert or captcha element to appear for 30 seconds. "
                      "Giving up.")
                return "Been waiting for creating account alert or captcha element to appear for 30 seconds"

        wait()

        # If captcha exists, solve it
        if captcha_exists:
            # Solve the captcha
            print("Solving Captcha...")
            captcha_image = driver.find_element_by_xpath(tuta_signup_captcha_image_xpath)
            image_link = captcha_image.get_attribute("src")
            save_captcha_location = r"C:/Users/gabe4/Desktop/WORK/furry-octo-funicular/IG/captcha/captcha-example.png"
            urlretrieve(image_link, save_captcha_location)
            time.sleep(5)
            captcha_answer = get_time_from_image(save_captcha_location)
            # email_bot.send_email_attachment(save_captcha_location, subject="Cap " + captcha_id)
            # captcha_answer = email_bot.check_email(email_subject_check="Re: Cap " + captcha_id)
            driver.find_element_by_xpath(tuta_signup_captcha_textbox_xpath).send_keys(captcha_answer)

            wait()

            # Wait for the confirm button to be active, then click on it
            i = 0
            while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_confirm_button_xpath, 0):
                time.sleep(1)
                i += 1
                if i > 30:
                    print("Couldn't click on tuta signup confirm button for over 30 seconds. Giving up.")
                    return "02 - Couldn't click on tuta signup confirm button for over 30 seconds"

            wait()

            # Wait for the creating account alert to appear
            i = 0
            while not selenium_api.element_is_clickable(By.XPATH, tuta_signup_creating_account_alert_xpath, 0):
                print("Creating account alert has not appeared yet. Captcha element has not appeared yet.")
                time.sleep(1)
                i += 1
                if i > 30:
                    print("Been waiting for creating account alert to appear for 30 seconds. Giving up")
                    return "Been waiting for creating account alert to appear for 30 seconds"

        wait()

        # Waiting for the creating account alert to disappear
        i = 0
        print("Waiting 5 minutes for the creating account alert to disappear...")
        while selenium_api.element_is_clickable(By.XPATH, tuta_signup_creating_account_alert_xpath, 0):
            time.sleep(1)
            i += 1
            if i > 300:
                print("Been waiting for creating account alert to disappear for 5 minutes. Giving up.")
                return "Been waiting for creating account alert to disappear for 5 minutes"

        wait()

    except Exception as e:
        print("Something went wrong during account creation process.")
        print(e)
        return "Uncaught exception during Tuta account creation"


create_account("run")



# selenium_server = SeleniumServer()
#
# security_group = selenium_server.get_current_security_group()
#
# email_bot = EmailBot()
# if security_group == "Creator" or security_group == "Admin" or security_group == "Node" or security_group == "Dev":
#     driver = webdriver.Firefox(capabilities=selenium_server.capa, firefox_options=selenium_server.opts)
# # app = QApplication(sys.argv)
# cloud_database = CloudDatabase()  # CloudDatabase() must be instantiated before AppSettings()
# creator_instance_image_id = cloud_database.get_vars_table()[0][1]
#
# created_account_already = False
#
# for config in cloud_database.get_config():
#     app_settings = AppSettings(config)
#     global_stats = GlobalStats()
#     selenium_actions = SeleniumActions()
#     selenium_api = SeleniumAPI()
#     database_stuff = DatabaseStuff()
#     # dialog = AppDialog()
#     # dialog.show()
#     # app.exec_()
#     magic = Magic()
#
#     if security_group == "Dev":
#         print("Dev Security Group")
#         pass
#
#     elif security_group == "Admin":
#
#         pass
#
#         for user in app_settings.users:
#             selenium_actions.login(user)
#             selenium_actions.suggest_page_likes()
#
#     elif security_group == "Creator" and created_account_already is False:
#         created_account_already = True
#
#         global_start_time = time.time()
#
#         vars_three_letter_code = cloud_database.get_vars_table()[0][0]
#         cloud_database.three_letter_code = vars_three_letter_code
#         app_settings.three_letter_code = vars_three_letter_code
#
#         logins_count = len(app_settings.users)
#         desired_logins_count = app_settings.logins_count
#         max_daily_accounts_created = app_settings.max_daily_accounts_created
#         failure_response = None
#         credentials = selenium_actions.create_account()
#         if type(credentials) == str:
#             failure_response = "Failed during create_account: " + str(credentials)
#         elif type(credentials) == tuple:
#             name_for_db = credentials[0]
#             email_for_db = credentials[1]
#             password_for_db = credentials[2]
#             if selenium_actions.setup_account_chat_settings():
#                 if selenium_actions.setup_account_profile_settings():
#                     if selenium_actions.upload_profile_pic():
#                         try:
#                             cloud_database.add_login_to_db(name=name_for_db, username=email_for_db,
#                                                            password=password_for_db)
#                         except Exception as e:
#                             print("Couldn't add login to database")
#                             print(e)
#                             failure_response = "Failed during add_login_to_db"
#                     else:
#                         failure_response = "Failed during upload_profile_pic"
#                 else:
#                     failure_response = "Failed during setup_account_profile_settings"
#             else:
#                 failure_response = "Failed during setup_account_chat_settings"
#         else:
#             failure_response = "Failed during create_account: Generic"
#
#         global_stats.minutes = (time.time() - global_start_time) / 60
#
#         if failure_response:
#             report_subject = cloud_database.three_letter_code + " Account Creation Failure (" + time.strftime("%m/%d/%Y") + ")"
#             report_body = ("--- " + time.strftime("%m/%d/%Y") + " ---" +
#                            "\nDaily Limit: " + str(max_daily_accounts_created) +
#                            "\nOriginal Logins Count: " + str(logins_count) +
#                            "\nDesired Logins Count: " + str(desired_logins_count) +
#                            "\nMinutes Taken: " + str(global_stats.minutes) +
#                            "\nFailure Response: " + failure_response)
#         else:
#             report_subject = cloud_database.three_letter_code + " Account Creation Success (" + time.strftime("%m/%d/%Y") + ")"
#             report_body = ("--- " + time.strftime("%m/%d/%Y") + " ---" +
#                            "\nDaily Limit: " + str(max_daily_accounts_created) +
#                            "\nOriginal Logins Count: " + str(logins_count) +
#                            "\nDesired Logins Count: " + str(desired_logins_count) +
#                            "\nMinutes Taken: " + str(global_stats.minutes) +
#                            "\n--- Account Created Successfully! ---")
#
#         email_bot.send_email_message(report_subject, body=report_body)
#
#         print("Process Complete.")
#
#     elif security_group == "Hub":
#
#         global_start_time = time.time()
#
#         time.sleep(3600 * app_settings.padding_time)
#
#         # cloud_database.set_three_letter_code()
#
#         for user in app_settings.users:
#             cloud_database.add_day_to_login(user.username, user.days)
#             # wait 2 days before running new login
#             if user.days < 2:
#                 continue
#             time.sleep(5)
#             node = selenium_server.get_all_stopped_slave_instances()
#             time.sleep(5)
#             if node:
#                 selenium_server.ec2conn.start_instances(node)
#                 driver = selenium_server.connect_to_node()
#                 if driver:
#                     start_time = time.time()
#                     print("User: " + user.username)
#                     magic.actions(user)
#                     user.minutes = (time.time() - start_time) / 60
#                 try:
#                     driver.close()
#                     driver.quit()
#                 except:
#                     print("driver.stop() or driver.quit() didnt work")
#                     pass
#                 selenium_server.ec2conn.stop_instances(node)
#             if user.banned is True:
#                 cloud_database.delete_login(user)
#                 email_subject = cloud_database.three_letter_code + " Ban - " + user.username
#                 email_bot.send_email_message(email_subject, body="")
#
#         global_stats.minutes = (time.time() - global_start_time) / 60
# # ????????
#         # account_creation_start_time = time.time()
#         # logins_count = len(app_settings.users)
#         # desired_logins_count = app_settings.logins_count
#         # max_daily_accounts_created = app_settings.max_daily_accounts_created
#         # # Create creator instances
#         # attempts = 0
#         # while logins_count < desired_logins_count and attempts < max_daily_accounts_created:
#         #     selenium_server.create_creator_instance()
#         #     time.sleep(20)
#         #     logins_count += 1
#         #     attempts += 1
#         #     time.sleep(10)
#         #     # Poll for when the instances stop 'pending'
#         #     seconds = 0
#         #     while seconds < 120:
#         #         pending_creator_instances = selenium_server.get_all_pending_creator_instances()
#         #         if len(pending_creator_instances) == 0:
#         #             break
#         #         time.sleep(5)
#         #         seconds += 5
#         #         print(str(len(pending_creator_instances)) + " Creator instances are still pending... " + str(seconds))
#         #     time.sleep(10)
#         #     # Poll the creator instances for when they stop 'running'. Timeout: 65 minutes
#         #     seconds = 0
#         #     while seconds < 3900:
#         #         running_creator_instances = selenium_server.get_all_running_creator_instances()
#         #         if len(running_creator_instances) == 0:
#         #             print("No more running creator instances.")
#         #             break
#         #         time.sleep(30)
#         #         seconds += 30
#         #         print(str(len(running_creator_instances)) + " Creator instances are still running... " + str(seconds))
#         #     # Terminate any running creator instances. Should only matter if the above block timed out.
#         #     creator_instances = selenium_server.get_all_running_creator_instances()
#         #     if len(creator_instances) > 0:
#         #         # I believe the following should work for a list of instances, too
#         #         selenium_server.terminate_an_instance(creator_instances)
#         #     time.sleep(10)
#         #     # Poll for when the instances stop 'shutting-down'
#         #     seconds = 0
#         #     while seconds < 120:
#         #         shutting_down_creator_instances = selenium_server.get_all_shutting_down_creator_instances()
#         #         if len(shutting_down_creator_instances) == 0:
#         #             break
#         #         time.sleep(5)
#         #         seconds += 5
#         #         print(str(len(shutting_down_creator_instances)) + " Creator instances are still shutting-down... " + str(
#         #             seconds))
#         #     time.sleep(60)
#         #     # Delete all inactive volumes once the creator instances are all 'terminated'
#         #     selenium_server.delete_all_inactive_volumes()
#         # Update stats
#         # account_creation_time = (time.time() - account_creation_start_time) / 60
#         # total_account_creation_time = account_creation_time  # * attempts
#         # global_stats.minutes += total_account_creation_time
#         # global_stats.account_creation_attempts = attempts
#
#         try:
#             filterwarnings('ignore', category=pymysql.Warning)
#             cloud_database.add_statistics_to_db()
#         except Exception as e:
#             print("Failed to add statistics to database.")
#             print(e)
#
#         print("Process Complete.")
#
#     elif security_group == "Node":
#
#         if app_settings.three_letter_code == "LOL":
#             for user in app_settings.users:
#                 if user.username == "MakaylaMiller90597@tutanota.com":
#                     if selenium_actions.login(user):
#                         # selenium_actions.setup_account_chat_settings()
#                         # selenium_actions.setup_account_profile_settings()
#                         # selenium_actions.upload_profile_pic()
#                         selenium_actions.suggest_page_likes()
#                         break
#         pass
#
#     else:
#         print("No security group?")
#
#
# # Final steps after for loop
# if security_group == "Hub":
#     current_instance = selenium_server.get_current_instance()
#     selenium_server.ec2conn.stop_instances(current_instance)
#     pass
#
# elif security_group == "Creator":
#     current_instance = selenium_server.get_current_instance()
#     selenium_server.ec2conn.terminate_instances(current_instance)
#     pass
#
# if security_group == "Dev":
#     print("Dev Security Group")
#     pass
