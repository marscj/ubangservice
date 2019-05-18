<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" label-position="top" label-width="120px" class="form-container">

      <sticky :z-index="10" :class-name="'sub-navbar '+postForm.status">
        <el-button v-if="isEdit" v-loading="loading" style="margin-left: 10px;" type="danger" >
          Delete
        </el-button>
        <el-button v-if="isEdit" v-loading="loading" style="margin-left: 10px;" type="warning" >
          Cancel
        </el-button>
        <el-button v-if="!isEdit" v-loading="loading" style="margin-left: 10px;" type="success" @click="createForm">
          Create
        </el-button>
        <el-button v-else v-loading="loading" style="margin-left: 10px;" type="success" @click="updateForm">
          Edit
        </el-button>
      </sticky>

      <div class="createPost-main-container">
        <div class="bookingInfo-container">
          <el-row :gutter="20">
            <el-col :span="16">
              <el-card >
                <el-form-item label="Start time:" prop="start_time" required>
                    <el-date-picker v-model="postForm.start_time" type="datetime" value-format="yyyy-MM-dd HH:mm" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable @change="handle_picktime"/>
                </el-form-item>
                <el-form-item label="End time:" prop="end_time" required>
                    <el-date-picker v-model="postForm.end_time" type="datetime" value-format="yyyy-MM-dd HH:mm" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable @change="handle_picktime"/>
                </el-form-item>
                <el-form-item label="Contact name:" prop="contact_name" style="width: 30%;" required>
                    <el-input v-model="postForm.contact_name" placeholder=""></el-input>
                </el-form-item>
                <el-form-item label="Contact phone:" prop="contact_phone" style="width: 30%;" required>
                    <el-input v-model="postForm.contact_phone"></el-input>
                </el-form-item>
                <el-form-item label="Vehicle:" style="width: 30%;" required>
                    <el-input v-model="postForm.vehicle"></el-input>
                </el-form-item>
                <el-form-item label="Guide:" style="width: 30%;">
                    <el-input v-model="postForm.guide"></el-input>
                </el-form-item>
                <el-form-item label="Pick up address:">
                    <el-input v-model="postForm.pick_up_addr"></el-input>  
                </el-form-item>
                <el-form-item label="Drop off address:">
                    <el-input v-model="postForm.drop_off_addr"></el-input>  
                </el-form-item>
                <el-form-item label="Remark:">
                    <el-input v-model="postForm.remark" :autosize="{ minRows: 4, maxRows: 4}" type="textarea"></el-input>  
                </el-form-item>
              </el-card>
            </el-col>

            <el-col :span="8">
              <el-row>
                <el-card >
                  <el-form-item label="Status:">
                    <!-- <span v-if="postForm.status">{{ postForm.status }}</span> -->
                    <el-input v-model="postForm.status" v-if="postForm.status" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Order:">
                    <!-- <span v-if="postForm.order">{{ postForm.order.orderId }}</span> -->
                    <el-input v-model="postForm.order.orderId" v-if="postForm.order" disabled></el-input>
                    <!-- <el-input disabled></el-input> -->
                  </el-form-item>
                  <el-form-item label="Creator:">
                    <!-- <span v-if="postForm.create_by">{{ postForm.create_by.name || postForm.create_by.username }}</span> -->
                    <el-input v-model="name" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Company:">
                    <!-- <span v-if="postForm.company_by">{{ postForm.company_by.name }}</span> -->
                    <el-input v-model="postForm.company_by.name" v-if="postForm.company_by" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Discount:">
                    <!-- <span v-if="postForm.discount">{{ postForm.discount.name }}</span> -->
                    <el-input v-model="postForm.discount.name" v-if="postForm.discount" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Create at:">
                    <!-- <span v-if="postForm.create_at">{{ postForm.create_at }}</span> -->
                    <el-input v-model="postForm.create_at" v-if="postForm.create_at" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Change at:">
                    <!-- <span postForm.change_at>{{ postForm.change_at }}</span> -->
                    <el-input v-model="postForm.change_at" v-if="postForm.change_at" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Expiry date:">
                    <!-- <span v-if="postForm.expiry_date">{{ postForm.expiry_date }}</span> -->
                    <el-input v-model="postForm.expiry_date" v-if="postForm.expiry_date" disabled></el-input>
                  </el-form-item>
                </el-card>
              </el-row>
            </el-col>
          </el-row>
        </div>
        <div class="itinerary-container">
          <el-row>
            <el-col >
              <el-card >
                <div slot="header">
                  <span>Itinerary</span>
                </div>
              </el-card>
            </el-col>
          </el-row>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script>
