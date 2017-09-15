import Vue from 'vue'
import Router from 'vue-router'
//import Hello from '@/components/Hello'
import Album from '@/components/Album'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      // name: 'Hello',
      // component: Hello
      name: 'Album',
      component: Album
    }
  ]
})
