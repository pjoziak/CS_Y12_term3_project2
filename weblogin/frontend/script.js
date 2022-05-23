//var cors = require('cors');
//app.use(cors());

handle_response = (response) => {
    console.log(response);
    if (response.ok) {
        console.log('OK');
    } else {
        console.log('NOK');
    }
};

handle_button_click = (event) => {
    var url = "http://localhost:12345/login";
    var user_input = document.getElementById("user");
    var pass_input = document.getElementById("pass");
    var header = document.getElementById("header");
    var user = user_input.value;
    var pass = pass_input.value;
    console.log(`Button clicked with user: [${user}], password: [${pass}].`);
    header.style["color"] = "#00FF00";
    var credentials = {user: user, password: pass};
    var options = {
      method: 'POST',
      mode: 'no-cors',
      body: JSON.stringify(credentials)
    };

    fetch(url, options).then(console.log);
}