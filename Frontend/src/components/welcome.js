import "../styles/Welcome.css"
import React, { Component } from "react"
import { Link } from "react-router-dom"

class Welcome extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<div id="welcome">
				<h1>Welcome to The Chupidala National Bank!</h1>
				<h2>Please login first:</h2>
				<Link to="/login">Log in</Link>
			</div>
		)
	}
}

export default Welcome