import Sticky from '@/components/Sticky'
import { validURL } from '@/utils/validate'
import { getBooking, updateBooking, createBooking } from '@/api/booking'
// import { searchUser } from '@/api/remote-search'

const defaultForm = {
  id: undefined,
  bookingId: undefined,
  status: undefined,
  start_time: undefined,
  end_time: undefined,
  contact_name: undefined,
  contact_phone: undefined,
  pick_up_addr: undefined,
  drop_off_addr: undefined,
  vehicle: undefined,
  guide: undefined,
  remark: undefined,
  expiry_date: undefined,
  create_at: undefined,
  change_at: undefined,
  order: undefined,
  discount: undefined,
  create_by: undefined,
  company_by: undefined
}

export default {
  name: 'BookingDetail',
  components: { Sticky },
  props: {
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      postForm: Object.assign({}, defaultForm),
      loading: false,
      userListOptions: [],
      rules: {
        start_time: [
          { required: true, message: 'This fields is required', trigger: 'blur' }
        ],
        end_time: [
          { required: true, message: 'This fields is required', trigger: 'blur' }
        ],
        contact_name: [
          { required: true, message: 'This fields is required', trigger: 'blur' }
        ],
        contact_phone: [
          { required: true, message: 'This fields is required', trigger: 'blur' }
        //   { required: true, pattern:/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im, message: 'Please input phone number', trigger: 'blur' }
        ]
      },
      tempRoute: {}
    }
  },
  computed: {
    name: {
      get() {
        if(this.postForm.create_by != undefined) {
          return this.postForm.create_by.name || this.postForm.create_by.username
        }
        return ''
      },
      set() {}
    }
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id
      this.fetchData(id)
    } else {
      this.postForm = Object.assign({}, defaultForm)
    }
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    fetchData(id) {
      getBooking(id).then(response => {
        this.postForm = response.data
        this.setTagsViewTitle()
      }).catch(err => {
        console.log(err)
      })
    },
    setTagsViewTitle() {
      const title = 'Edit Booking'
      const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.bookingId}` })
      this.$store.dispatch('tagsView/updateVisitedView', route)
    },
    createForm() {
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.postForm.status = 'Created'

          console.log(this.postForm)

          createBooking(this.postForm).then(response => {
            var id = response.data['id']
            this.$router.replace({ 
              path: `/booking/edit/${id}`
            })
            // this.$notify({
            //   title: 'Success',
            //   message: 'Create Successfully',
            //   type: 'success',
            //   duration: 2000
            // })
            // this.loading = false
          }).catch(err => {
            console.log(err)
          })
        } else {
          return false
        }
      })
    },
    updateForm() {
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$notify({
            title: 'Success',
            message: 'Change Successfully',
            type: 'success',
            duration: 2000
          })
          this.loading = false
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    
    getRemoteUserList(query) {
    //   searchUser(query).then(response => {
    //     if (!response.data.items) return
    //     this.userListOptions = response.data.items.map(v => v.name)
    //   })
    },
    handle_picktime() {
      console.log(this.postForm.start_time)
      console.log(this.postForm.end_time)
      if(this.postForm.start_time != null && this.postForm.end_time != null) {

      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import "~@/styles/mixin.scss";

.createPost-container {
  position: relative;

  .createPost-main-container {
    padding: 20px 20px 20px 20px;

    .bookingInfo-container {
      position: relative;
      @include clearfix;
      padding-bottom: 20px;

      .bookingInfo-container-item {
        float: left;
      }
    }

    .itinerary-container {
      position: relative;
      @include clearfix;
      padding-bottom: 50px;
    }
  }


}

</style>
