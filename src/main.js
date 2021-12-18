import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
// import 'bootstrap-icons/font/fonts/bootstrap-icons.css'
import './index.css'
// import { camelCase, upperFirst } from 'lodash'

const app = createApp(App)

// const requireComponent = require.context(
//   './components/base',
//   false,
//   /Base[A-Z]\w+\.(vue|js)$/
// )

// requireComponent.keys().forEach((fileName) => {
//   const componentConfig = requireComponent(fileName)

//   const componentName = upperFirst(
//     camelCase(fileName.replace(/^\.\/(.*)\.\w+$/, '$1'))
//   )

//   app.component(componentName, componentConfig.default || componentConfig)
// })

app.use(store)
app.use(router)
app.mount('#app')
