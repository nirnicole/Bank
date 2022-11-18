import "./App.css"
import { BrowserRouter as Router } from "react-router-dom"
import React, { Component } from "react"
import Home from "./components/home"

class App extends Component {
	constructor() {
		super()
		this.state = {}
	}

	render() {
		return (
			<Router>
				<Home />
			</Router>
		)
	}
}

export default App
