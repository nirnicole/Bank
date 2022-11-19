import "../styles/Home.css"
import React, { Component } from "react"
import { Route } from "react-router-dom"
import Welcome from "./welcome"
import Transactions from "./transactions"
import Operations from "./operations"
import Breakdown from "./breakdown"
import NavBar from "./navbar"
import Balance from "./balance"
import Login from "./authentication/login"
import Unauthorized from "./authentication/unauthorized"
import profile from "../auth/profile"

class Home extends Component {
	constructor() {
		super()
		this.state = {}
	}

	getTransactionsPage = () =>
		profile.userName ? <Transactions></Transactions> : <Unauthorized />
	getOperationsPage = () =>
		profile.userName ? <Operations></Operations> : <Unauthorized />
	getBreakdownPage = () =>
		profile.userName ? <Breakdown></Breakdown> : <Unauthorized />

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
					{profile.userName ? <Balance></Balance> : null}
				</div>
				<div id="bank-interface">{this.getAppRoutes()}</div>
			</div>
		)
	}
}

export default Home
