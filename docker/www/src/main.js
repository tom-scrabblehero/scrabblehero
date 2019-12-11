import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import VueGtag from 'vue-gtag'

import App from './App.vue'
import Home from './components/Home.vue'
import Word from './components/Word.vue'
import Contact from './components/Contact.vue'

import './assets/styles.scss'
import 'bootstrap-vue/dist/bootstrap-vue.css'

class Api {
  constructor(url) {
    this.url = url
  }

  async get(route) {
    return fetch(this.url + route).then(response => response.json())
  }
}

const routes = [
  {name: 'index', path: '/', component: Home},
  {name: 'contact', path: '/contact', component: Contact},
  {name: 'words', path: '/words/:word', component: Word}
]

const router = new VueRouter({
  routes: routes,
  mode: 'history'
})

Vue.config.productionTip = false
Vue.prototype.$api = new Api(process.env.VUE_APP_API_URL)
Vue.use(VueRouter)
Vue.use(BootstrapVue)
Vue.use(VueGtag, { config: { id: process.env.VUE_APP_GOOGLE_TRACKING_ID }}, router)

const app = new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')

window.app = app

console.log(process.env)
