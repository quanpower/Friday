export default [
  // user
  {
    path: '/user',
    component: '../layouts/UserLayout',
    routes: [
      { path: '/user', redirect: '/user/login' },
      { path: '/user/login', component: './User/Login' },
      { path: '/user/register', component: './User/Register' },
      { path: '/user/register-result', component: './User/RegisterResult' },
    ],
  },
  // app
  {
    path: '/',
    component: '../layouts/BasicLayout',
    Routes: ['src/pages/Authorized'],
    routes: [
      // dashboard
      { path: '/', redirect: '/dashboard/dashboard' },
      {
        path: '/dashboard',
        name: 'dashboard',
        icon: 'dashboard',
        routes: [
          {
            path: '/dashboard/dashboard',
            name: 'dashboard',
            component: './Dashboard/Dashboard',
          },
          {
            path: '/dashboard/display',
            name: 'display',
            routes: [
              {
                path: '/display/digital/:device_id',
                name: 'digital',
                icon: 'dashboard',

                component: './Dashboard/Display/Digital',
              },
              {
                path: '/display/bar/:device_id',
                name: 'bar',
                icon: 'bar-chart',

                component: './Dashboard/Display/Bar',
              },
              {
                path: '/display/line/:device_id',
                name: 'line',
                icon: 'area-chart',
                component: './Dashboard/Display/Line',
              },
            ]
          },
          {
            path: '/dashboard/history/:device_id',
            name: 'history',
            component: './Dashboard/Monitor',
          },
          {
            path: '/dashboard/alarm/:device_id',
            name: 'alarm',
            component: './Dashboard/Alarm',
            hideInMenu: true,

          },
        ],
      },

      // prouct
      {
        path: '/product',
        icon: 'laptop',
        name: 'product',
        routes: [
          {
            path: '/product/product-list',
            name: 'product-list',
            component: './Product/ProductList',
          },
          {
            path: '/product/product-profile/:product_id',
            name: 'product-profile',
            component: './Product/ProductProfile',
          },
        ],
      },


      // device
      {
        path: '/device',
        icon: 'tablet',
        name: 'device',
        routes: [
          {
            path: '/device/device-list',
            name: 'device-list',
            component: './Device/DeviceList',
          },
          {
            path: '/device/device-profile/:device_id',
            name: 'device-profile',
            component: './Device/DeviceProfile',
          },
        ],
      },

      // configuration
      {
        path: '/configuration',
        icon: 'block',
        name: 'configuration',
        routes: [
          {
            path: '/configuration/svg/display',
            name: 'svg-display',
            component: './Configuration/Svg/Display',
          },
         {
            path: '/configuration/svg/editor',
            name: 'svg-editor',
            component: './Configuration/Svg/Editor',
          },
        ],
      },

      //project

      {
        path: '/projects',
        icon: 'schedule',
        name: 'project',
        routes: [
          {
            path: '/projects',
            name: 'project',
            component: './Project/ProjectList',
          },
        ],
      },

      //version

      {
        path: '/version',
        icon: 'save',
        name: 'version',
        routes: [
          {
            path: '/version/changelog',
            name: 'changelog',
            component: './Version/Changelog',
          },
          {
            path: '/version/todolist',
            name: 'todolist',
            component: './Version/Todolist',
          },
          {
            path: '/version/buglist',
            name: 'buglist',
            component: './Bug/BugList',
          },
          {
            path: '/version/bugprofile',
            name: 'bugprofile',
            hideInMenu: true,
            component: './Bug/BugProfile',
          },
        ],
      },

      // forms
      {
        path: '/form',
        icon: 'form',
        name: 'form',
        hideInMenu: true,
        routes: [
          {
            path: '/form/basic-form',
            name: 'basicform',
            component: './Forms/BasicForm',
          },
          {
            path: '/form/step-form',
            name: 'stepform',
            component: './Forms/StepForm',
            hideChildrenInMenu: true,
            routes: [
              {
                path: '/form/step-form',
                name: 'stepform',
                redirect: '/form/step-form/info',
              },
              {
                path: '/form/step-form/info',
                name: 'info',
                component: './Forms/StepForm/Step1',
              },
              {
                path: '/form/step-form/confirm',
                name: 'confirm',
                component: './Forms/StepForm/Step2',
              },
              {
                path: '/form/step-form/result',
                name: 'result',
                component: './Forms/StepForm/Step3',
              },
            ],
          },
          {
            path: '/form/advanced-form',
            name: 'advancedform',
            component: './Forms/AdvancedForm',
          },
        ],
      },
      // list
      {
        path: '/list',
        icon: 'table',
        name: 'list',
        hideInMenu: true,
        routes: [
          {
            path: '/list/table-list',
            name: 'searchtable',
            component: './List/TableList',
          },
          {
            path: '/list/basic-list',
            name: 'basiclist',
            component: './List/BasicList',
          },
          {
            path: '/list/card-list',
            name: 'cardlist',
            component: './List/CardList',
          },
          {
            path: '/list/search',
            name: 'searchlist',
            component: './List/List',
            routes: [
              {
                path: '/list/search',
                redirect: '/list/search/articles',
              },
              {
                path: '/list/search/articles',
                name: 'articles',
                component: './List/Articles',
              },
              {
                path: '/list/search/projects',
                name: 'projects',
                component: './List/Projects',
              },
              {
                path: '/list/search/applications',
                name: 'applications',
                component: './List/Applications',
              },
            ],
          },
        ],
      },
      {
        path: '/profile',
        name: 'profile',
        icon: 'profile',
        hideInMenu: true,
        routes: [
          // profile
          {
            path: '/profile/basic',
            name: 'basic',
            component: './Profile/BasicProfile',
          },
          {
            path: '/profile/advanced',
            name: 'advanced',
            component: './Profile/AdvancedProfile',
          },
        ],
      },
      {
        name: 'result',
        icon: 'check-circle-o',
        path: '/result',
        hideInMenu: true,
        routes: [
          // result
          {
            path: '/result/success',
            name: 'success',
            component: './Result/Success',
          },
          { path: '/result/fail', name: 'fail', component: './Result/Error' },
        ],
      },
      {
        name: 'exception',
        icon: 'warning',
        path: '/exception',
        hideInMenu: true,
        routes: [
          // exception
          {
            path: '/exception/403',
            name: 'not-permission',
            component: './Exception/403',
          },
          {
            path: '/exception/404',
            name: 'not-find',
            component: './Exception/404',
          },
          {
            path: '/exception/500',
            name: 'server-error',
            component: './Exception/500',
          },
          {
            path: '/exception/trigger',
            name: 'trigger',
            hideInMenu: true,
            component: './Exception/TriggerException',
          },
        ],
      },
      {
        name: 'account',
        icon: 'user',
        path: '/account',
        routes: [
          {
            path: '/account/center',
            name: 'center',
            component: './Account/Center/Center',
            routes: [
              {
                path: '/account/center',
                redirect: '/account/center/articles',
              },
              {
                path: '/account/center/articles',
                component: './Account/Center/Articles',
              },
              {
                path: '/account/center/applications',
                component: './Account/Center/Applications',
              },
              {
                path: '/account/center/projects',
                component: './Account/Center/Projects',
              },
            ],
          },
          {
            path: '/account/settings',
            name: 'settings',
            component: './Account/Settings/Info',
            routes: [
              {
                path: '/account/settings',
                redirect: '/account/settings/base',
              },
              {
                path: '/account/settings/base',
                component: './Account/Settings/BaseView',
              },
              {
                path: '/account/settings/security',
                component: './Account/Settings/SecurityView',
              },
              {
                path: '/account/settings/binding',
                component: './Account/Settings/BindingView',
              },
              {
                path: '/account/settings/notification',
                component: './Account/Settings/NotificationView',
              },
            ],
          },
        ],
      },
      {
        component: '404',
      },
    ],
  },
];
