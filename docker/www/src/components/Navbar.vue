<template>
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand href="/">Scrabble Hero</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="/two-letter-words">Two Letter Words</b-nav-item>
        <b-nav-item href="/words/starting-with/AA">Words Starting With</b-nav-item>
        <b-nav-item href="/words/ending-with/ING">Words Ending With </b-nav-item>
        <b-nav-item href="/words/containing/AZ">Words Containing </b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>
