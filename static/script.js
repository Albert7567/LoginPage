function login(){ 
    alert("You are logged in.")
}
function firebaseLogin() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
  
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
        userCredential.user.getIdToken().then((idToken) => {
          // Send ID token to Flask backend
          fetch('/verify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ idToken: idToken })
          })
          .then(response => response.json())
          .then(data => {
            if (data.success) {
              window.location.href = '/dashboard';
            } else {
              alert('Login failed on backend.');
            }
          });
        });
      })
      .catch((error) => {
        alert(error.message);
      });
  }
  