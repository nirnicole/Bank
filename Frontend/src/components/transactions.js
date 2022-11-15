import "../styles/Transactions.css"
import React, { Component } from "react"
import Transaction from "./transaction"

class Transactions extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<div className="transactions-container">
				<h1>Transactions:</h1>
				<Transaction></Transaction>
				<Transaction></Transaction>
				<Transaction></Transaction>
			</div>
		)
	}
}

export default Transactions
