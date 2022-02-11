describe('changeResponseTest', function(){ 

    it('changesResponseFromNumbersAPI', function() { 
    
     const staticResponse = { 
      statusCode: 200, 
      body: { "text": "42 modified response", "number": 42, "found": true, "type": "trivia"}, 
      headers :{'Access-Control-Allow-Origin': '*'} 
     } 
    
    cy.intercept('http://numbersapi.com/42?json', staticResponse) 
    cy.visit('http://numbersapi.com/42?json') 
    
    })
})