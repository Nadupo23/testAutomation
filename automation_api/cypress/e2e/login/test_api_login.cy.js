describe('API Testing To Login Services', () => {
  it('Must Correct username and password in login', () => {
    cy.request({
      method: 'POST',
      url: 'https://api.demoblaze.com/login',
      body: {
        username: 'nadupo',
        password: '123456'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.contain('Auth_token:');
    });
  });
  it('Must Incorrect username in login', () => {
    cy.request({
      method: 'POST',
      url: 'https://api.demoblaze.com/login',
      body: {
        username: 'pKnjFwWxMmlksjndf385959jndfsKgDxzpyppwKjdf584',
        password: '123'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('errorMessage', 'User does not exist.');
    });
  });
  it('Must Incorrect password in login', () => {
    cy.request({
      method: 'POST',
      url: 'https://api.demoblaze.com/login',
      body: {
        username: 'nadupo',
        password: '123'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('errorMessage', 'Wrong password.');
    });
  });
});

