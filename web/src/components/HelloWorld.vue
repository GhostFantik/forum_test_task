<template>
  <div class="container">
    <div class="input-group mb-3">
      <input
        type="text"
        class="form-control"
        placeholder="Forum name"
        aria-label="Forum name"
        aria-describedby="button-addon2"
        v-model="forum_name"
      />
      <button
        class="btn btn-outline-secondary"
        type="button"
        id="button-addon2"
        @click="getUsersTrackingForum"
      >
        Show
      </button>
    </div>
    <div class="d-flex justify-content-center">
      <h1>{{ currentPage }}</h1>
    </div>
    <nav
      aria-label="Page navigation example"
      class="d-flex justify-content-center"
    >
      <ul class="pagination">
        <li class="page-item" :class="{ disabled: isLeftDisabled }">
          <button
            class="page-link"
            :disabled="isLeftDisabled"
            @click="previousPage"
          >
            &laquo;
          </button>
        </li>
        <li class="page-item" :class="{ disabled: isRightDisabled }">
          <button
            class="page-link"
            :disabled="isRightDisabled"
            @click="nextPage"
          >
            &raquo;
          </button>
        </li>
      </ul>
    </nav>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Пользователь</th>
          <th scope="col">Mark Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in users" :key="index">
          <th scope="row">{{ index + 1 }}</th>
          <td>{{ user.user }}</td>
          <td>{{ user.mark_time }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  data() {
    return {
      forum_name: "",
      users: [],
      next: null,
      previous: null,
      currentPage: 1,
    };
  },
  methods: {
    getUsersTrackingForum() {
      console.log("CLICK");
      axios
        .get(
          `http://127.0.0.1:8005/forum_tracking/forumreadtrack/?forum_name=${this.forum_name}`
        )
        .then((response) => {
          this.users = response.data.results;
          this.next = response.data.next;
          this.previous = response.data.previous;
        });
      this.currentPage = 1;
    },
    nextPage() {
      if (this.next !== null) {
        axios.get(this.next).then((response) => {
          this.users = response.data.results;
          this.next = response.data.next;
          this.previous = response.data.previous;
        });
        this.currentPage++;
      }
    },
    previousPage() {
      if (this.previous !== null) {
        axios.get(this.previous).then((response) => {
          this.users = response.data.results;
          this.next = response.data.next;
          this.previous = response.data.previous;
        });
        this.currentPage--;
      }
    },
  },
  computed: {
    isLeftDisabled() {
      return this.previous === null;
    },
    isRightDisabled() {
      return this.next === null;
    },
  },
};
</script>
