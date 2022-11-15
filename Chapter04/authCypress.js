it('Successfully login using headers', function () { 
    cy.request({url: "https://www.googleapis.com/userinfo/v2/me",
        headers: { 
            authorization: 'Bearer access_token!'
        }
    }).then((resp) => {
        expect(resp.body).to.have.property('email')
    })
}) 