import "../styles/Transactions.css"
import React, { Component } from "react"
import Transaction from "./transaction"
import axios from "axios"

const ROUTES_TRANSACTIONS = "http://localhost:8000/transactions"

class Transactions extends Component {
	constructor() {
		super()
		this.state = {
			transactions: [],
		}
	}

	async getTransactions() {
		return axios.get(ROUTES_TRANSACTIONS)
	}

	async componentDidMount() {
		const response = await this.getTransactions()
		console.log(response.data)
		this.setState({ transactions: response.data.transactions })
	}

	render() {
		return (
			<div className="transactions-container">
				<h1>Transactions:</h1>
				{this.state.transactions.map((t) => {
					return <Transaction details={t}></Transaction>
				})}
			</div>
		)
	}
}

export default Transactions
