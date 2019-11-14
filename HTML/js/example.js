// example usage of the api
// import using <script src="example.js" type="module"></script>

import {Inventix} from "./inventix.js"

const api = new Inventix("https://example.com");

(async () => {
    console.log(await api.login("testuser", "password"));
    console.log(await api.searchItems("l"));
    console.log(await api.getItem(5))
})();
