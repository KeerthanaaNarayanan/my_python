# sonicos ui7 launch url - https://blrauto.eng.sonicwall.com/launch/launch-form-sonicos7

def login_ui(self):
    try:
        retries = 0
        while retries < 2:
            try:
                logger.info("Login to SonicAuto (UI)")
                self.browser_name = "chrome"
                self.kill_browser_sessions()
                chromedriver_autoinstaller.install(custom_path=chrome_driver_directory)
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument('--disable-extensions')
                chrome_options.add_argument('--disable-software-rasterizer')
                chrome_options.add_argument("--start-maximized")
                chrome_options.add_argument("--ignore-certificate-errors")
                chrome_options.add_argument('--remote-debugging-port=9222')
                chrome_options.add_argument("–-disable-dev-shm-usage")
                chrome_options.add_argument('window-size=1920x1080')
                capabilities = DesiredCapabilities.CHROME
                capabilities['applicationCacheEnabled'] = False

                self.browser = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
                self.lib.go_to_url(self.lib.URL)
                self.code_flow = "Login workflow\t\t:\t"
                self.lib.set_text_field('xpath', "//input[@type='text' and @name='emailInput']",
                                        self.lib.FW_USERNAME)
                self.lib.set_text_field('xpath', "//input[@type='password' and @name='emailInput']",
                                        self.lib.FW_PASSWORD)
                self.lib.click_element('class', 'sw-login__trigger')
                time.sleep(3)
                if self.lib.did_page_load_successfully():
                    time.sleep(3)
                    current_url = self.lib.browser.current_url
                    logger.debug2("Current URL: " + str(current_url))
                    while 'dashboard' not in current_url:
                        current_url = self.lib.browser.current_url
                        if "nsm-warning" in current_url:
                            logger.info("NSM Warning Shown")
                            logger.debug(str(self.code_flow) + "Handling NSM warning")
                            self.get_element('xpath',
                                             "//div[contains(@class, 'sw-action-bar-item')]/button[contains(text(), 'Proceed')]",
                                             visible=False).click()
                        if "launchWizard" in current_url:
                            logger.info("Launch Wizard Shown")
                            self.click_element('xpath',
                                               "//div[contains(text(), 'To manually configure SonicWall')]/a")
                        if "preempt" in current_url:
                            logger.info("Config Preempt Shown")
                            self.click_element('xpath', "//button[contains(text(), 'Config')]")
                        time.sleep(2)
                        current_url = self.lib.browser.current_url
                self.lib.check_and_accept_multiple_alerts()  # Remove comments one's GEN-7103 is solved
                self.lib.configure_toggle_button("Configuration", True,
                                                 label=False)  # Remove comments one's GEN-7103 is solved
                self.lib.check_and_accept_multiple_alerts()
                self.wait_for_page_data_to_be_rendered()  # Remove comments one's GEN-7103 is solved
                return True
            except Exception as err:
                logger.error(str(self.code_flow) + "Exception : " + str(err))
                retries = retries + 1
                if retries < 2:
                    self.lib.close_browser()
                    continue
                else:
                    logger.error(str(self.code_flow) + "Exception \t: " + str(err))
                    Assertion.fail(str(self.code_flow) + "Unable to Login")
    except Exception as err:
        logger.error(str(self.code_flow) + "Exception \t: " + str(err))
        Assertion.fail(str(self.code_flow) + "Firewall login failed")


def logout_ui(self):
    try:
        self.code_flow = "Logout workflow\t\t:\t"
        self.lib.click_element('xpath', '//div/span[contains(@class,"sw-avatar__initials")]')
        self.lib.click_element('xpath', '//span[contains(text(),"Log Out")]')
        self.lib.click_element('xpath', '//div/button[contains(text(),"Continue")]')
        if self.lib.does_element_exist('xpath', '//div[contains(text(), "You have been logged out.")]'):
            logger.info(str(self.code_flow) + "Logged out")
        self.lib.close_browser()
        self.lib.quit()
    except Exception as err:
        logger.error(str(self.code_flow) + "Exception \t: " + str(err))
        self.lib.close_browser()
        self.lib.quit()
        Assertion.fail(str(self.code_flow) + "Firewall logout failed")
