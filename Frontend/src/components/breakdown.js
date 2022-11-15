import "../styles/Breakdown.css"
import React, { Component } from "react"
import CatagoryItem from "./catagoryItem"

class Breakdown extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<div className="breakdown-container">
				<h1>Breakdown:</h1>
				<CatagoryItem></CatagoryItem>
				<CatagoryItem></CatagoryItem>
				<CatagoryItem></CatagoryItem>
			</div>
		)
	}
}

export default Breakdown
