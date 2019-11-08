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

async function apiRequest(data,endpoint){
//    const url = 'http://inventix:8000/login';
    const url = 'http://192.168.3.64:8000/'+endpoint;
//    const url = 'http://192.168.3.141:8000/login';
    // fetch: https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch
    try {
        const response = await fetch(url, {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data) 
          });
        const json = await response.json();
        //console.log(json);
        //console.log('Success:', JSON.stringify(json));
        return JSON.stringify(json)
    } catch (error) {
        console.error('Error:', error);
    }    
    
}

async function loginUser (){
    enableLoadAnimation();
    //alert('wanna login');
    var username = document.getElementById('loginUserName').value;
    var password = document.getElementById('loginPassWord').value;
    const digestHex = await digestMessage(password);
    console.log(digestHex);



    const data = {username: username, password: digestHex};    
    alert(await apiRequest(data,'login'));
};

async function searchWords (){
    var searchquery = document.getElementById('searchquery').value;
    alert('search for: ' + searchquery);
//    const url = 'http://inventix:8000/getItems';
    const data = {q: searchquery};
    alert(await apiRequest(data,'searchItems'));
    
}


async function digestMessage(message) {
  const msgUint8 = new TextEncoder().encode(message);                           // encode as (utf-8) Uint8Array
  const hashBuffer = await crypto.subtle.digest('SHA-256', msgUint8);           // hash the message
  const hashArray = Array.from(new Uint8Array(hashBuffer));                     // convert buffer to byte array
  const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join(''); // convert bytes to hex string
  return hashHex;
}





//document.addEventListener('load',enableLoadAnimation);
document.addEventListener('DOMContentLoaded', loadContentFromAPI);
document.getElementById('loginButton').addEventListener('click', loginUser);
document.getElementById('submitSearch').addEventListener('click', searchWords);
