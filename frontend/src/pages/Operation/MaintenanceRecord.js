import React, { Component, Fragment } from 'react';
import { connect } from 'dva';
import {
  Button,
  Menu,
  Dropdown,
  Icon,
  Row,
  Col,
  Steps,
  Card,
  Popover,
  Badge,
  Table,
  Tooltip,
  Divider,
} from 'antd';
import classNames from 'classnames';
import PageHeaderWrapper from '@/components/PageHeaderWrapper';
import styles from './MaintenanceRecord.less';


const operationTabList = [
  {
    key: 'tab1',
    tab: '维修记录',
  },
  {
    key: 'tab2',
    tab: '保养记录',
  },
  {
    key: 'tab3',
    tab: '升级记录',
  },
];

const columns = [
  {
    title: '操作类型',
    dataIndex: 'type',
    key: 'type',
  },
  {
    title: '操作人',
    dataIndex: 'name',
    key: 'name',
  },
  {
    title: '执行结果',
    dataIndex: 'status',
    key: 'status',
    render: text =>
      text === 'agree' ? (
        <Badge status="success" text="成功" />
      ) : (
        <Badge status="error" text="失败" />
      ),
  },
  {
    title: '操作时间',
    dataIndex: 'updatedAt',
    key: 'updatedAt',
  },
  {
    title: '备注',
    dataIndex: 'memo',
    key: 'memo',
  },
];

@connect(({ operation, loading }) => ({
  operation,
  loading: loading.effects['operation/fetchAdvanced'],
}))

class AdvancedProfile extends Component {
  state = {
    operationkey: 'tab1',
  };

  componentDidMount() {
    const { dispatch } = this.props;
    dispatch({
      type: 'operation/fetchAdvanced',
    });

  }

  componentWillUnmount() {
  }

  onOperationTabChange = key => {
    this.setState({ operationkey: key });
  };


  render() {
    const { stepDirection, operationkey } = this.state;
    const { operation, loading } = this.props;
    const { advancedOperation1, advancedOperation2, advancedOperation3 } = operation;
    
    const contentList = {
      tab1: (
        <Table
          pagination={false}
          loading={loading}
          dataSource={advancedOperation1}
          columns={columns}
        />
      ),
      tab2: (
        <Table
          pagination={false}
          loading={loading}
          dataSource={advancedOperation2}
          columns={columns}
        />
      ),
      tab3: (
        <Table
          pagination={false}
          loading={loading}
          dataSource={advancedOperation3}
          columns={columns}
        />
      ),
    };

    return (
      <PageHeaderWrapper
        title="维护记录"
        logo={
          <img alt="" src="https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png" />
        }

      >

        <Card
          className={styles.tabsCard}
          bordered={false}
          tabList={operationTabList}
          onTabChange={this.onOperationTabChange}
        >
          {contentList[operationkey]}
        </Card>
      </PageHeaderWrapper>
    );
  }
}

export default AdvancedProfile;
