const app = Vue.createApp({
    data() {
        return {
            message: "Hello, World!",
            num: 5
        }
    }
})

const mountedApp = app.mount("#app")