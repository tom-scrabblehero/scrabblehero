import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'
import Home from './components/Home.vue'
import Contact from './components/Contact.vue'

import './assets/styles.scss'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false

class Api {
  constructor(url) {
    this.url = url
  }

  async get(route) {
    return fetch(this.url + route).then(response => response.json())
  }
}

Vue.prototype.$api = new Api(process.env.VUE_APP_API_URL)

const routes = [
  {path: '/', component: Home},
  {path: '/contact', component: Contact}
]

const router = new VueRouter({
  routes: routes,
  mode: 'history'
})

Vue.use(VueRouter)
Vue.use(BootstrapVue)

const v = new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')

window.v = v
