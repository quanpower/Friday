import { isUrl } from '../utils/utils';

const menuData = [
  {
    name: 'dashboard',
    icon: 'dashboard',
    path: 'dashboard',
    children: [
      {
        name: '仪表盘',
        path: 'dashboard',
      },
      {
        name: '监控页',
        path: 'analysis/1',
      },
      {
        name: '记录页',
        path: 'monitor/1',
      },
      {
        name: '报警页',
        path: 'alarm/1',
      },
      {
        name: '分析工作台监控',
        path: 'workplace',
        hideInMenu: true,
        // hideInBreadcrumb: true,
        // hideInMenu: true,
      },
    ],
  },
  {
    name: '产品管理',
    icon: 'laptop',
    path: 'product',
    children: [
      {
        name: '产品列表',
        path: 'product-list',
      },
      {
        name: '产品详情',
        path: 'product-profile/1',
      },
    ],
  },
{
    name: '设备管理',
    icon: 'tablet',
    path: 'device',
    children: [
      {
        name: '设备列表',
        path: 'device-list',
      },
      {
        name: '设备详情',
        path: 'device-profile/1',
      },
    ],
  },

{
    name: '项目页',
    icon: 'calendar',
    path: 'project',
    children: [
      {
        name: '项目',
        path: 'project',
      },
      {
        name: '任务',
        path: 'worker',
      },
    ],
  },

  {
    name: '用户管理',
    icon: 'user',
    path: 'user',
    children: [
      {
        name: '个人资料',
        path: 'profile',
      },
      {
        name: '用户权限',
        path: 'permission',
      },
    ],
  },

  {
    name: '系统设置',
    icon: 'setting',
    path: 'form',
    children: [
      {
        name: '充值',
        path: 'step-form',
      },
    ],
  },

  {
    name: '版本更新',
    icon: 'sync',
    path: 'version',
    children: [
      {
        name: 'ChangeLog',
        path: 'changelog',
      },
      {
        name: 'ToDo',
        path: 'todolist',
      },
    ],
  },

  {
    name: '表单页',
    icon: 'form',
    path: 'form',
    hideInMenu: true,
    children: [
      {
        name: '基础表单',
        path: 'basic-form',
      },
      {
        name: '分步表单',
        path: 'step-form',
      },
      {
        name: '高级表单',
        authority: 'admin',
        path: 'advanced-form',
      },
    ],
  },
  {
    name: '列表页',
    icon: 'table',
    path: 'list',
    hideInMenu: true,
    children: [
      {
        name: '查询表格',
        path: 'table-list',
      },
      {
        name: '标准列表',
        path: 'basic-list',
      },
      {
        name: '卡片列表',
        path: 'card-list',
      },
      {
        name: '搜索列表',
        path: 'search',
        children: [
          {
            name: '搜索列表（文章）',
            path: 'articles',
          },
          {
            name: '搜索列表（项目）',
            path: 'projects',
          },
          {
            name: '搜索列表（应用）',
            path: 'applications',
          },
        ],
      },
    ],
  },
  {
    name: '详情页',
    icon: 'profile',
    path: 'profile',
    hideInMenu: true,
    children: [
      {
        name: '基础详情页',
        path: 'basic',
      },
      {
        name: '高级详情页',
        path: 'advanced',
        authority: 'admin',
      },
    ],
  },
  {
    name: '结果页',
    icon: 'check-circle-o',
    path: 'result',
    hideInMenu: true,
    children: [
      {
        name: '成功',
        path: 'success',
      },
      {
        name: '失败',
        path: 'fail',
      },
    ],
  },
  {
    name: '异常页',
    icon: 'warning',
    path: 'exception',
    hideInMenu: true,
    children: [
      {
        name: '403',
        path: '403',
      },
      {
        name: '404',
        path: '404',
      },
      {
        name: '500',
        path: '500',
      },
      {
        name: '触发异常',
        path: 'trigger',
        hideInMenu: true,
      },
    ],
  },
  {
    name: '账户',
    icon: 'user',
    path: 'user',
    authority: 'guest',
    children: [
      {
        name: '登录',
        path: 'login',
      },
      {
        name: '注册',
        path: 'register',
      },
      {
        name: '注册结果',
        path: 'register-result',
      },
    ],
  },
];

function formatter(data, parentPath = '/', parentAuthority) {
  return data.map(item => {
    let { path } = item;
    if (!isUrl(path)) {
      path = parentPath + item.path;
    }
    const result = {
      ...item,
      path,
      authority: item.authority || parentAuthority,
    };
    if (item.children) {
      result.children = formatter(item.children, `${parentPath}${item.path}/`, item.authority);
    }
    return result;
  });
}

export const getMenuData = () => formatter(menuData);
