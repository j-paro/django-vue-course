const app = Vue.createApp({
    data() {
        return {
            users: [
                {
                    id: 1554346,
                    name: "alice",
                    profession: "developer"
                },
                {
                    id: 633435,
                    name: "bob",
                    profession: "mail"
                },
                {
                    id: 23463,
                    name: "batman",
                    profession: "cook"
                },
                {
                    id: 2007,
                    name: "jane",
                    profession: "waiter"
                },
                {
                    id: 998757623,
                    name: "superman",
                    profession: "unemployed"
                },
            ]
        }
    }
})

const mountedApp = app.mount("#app")
