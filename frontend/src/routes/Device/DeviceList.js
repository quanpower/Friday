import React, { PureComponent } from 'react';
import numeral from 'numeral';
import { connect } from 'dva';
import { Row, Col, Form, Card, Select, Icon, Avatar, List, Tooltip, Dropdown, Menu } from 'antd';


import styles from './Applications.less';


/* eslint react/no-array-index-key: 0 */
@connect(({ devices, loading }) => ({
  devices,
  loading: loading.models.devices,
}))
export default class DeviceList extends PureComponent {
  componentDidMount() {
    this.props.dispatch({
      type: 'devices/fetchDevices',
    });
  }


  render() {
    const { devices: { devices }, loading, form } = this.props;
    
    const CardInfo = ({ status, updateAt }) => (
      <div className={styles.cardInfo}>
        <div>
          <p>当前状态</p>
          <p>{status}</p>
        </div>
        <div>
          <p>更新时间</p>
          <p>{updateAt}</p>
        </div>
      </div>
    );

    const itemMenu = (
      <Menu>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="http://www.alipay.com/">
            1st menu item
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="http://www.taobao.com/">
            2nd menu item
          </a>
        </Menu.Item>
        <Menu.Item>
          <a target="_blank" rel="noopener noreferrer" href="http://www.tmall.com/">
            3d menu item
          </a>
        </Menu.Item>
      </Menu>
    );

    return (
      <div className={styles.filterCardList}>


        <List
          rowKey="id"
          style={{ marginTop: 24 }}
          grid={{ gutter: 24, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }}
          loading={loading}
          dataSource={devices}
          renderItem={item => (
            <List.Item key={item.id}>
              <Card
                hoverable
                bodyStyle={{ paddingBottom: 20 }}
                actions={[
                  <Tooltip title="下载">
                    <Icon type="download" />
                  </Tooltip>,
                  <Tooltip title="编辑">
                    <Icon type="edit" />
                  </Tooltip>,
                  <Tooltip title="分享">
                    <Icon type="share-alt" />
                  </Tooltip>,
                  <Dropdown overlay={itemMenu}>
                    <Icon type="ellipsis" />
                  </Dropdown>,
                ]}
              >
                <Card.Meta avatar={<Avatar size="small" src={item.avatar} />} title={item.name} />
                <div className={styles.cardItemContent}>
                  <CardInfo
                    status={item.status}
                    updateAt={item.gmt_online}
                  />
                </div>
              </Card>
            </List.Item>
          )}
        />
      </div>
    );
  }
}
