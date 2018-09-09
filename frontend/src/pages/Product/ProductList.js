import React, { PureComponent } from 'react';
import moment from 'moment';
import { connect } from 'dva';
import { Row, Col, Form, Card, Select, List } from 'antd';

import AvatarList from '@/components/AvatarList';
import Ellipsis from '@/components/Ellipsis';

import styles from './ProductList.less';


/* eslint react/no-array-index-key: 0 */
@connect(({ products, loading }) => ({
  products,
  loading: loading.models.products,
}))
export default class ProductList extends PureComponent {
  componentDidMount() {
    this.props.dispatch({
      type: 'products/fetchProducts',
    });
  }


  render() {
    const { products: { products = [] }, loading } = this.props;

    const cardList = products ? (
      <List
        rowKey="id"
        loading={loading}
        grid={{ gutter: 24, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }}
        dataSource={products}
        renderItem={item => (

          <List.Item>
            <Card
              className={styles.card}
              hoverable
              cover={<img alt={item.product_name} src={item.product_avatar} height={154} />}
            >
              <Card.Meta
                title={<a href={`#/product/product-profile/${item.id}`}>{item.product_name}</a>}
                description={<Ellipsis lines={2}>{item.product_description}</Ellipsis>}
              />
              <div className={styles.cardItemContent}>
                <span>{moment(item.gmt_update).fromNow()}</span>
                <div className={styles.avatarList}>
                  <AvatarList size="mini">
                    {item.members.map((member, i) => (
                      <AvatarList.Item
                        key={`${item.id}-avatar-${i}`}
                        src={member.avatar}
                        tips={member.name}
                      />
                    ))}
                  </AvatarList>
                </div>
              </div>
            </Card>
          </List.Item>
        )}
      />
    ) : null;


    return (
      <div className={styles.coverCardList}>
        <div className={styles.cardList}>{cardList}</div>
      </div>
    );
  }
}
