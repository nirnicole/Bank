import "../styles/Operations.css"
import React, { Component } from "react"

class Operations extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<div className="operations-container">
				<h1>Insert Transaction</h1>
				<label>Transaction amount</label>
				<input></input>
				<label>Transaction vendor</label>
				<input></input>
				<label>Transaction catagory</label>
				<input></input>
				<button>Deposit</button>
				<button>Withdraw</button>
			</div>
		)
	}
}

export default Operations
