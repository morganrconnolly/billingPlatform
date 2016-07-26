var React = require('react')
var MainContainer = require('../containers/MainContainer')
var SidebarContainer = require('../containers/SidebarContainer')

var Index = React.createClass({
  render: function () {
    return (
      <div>
       	<MainContainer/>
    		<SidebarContainer/>
      </div>
    )
  }
});

module.exports = Index;
