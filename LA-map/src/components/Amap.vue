<template>
  <div>
    <iframe src="maps/a-map.html"></iframe>
  </div>
</template>

<script>
  export default {
    name: 'amap',
  }
</script>

<style>
    iframe {
      position: absolute;
      bottom: 0;
      right: 0;
      width: 100%;
      height: 80vh;
      margin: 0;
      padding: 0;
      border: 0;
    }
</style>