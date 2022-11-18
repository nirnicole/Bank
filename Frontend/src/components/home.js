import "../styles/Home.css"
import React, { Component } from "react"
import { Route } from "react-router-dom"
import Welcome from "./welcome"
import Transactions from "./transactions"
import Operations from "./operations"
import Breakdown from "./breakdown"
import NavBar from "./navbar"
import Balance from "./balance"
import Login from "./login"

class Home extends Component {
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
				<Route exact path="/" render={() => <Welcome />} />
				<Route exact path="/login" render={() => <Login />} />
				<Route
					exact
					path="/transactions"
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
			<div className="App">
				<div className="footer">
					<NavBar></NavBar>
					<Balance balance={this.state.balance}></Balance>
				</div>
				<div id="bank-interface">{this.getAppRoutes()}</div>
			</div>
		)
	}
}

export default Home
