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

	deleteTransaction = (id) => {
		const self = this
		const api = axios.create({ baseURL: ROUTES_TRANSACTIONS })
		api.delete(`/${id}`)
			.then((res) => {
				self.componentDidMount()
			})
			.catch((error) => {
				console.log(error)
			})
	}

	async componentDidMount() {
		const response = await this.getTransactions()
		this.setState({ transactions: response.data.transactions })
	}

	render() {
		return (
			<div className="transactions-container">
				<h1>Transactions:</h1>
				{this.state.transactions.map((t, v) => {
					return (
						<Transaction
							key={v}
							details={t}
							deleteTransaction={this.deleteTransaction}
						></Transaction>
					)
				})}
			</div>
		)
	}
}

export default Transactions
