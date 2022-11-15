import "../styles/Balance.css"
import React, { Component } from "react"

class Balance extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return <div id="balance">balance: {this.props.balance}$</div>
	}
}

export default Balance
