import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'

import './assets/styles.scss'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue)


class Api {
  constructor(url) {
    this.url = url
  }

  async get(route) {
    return fetch(this.url + route).then(response => response.json())
  }
}

Vue.prototype.$api = new Api(process.env.VUE_APP_API_URL)

const v = new Vue({
  render: h => h(App),
}).$mount('#app')

window.v = v
