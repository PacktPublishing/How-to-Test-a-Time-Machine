describe('changeURL', function(){ 
    it('changesCodeForImage', function() { 
    cy.intercept('https://github.com/', (req) => {
         req.reply((res) => {
             res.body = '<img src="https://random-d.uk/api/261.jpg" alt="TestingTimeMachines">'
         })
     }).as('newURL')
    cy.visit('https://github.com/')
    cy.wait('@newURL').its('response.body').should('include', 'TestingTimeMachines')
    })
})