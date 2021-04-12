<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Moods</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.mood-modal>Add Mood</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Timestamp</th>
              <th scope="col">Name</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(mood, index) in moods" :key="index">
              <td>{{ mood.timestamp }}</td>
              <td>{{ mood.name }}</td>
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
    <b-modal ref="addMoodModal"
            id="mood-modal"
            title="Add a new Mood"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-timestamp-group"
                    label="Timestamp:"
                    label-for="form-timestamp-input">
          <b-form-input id="form-timestamp-input"
                        type="text"
                        v-model="addMoodForm.timestamp"
                        required
                        placeholder="Enter timestamp">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
            <b-form-input id="form-name-input"
                          type="text"
                          v-model="addMoodForm.name"
                          required
                          placeholder="Enter Name">
            </b-form-input>
          </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      moods: [],
      addMoodForm: {
        timestamp: '',
        name: '',
      },
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
    addMood(payload) {
      const path = 'http://localhost:5000/moods';
      axios.post(path, payload)
        .then(() => {
          this.getMoods();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMood();
        });
    },
    initForm() {
      this.addMoodForm.timestamp = '';
      this.addMoodForm.name = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMoodModal.hide();
      const payload = {
        timestamp: this.addMoodForm.timestamp,
        name: this.addMoodForm.name,
      };
      this.addMood(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addMoodModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getMoods();
  },
};
</script>
