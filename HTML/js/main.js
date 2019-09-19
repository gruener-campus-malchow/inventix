'use strict';

var loadContentFromAPI = function ( ) {
     
     var body = document.getElementsByTagName('body')[0];
     var loadlogo = document.createElement('img');
     var url = document.createAttribute('src');
     url.value = 'https://cis.gruener-campus-malchow.de/diglit/img/loading.gif';
     loadlogo.setAttributeNode(url);
     body.prepend(loadlogo);

};

document.addEventListener('DOMContentLoaded', loadContentFromAPI);
