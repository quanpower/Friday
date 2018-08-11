import React, { PureComponent } from 'react';
import moment from 'moment';
import { connect } from 'dva';
import { Row, Col, Form, Card, Select, List } from 'antd';
import { Button, Modal, Form, Input, Radio } from 'antd';



import styles from './ProductList.less';


/* eslint react/no-array-index-key: 0 */
@connect(({ bug, loading }) => ({
  bug,
  loading: loading.models.bug,
}))


const FormItem = Form.Item;

const CollectionCreateForm = Form.create()(
  class extends React.Component {
    render() {
      const { visible, onCancel, onCreate, form } = this.props;
      const { getFieldDecorator } = form;
      return (
        <Modal
          visible={visible}
          title="Create a new collection"
          okText="Create"
          onCancel={onCancel}
          onOk={onCreate}
        >
          <Form layout="vertical">
            <FormItem label="Title">
              {getFieldDecorator('title', {
                rules: [{ required: true, message: 'Please input the title of collection!' }],
              })(
                <Input />
              )}
            </FormItem>
            <FormItem label="Description">
              {getFieldDecorator('description')(<Input type="textarea" />)}
            </FormItem>
            <FormItem className="collection-create-form_last-form-item">
              {getFieldDecorator('modifier', {
                initialValue: 'public',
              })(
                <Radio.Group>
                  <Radio value="public">Public</Radio>
                  <Radio value="private">Private</Radio>
                </Radio.Group>
              )}
            </FormItem>
          </Form>
        </Modal>
      );
    }
  }
);

export default class Bug extends PureComponent {
  componentDidMount() {
    this.props.dispatch({
      type: 'bug/fetchBugs',
    });
  }


  render() {
    const { bugs: { products = [] }, loading } = this.props;

    state = {
        visible: false,
      };

    showModal = () => {
      this.setState({ visible: true });
    }

    handleCancel = () => {
      this.setState({ visible: false });
    }

    handleCreate = () => {
      const form = this.formRef.props.form;
      form.validateFields((err, values) => {
        if (err) {
          return;
        }

        console.log('Received values of form: ', values);
        form.resetFields();
        this.setState({ visible: false });
      });
    }

    saveFormRef = (formRef) => {
      this.formRef = formRef;
    }

    return (
      <div>
        <Button type="primary" onClick={this.showModal}>New Collection</Button>
        <CollectionCreateForm
          wrappedComponentRef={this.saveFormRef}
          visible={this.state.visible}
          onCancel={this.handleCancel}
          onCreate={this.handleCreate}
        />
      </div>
    );
  }
}

