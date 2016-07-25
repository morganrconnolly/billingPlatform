//excluding private compononents, one compononent per file??

var React = require('react');

//will have no props
function SidebarContainer(props) {
	return (
			<div>

			</div>
		)
}

//what form will the student data be in when it's passed to student list?
//it will be passed to react by the back end, so I get to choose.
var StudentList = React.createClass({

});



//Will take in the list of students for the currently logged in user.
StudentList.propTypes = {

}

module.exports = SidebarContainer