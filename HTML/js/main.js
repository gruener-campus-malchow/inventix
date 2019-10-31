'use strict';

function insertLoadAnimation(){
     //alert('loading');
     var body = document.getElementsByTagName('body')[0];
     var loadlogo = document.createElement('img');
     var url = document.createAttribute('src');
     url.value = 'https://cis.gruener-campus-malchow.de/diglit/img/loading.gif';
     var id = document.createAttribute('id');
     id.value = 'loadAnimation'
     loadlogo.setAttributeNode(url);
     loadlogo.setAttributeNode(id);
     body.prepend(loadlogo);
}

function enableLoadAnimation(){
    var loadAnimation = document.getElementById('loadAnimation');
    loadAnimation.style.display = 'visible';
}

function disableLoadAnimation(){
    var loadAnimation = document.getElementById('loadAnimation');
    loadAnimation.style.display = 'none';
}

function loadContentFromAPI(){
    insertLoadAnimation();
    disableLoadAnimation();
};

function loginUser (){
    enableLoadAnimation();
    alert('wanna login');
    var username = document.getElementById('loginUserName').value;
    var password = document.getElementById('loginPassWord').value;
    
    const url = 'http://192.168.3.178:8000/login';
    const data = {user: username, hash: password};
    // fetch: https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch
    try {
        const response = fetch(url, {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers: {'Content-Type': 'application/json'},
            mode:'no-cors'
          });
          
          
  const json = response.json();
  console.log('Success:', JSON.stringify(json));
} catch (error) {
  console.error('Error:', error);
}
    
    alert(username + ' ' + password);
    

};

//document.addEventListener('load',enableLoadAnimation);
document.addEventListener('DOMContentLoaded', loadContentFromAPI);
document.getElementById('loginButton').addEventListener('click', loginUser);
