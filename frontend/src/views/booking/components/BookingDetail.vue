<template>
  <div class="createPost-container">
    <el-form ref="postForm" :model="postForm" :rules="rules" label-position="top" label-width="120px" class="form-container">

      <sticky :z-index="10" :class-name="'sub-navbar '+postForm.status">
        <el-button v-loading="loading" style="margin-left: 10px;" type="success" @click="submitForm">
          Publush
        </el-button>
        <el-button v-loading="loading" type="warning" @click="draftForm">
          Draft
        </el-button>
      </sticky>

      <div class="createPost-main-container">
        <div class="bookingInfo-container">
          <el-row :gutter="20">
            <el-col :span="16">
              <el-card >
                <el-form-item label="Start time:" required>
                    <el-date-picker v-model="postForm.start_time" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable @change="handle_picktime"/>
                </el-form-item>
                <el-form-item label="End time:" required>
                    <el-date-picker v-model="postForm.end_time" type="datetime" format="yyyy-MM-dd HH:mm" placeholder="Select date and time" clearable @change="handle_picktime"/>
                </el-form-item>
                <el-form-item label="Contact name:" style="width: 30%;" required>
                    <el-input v-model="postForm.contact_name" placeholder=""></el-input>
                </el-form-item>
                <el-form-item label="Contact phone:" style="width: 30%;" required>
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

            <el-col v-if="isEdit" :span="8">
              <el-row>
                <el-card >
                  <el-form-item label="Status:">
                    <el-input v-model="postForm.status" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Order:">
                    <el-input v-model="postForm.order.orderId" v-if="postForm.order" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Creator:">
                    <el-input v-model="postForm.create_by.name" v-if="postForm.create_by" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Company:">
                    <el-input v-model="postForm.company.name" v-if="postForm.company" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Discount:">
                    <el-input v-model="postForm.discount.name" v-if="postForm.discount" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Create at:">
                    <el-input v-model="postForm.create_at" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Change at:">
                    <el-input v-model="postForm.change_at" disabled></el-input>
                  </el-form-item>
                  <el-form-item label="Expiry date:">
                    <el-input v-model="postForm.create_at" disabled></el-input>
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
// import { fetchArticle } from '@/api/article'
// import { searchUser } from '@/api/remote-search'

const defaultForm = {
  bookingId: '',
  status: 'Darft',
  start_time: null,
  end_time: null,
  contact_name: '',
  contact_phone: '',
  pick_up_addr: '',
  drop_off_addr: '',
  vehicle: null,
  guide: null,
  remark: '',
  expiry_date: '',
  create_at: '',
  change_at: '',
  order: {
    orderId: ''
  },
  discount: {
    name: ' 25% for free',
    value: 0.25
  },
  create_by: {
    username: 'admin',
    name: 'admin'
  },
  company: {
    name: 'bastaki transposit'
  }
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
    const validateRequire = (rule, value, callback) => {
      if (value === '') {
        this.$message({
          message: rule.field + '为必传项',
          type: 'error'
        })
        callback(new Error(rule.field + '为必传项'))
      } else {
        callback()
      }
    }
    const validateSourceUri = (rule, value, callback) => {
      if (value) {
        if (validURL(value)) {
          callback()
        } else {
          this.$message({
            message: '外链url填写不正确',
            type: 'error'
          })
          callback(new Error('外链url填写不正确'))
        }
      } else {
        callback()
      }
    }
    return {
      postForm: Object.assign({}, defaultForm),
      loading: false,
      userListOptions: [],
      rules: {
        image_uri: [{ validator: validateRequire }],
        title: [{ validator: validateRequire }],
        content: [{ validator: validateRequire }],
        source_uri: [{ validator: validateSourceUri, trigger: 'blur' }]
      },
      tempRoute: {}
    }
  },
  computed: {
    contentShortLength() {
      return this.postForm.content_short.length
    },
    displayTime: {
      // set and get is useful when the data
      // returned by the back end api is different from the front end
      // back end return => "2013-06-25 06:59:25"
      // front end need timestamp => 1372114765000
      get() {
        return (+new Date(this.postForm.display_time))
      },
      set(val) {
        this.postForm.display_time = new Date(val)
      }
    }
  },
  created() {
    if (this.isEdit) {
      const id = this.$route.params && this.$route.params.id
      this.fetchData(id)
    } else {
      this.postForm = Object.assign({}, defaultForm)
    }

    // Why need to make a copy of this.$route here?
    // Because if you enter this page and quickly switch tag, may be in the execution of the setTagsViewTitle function, this.$route is no longer pointing to the current page
    // https://github.com/PanJiaChen/vue-element-admin/issues/1221
    this.tempRoute = Object.assign({}, this.$route)
  },
  methods: {
    fetchData(id) {
    //   fetchArticle(id).then(response => {
    //     this.postForm = response.data
    //     // Just for test
    //     this.postForm.title += `   Article Id:${this.postForm.id}`
    //     this.postForm.content_short += `   Article Id:${this.postForm.id}`

    //     // Set tagsview title
    //     this.setTagsViewTitle()
    //   }).catch(err => {
    //     console.log(err)
    //   })
    },
    setTagsViewTitle() {
      const title = 'Edit Article'
      const route = Object.assign({}, this.tempRoute, { title: `${title}-${this.postForm.id}` })
      this.$store.dispatch('tagsView/updateVisitedView', route)
    },
    submitForm() {
      console.log(this.postForm)
      this.$refs.postForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$notify({
            title: '成功',
            message: '发布文章成功',
            type: 'success',
            duration: 2000
          })
          this.postForm.status = 'published'
          this.loading = false
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    draftForm() {
      if (this.postForm.content.length === 0 || this.postForm.title.length === 0) {
        this.$message({
          message: '请填写必要的标题和内容',
          type: 'warning'
        })
        return
      }
      this.$message({
        message: '保存成功',
        type: 'success',
        showClose: true,
        duration: 1000
      })
      this.postForm.status = 'draft'
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
