var DynamicSearch = React.createClass({

  // sets initial state
  getInitialState: function(){
    return { searchString: '' };
  },

  // sets state, triggers render method
  handleChange: function(event){
    // grab value form input box
    this.setState({searchString:event.target.value});
    console.log("scope updated!");
  },

  render: function() {

    var showDates = this.props.items;
    var searchString = this.state.searchString.trim().toLowerCase();

    // filter showDates list by value from input box
    if(searchString.length > 0){
      showDates = showDates.filter(function(show){
        return show.name.toLowerCase().match( searchString );
      });
    }

    return (
      <div>
        <input type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="Search!" />
        <ul>
          { showDates.map(function(show){ return <li>{show.name} </li> }) }
        </ul>
      </div>
    )
  }

});

// list of showDates, defined with JavaScript object literals
var showDates = [
  {"name": "1984-01-20"}, {"name": "1985-02-20"}, {"name": "1999-01-20"}, {"name": "2000-02-25"}
];

ReactDOM.render(
  <DynamicSearch items={ showDates } />,
  document.getElementById('main')
);