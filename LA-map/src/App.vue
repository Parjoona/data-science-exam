<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/amap">A map</router-link>
      <router-link to="/bmap">B map</router-link>
      <router-link to="/cmap">C map</router-link>
    </div>
    <transition name="fade">
      <router-view/>
    </transition>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  line-height: calc(20vh - 60px);
  font-size: 2rem;
}

#nav a {
  font-weight: bold;
  padding: 5px 20px;
  margin: 0 10px;
  color: #2c3e50;
  text-decoration: none;
  text-transform: uppercase;
  border: 2px solid #000;
}

#nav a:hover {
  background: rgb(212, 243, 255);
}

#nav a.router-link-exact-active {
  color: #1181c2;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 1.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
