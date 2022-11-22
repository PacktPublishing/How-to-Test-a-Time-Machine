const webdriver = require('selenium-webdriver');

class newDriver extends webdriver.WebDriver {
    sayHi() {
        console.log("hi")
    }
}

module.exports = newDriver