<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Moods</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Add Mood</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Timestamp</th>
              <th scope="col">Mood</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(mood, index) in moods" :key="index">
              <td>{{mood.timestamp}}</td>
              <td>{{mood.name}}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      moods: [],
    };
  },
  methods: {
    getMoods() {
      const path = 'http://localhost:5000/moods';
      axios.get(path)
        .then((res) => {
          this.moods = res.data.moods;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMoods();
  },
};
</script>
