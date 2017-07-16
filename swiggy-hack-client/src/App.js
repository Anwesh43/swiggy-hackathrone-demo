import React, { Component } from 'react';
import io from 'socket.io-client';

// const socket = io('http://172.16.120.145:9000');

// socket.on('connect', () => {
//   console.log('socket connected');
// });

// socket.on('hello', (data) => {
//   console.log('event: ', data);
// });

// socket.on('new_order', (data) => {
//   console.log('new order: ', data);
// });

// socket.on('disconnect', () => {
//   console.log('socket disconnected');
// });

// {
//   place: 'Koramangala', 
//   restaurant: 'Grameen', 
//   food_item: 'Kashmiri Pulao', 
//   cost: 140.0
// },
// {
//   place: 'Koramangala', 
//   restaurant: 'Grameen', 
//   food_item: 'Kashmiri Pulao', 
//   cost: 140.0
// }

class App extends Component {
  constructor(props) {
    super(props);    
    this.state = {
      orders: [
        
      ],
    }

    this.socket = io('http://172.16.120.185:9000');
    this.socket.on('connect', () => {
      console.log('socket connected');
    });
    this.socket.on('hello', (data) => {
      console.log('event: ', data);
    });

    this.socket.on('new_order', (data) => {
      console.log('new order: ', data);
      const items = this.state.orders;
      items.push(data);
      console.log('order items: ', items);
      this.setState({
        orders: items,
      })
    });

    this.socket.on('disconnect', () => {
      console.log('socket disconnected');
    });
  }

  render() {
    const listItems = this.state.orders.map((order, index) => <li style={{ fontSize: 20 }} key={`${order.food_item}_${index}`} className="collection-item">{`${index + 1}. Food Item: ${order.food_item}, Price: ${order.cost}, Restaurent: ${order.restaurant}, Place: ${order.place}`}</li>);
    console.log('listItems: ', listItems);
    return (
      <div>
        <div style={{ flex: 1, margin: 16 }}>
          <div className="row">
            <h2>Orders</h2>
            <button onClick={() => { this.setState({ orders: [] }) }}>Clear all</button>
          </div>
          <ul className="collection">{listItems}</ul>
        </div>
      </div>
    );
  }
}

export default App;