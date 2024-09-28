<script setup>
import { useCounterStore } from '../stores/counter'

const store = useCounterStore()
</script>


<template>
  <section>
    <h2>Couter</h2>
    <p>Count: {{ store.count }}</p>
    <p>Double count: {{ store.doubleCount }}</p>
    <button type="button" @click="store.increment">Increment</button>
  </section>
</template>