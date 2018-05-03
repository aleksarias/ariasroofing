var CustomerLanding = React.createClass({

    getInitialState: function () {
      return {customText: ""};
    },

    componentDidMount: function() {
        $.getJSON('../api/users/' + profilepk + '.json', function(result) {
        if (this.isMounted()) {
            this.setState({
            user_data: result
            });
        }
    }.bind(this));
},

    customClickFunction: function (){
        this.setState({customText: "You clicked the button! :P "});
    },


    render: function () {
        var data = this.state.user_data;
        console.log(data);
       return (
                <div>
                    <div className="row">
                        <form method="POST" action="">
                            <div className="col-xs-6">
                                <h2>Mailing Address</h2>
                                <input type="submit" value="Update" />
                                <h2>Account Summary</h2>
                                <h3>Jobs</h3>
                                    Job ID:<br />
                                    Address:<br/>
                            </div>
                            <div className="col-xs-6">
                                <h2>Referrals</h2>
                                <input type="submit" value="Add New" />
                            </div>
                        </form>
                    </div>
                </div>
        )
   }
});


React.render(
    <CustomerLanding />,
    document.getElementById('js-container')
);