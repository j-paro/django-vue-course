const app = Vue.createApp({
    computed: {
        getRandomComputed() {
            return Math.random();
        }
    },
    methods: {
        getRandomNumber() {
            return Math.random();
        }
    }
})

const mountedApp = app.mount("#app")