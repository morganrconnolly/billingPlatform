//adding multiple pages requires adding ReactRouter and a routes utility. 
//Which will be fun! but I should get a grasp on the main page first.

var MainContainer = require('../components/MainContainer')

export default class BillingPage extends Component {

  render() {


    return (
      <div>
      	Hello! This is your billing page, reporting for duty.
        <MainContainer />
      </div>
    );
  }
}