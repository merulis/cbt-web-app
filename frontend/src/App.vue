<script setup>
</script>

<template>
  <header>
    <h2>CBT application</h2>
    <nav>
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/counter">Counter</RouterLink>
    </nav>
  </header>

  <main>
    <aside></aside>
    <section id="main-content">
      <RouterView />
    </section>
    <aside></aside>
  </main>
</template>

<style scoped>
h2 {
  margin-right: 20px;
}
nav {
  margin-left: 10px;
}
nav > a{
  padding: 10px;
  margin-left: 5px;
  margin-right: 5px;
  text-decoration: none;
}
a:hover {
  padding: 10px;
  border-radius: 10px;
  color: var(--text-hover);
  background-color:var(--hover);
}
</style>
