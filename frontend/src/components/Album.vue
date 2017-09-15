<template>
  <div class="album">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'album',
  data () {
    return {
      msg: 'Welcome to my album'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1 {
  font-weight: normal;
}
</style>
