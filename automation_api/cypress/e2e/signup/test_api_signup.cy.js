describe('API Testing To SignUp Services', () => {
  it('Must register user successfully', () => {
    const username = 'user_' + Math.random().toString(36).substring(7);
    cy.request({
      method: 'POST',
      url: 'https://api.demoblaze.com/signup',
      body: {
        username,
        password: '12345'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
    });
  });
  it('Cannot register an existing user', () => {
    cy.request({
      method: 'POST',
      url: 'https://api.demoblaze.com/signup',
      body: {
        username: 'nadupo',
        password: '123456'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('errorMessage', 'This user already exist.');
    });
  });
});

