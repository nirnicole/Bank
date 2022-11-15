import "./App.css"
import { BrowserRouter as Router, Route } from "react-router-dom"
import React, { Component } from "react"
import Transactions from "./components/transactions"
import Operations from "./components/operations"
import Breakdown from "./components/breakdown"
import NavBar from "./components/navbar"
import Balance from "./components/balance"

class App extends Component {
	constructor() {
		super()
		this.state = { balance: 2500 }
	}

	getTransactionsPage = () => <Transactions></Transactions>
	getOperationsPage = () => <Operations></Operations>
	getBreakdownPage = () => <Breakdown></Breakdown>

	getAppRoutes = () => {
		return (
			<div className="routs-container">
				<Route
					exact
					path="/"
					render={() => this.getTransactionsPage()}
				/>
				<Route
					exact
					path="/operations"
					render={() => this.getOperationsPage()}
				/>
				<Route
					exact
					path="/breakdown"
					render={() => this.getBreakdownPage()}
				/>
			</div>
		)
	}

	render() {
		return (
			<Router>
				<div className="App">
					<div className="footer">
						<NavBar></NavBar>
						<Balance balance={this.state.balance}></Balance>
					</div>
					<div id="bank-interface">{this.getAppRoutes()}</div>
				</div>
			</Router>
		)
	}
}

export default App
