import React, { PureComponent } from 'react';
import { connect } from 'dva';
import { Card, Button, Icon, List } from 'antd';

import Ellipsis from 'components/Ellipsis';
import PageHeaderLayout from '../../layouts/PageHeaderLayout';

import styles from './WorkerList.less';

@connect(({ workers, loading }) => ({
  workers,
  loading: loading.models.workers,
}))


export default class WorkerList extends PureComponent {
  componentDidMount() {
    console.log('this.props')
    console.log(this.props)
    // const search = this.props.location.search;
    const project_name = this.props.match.params.project_name
    console.log(project_name);


    this.props.dispatch({
      type: 'workers/fetchWorkers',
      payload: {
        project_name: project_name,
      },
    });
  }

  render() {
    const { workers: { workers }, loading } = this.props;

    const content = (
      <div className={styles.pageHeaderContent}>
        <p>
          工况简介:...。
        </p>
        <div className={styles.contentLink}>
          <a>
            <img alt="" src="https://gw.alipayobjects.com/zos/rmsportal/MjEImQtenlyueSmVEfUD.svg" />{' '}
            快速开始
          </a>
          <a>
            <img alt="" src="https://gw.alipayobjects.com/zos/rmsportal/NbuDUAuBlIApFuDvWiND.svg" />{' '}
            产品简介
          </a>
          <a>
            <img alt="" src="https://gw.alipayobjects.com/zos/rmsportal/ohOEPSYdDTNnyMbGuyLb.svg" />{' '}
            产品文档
          </a>
        </div>
      </div>
    );

    const extraContent = (
      <div className={styles.extraImg}>
        <img
          alt="这是一个标题"
          src="https://gw.alipayobjects.com/zos/rmsportal/RzwpdLnhmvDJToTdfDPe.png"
        />
      </div>
    );

    return (
      <PageHeaderLayout title="工况列表" content={content} extraContent={extraContent}>
        <div className={styles.cardList}>
          <List
            rowKey="id"
            loading={loading}
            grid={{ gutter: 24, lg: 3, md: 2, sm: 1, xs: 1 }}
            dataSource={['', ...workers]}
            renderItem={item =>
              item ? (
                <List.Item key={item.id}>
                  <Card hoverable className={styles.card} actions={[<a>操作一</a>, <a>操作二</a>]}>
                    <Card.Meta
                      avatar={<img alt="" className={styles.cardAvatar} src={item.avatar} />}
                      title={<a href={item.href}>{item.title}</a>}
                      description={
                        <Ellipsis className={styles.item} lines={3}>
                          {item.createdAt}
                        </Ellipsis>
                      }
                    />
                  </Card>
                </List.Item>
              ) : (
                <List.Item>
                  <Button type="dashed" className={styles.newButton}>
                    <Icon type="plus" /> 新增产品
                  </Button>
                </List.Item>
              )
            }
          />
        </div>
      </PageHeaderLayout>
    );
  }
}
