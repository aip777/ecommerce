<template>
  <div class="home">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Products</h2>
      </div>
      
      <ProductBox 
        v-for="product in lastestProducts"
        v-bind:key="product.id"
        v-bind:product="product"/>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
  name: 'Home',
  data() {
    return {
      lastestProducts: []
    }
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLastestProducts()
    document.title = 'Home | Ecommerce Store'
  },
  methods: {
    async getLastestProducts() {
      this.$store.commit('setIsLoading', true)

      await  axios.get('/api/v1/products/latest')
      .then(response => {
        this.lastestProducts = response.data
      })
      .catch( error => {
        console.log(error)
      })
      
      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>

<style lang="scss">
.hero.is-dark {
  background-color: #a86611;
  color: #fff;
  padding-bottom: 0px;
  height: 240px;
}
.hero.is-medium .hero-body{
  padding: 3rem 4.5rem;
}
 
 
</style>
