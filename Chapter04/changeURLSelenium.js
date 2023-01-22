(async function changeURLSelenium() {
    const chrome = require('selenium-webdriver/chrome');
    const webdriver = require('selenium-webdriver');
    const http = require('selenium-webdriver/devtools/networkinterceptor');
    const chromedriver = require('chromedriver');    
    const assert = require('assert')
    console.log(chromedriver.path)
    try {
    let driver = await new webdriver.Builder()
      .forBrowser('chrome')
      .build();
    const connection = await driver.createCDPConnection('page')
    let url = "https://github.com/"
    let httpResponse = new http.HttpResponse(url)
    httpResponse.addHeaders("Content-Type", "UTF-8")
    httpResponse.method = "GET"
    httpResponse.status = 404
    httpResponse.urlToIntercept = url
    httpResponse.returnBody = "TestingTimeMachines"
    httpResponse.body = "<html><body>TestingTimeMachines</body></html>" //<img src="https://random-d.uk/api/261.jpg" alt="TestingTimeMachines">'
    await driver.onIntercept(connection, httpResponse, async function () {
      let body = await driver.getPageSource()
      assert.strictEqual(body.includes("TestingTimeMachines"), true, 'Body contains: ${body}')
    })
    await driver.get(url)
    await driver.quit()
} catch (e) {
    console.log(e)
}
}())
