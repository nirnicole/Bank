import "../styles/Breakdown.css"
import React, { Component } from "react"
import CatagoryItem from "./catagoryItem"
import axios from "axios"

const ROUTES_BREAKDWON = "http://localhost:8000/breakdown"

class Breakdown extends Component {
	constructor() {
		super()
		this.state = {
			categories: [],
		}
	}

	async getBreakdown() {
		return axios.get(ROUTES_BREAKDWON)
	}

	async componentDidMount() {
		const response = await this.getBreakdown()
		console.log(response.data)
		this.setState({ categories: response.data.breakdown })
	}

	render() {
		return (
			<div className="breakdown-container">
				<h1>Breakdown:</h1>
				{this.state.categories.map((c) => {
					return <CatagoryItem details={c}></CatagoryItem>
				})}
			</div>
		)
	}
}

export default Breakdown
