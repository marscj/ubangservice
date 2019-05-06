<template>
  <div id="welcome" >
    <div class="enter">
      <ul>
        <router-link tag="li" to="/login">
          <a>Company Entrance</a>
        </router-link>
      </ul>
    </div>
    <img alt="logo" src="@/assets/logo.png">
    <h1>Welcome to UBang Service</h1>
    <h2>The website is under construction.</h2>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
#welcome {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}

.enter {
  text-align: right;
  padding-right: 20px
}

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>