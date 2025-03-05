import {createStore} from "vuex";

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      username: ''
    },
    department: {
      id: 0,
      title: ''
    }
  },
  mutations: {
    initializeHospital(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.username = localStorage.getItem('username')
        state.user.id = localStorage.getItem('userid')
        state.department.id = localStorage.getItem('department_id')
        state.department.title = localStorage.getItem('department_title')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
        state.department.id = 0
        state.department.title = ''
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
    setDepartment(state, department) {
      state.department = department

      localStorage.setItem('department_id', department.id)
      localStorage.setItem('department_title', department.title)
    }
  },
  actions: {},
  modules: {}
})
