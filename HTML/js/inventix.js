// main library for interaction with the backend
// import {Inventix} from "./inventix.js"

class Inventix {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async login(username, password) {
        const rawResponse = await fetch(this.baseUrl + "/login",
            {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({username: username, password: password})
            });
        return await rawResponse.json();
    }

    async searchItems(name = "", notes = "") {
        const params = new URLSearchParams();
        params.append("name", name);
        params.append("notes", notes);
        const rawResponse = await fetch(this.baseUrl + "/searchItems?" + params.toString());
        return await rawResponse.json();
    };

    async getItem(id) {
        const rawResponse = await fetch(this.baseUrl + "/getItem/" + id);
        return await rawResponse.json();
    };
}

export {Inventix};