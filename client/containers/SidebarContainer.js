var React = require('react');
var s = require('../css/style.css')
//var StudentList = require('../components/StudentList');

//this should probably be turned into a stateless funcitonal component later
var SidebarContainer = React.createClass({
	render: function() {
		return (
			<div>
			This is the SidebarContainer
			<button className={s.sidebar}>
			HI
			</button>
			</div>




		)
	}


});

module.exports = SidebarContainer;