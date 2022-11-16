import "../styles/Transaction.css"
import React, { Component } from "react"

class Transaction extends Component {
	constructor() {
		super()
		this.state = {}
	}

	_getCostClass = (cost) => (cost >= 0 ? "cost-positive" : "cost-negetive")

	render() {
		let transaction = this.props.details
		let cost = transaction.TransactionAmount
		return (
			<div className="transaction-container">
				<label className="item">{transaction.TransactionVendor}</label>
				<label className={this._getCostClass(cost)}>{cost}</label>
				<label className="catagory">
					{transaction.TransactionCategory}
				</label>
				<button className="button">Delete</button>
			</div>
		)
	}
}

export default Transaction
