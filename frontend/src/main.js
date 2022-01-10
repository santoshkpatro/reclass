import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import upperFirst from 'lodash/upperFirst'
import camelCase from 'lodash/camelCase'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import './assets/main.css'

const requireComponent = require.context(
  './views/base',
  false,
  /Base[A-Z]\w+\.(vue|js)$/
)

const app = createApp(App)

requireComponent.keys().forEach((fileName) => {
  const componentConfig = requireComponent(fileName)

  const componentName = upperFirst(
    camelCase(fileName.replace(/^\.\/(.*)\.\w+$/, '$1'))
  )

  app.component(componentName, componentConfig.default || componentConfig)
})

app.use(store)
app.use(router)
app.mount('#app')
