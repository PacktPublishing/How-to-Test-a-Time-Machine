describe('changeURL', function(){ 
    it('changesCodeForImage', function() { 
    cy.intercept('/search/count?q=intercept%2F&type=Commits', (req) => {
         req.reply((res) => {
             res.body = '<span aria-label="Testing time machines" title="Changed!" data-view-component="true" class="Counter js-codesearch-count tooltipped tooltipped-n ml-1 mt-1">Changed!</span>             '
         })
     }).as('newURL')
    cy.visit('https://github.com/search?q=intercept/')
    cy.wait('@newURL').its('response.body').should('include', 'Changed!')
    })
})