const newDriver = require('./newDriver.js')
const webdriver = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const chromedriver = require('chromedriver');

newDriver.prototype = new webdriver.WebDriver;

let driver = Object.assign(new newDriver, new webdriver.Builder()
.withCapabilities(webdriver.Capabilities.chrome())
.build());

driver.sayHi();