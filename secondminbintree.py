class MyNumbers extends React.Component {
  multiplySomeNumbers(n) { //We define the `multiplySomeNumbers` method inside our class declaration because we won't want `multiplySomeNumbers` to be re-created each time the render function is called. Also, if instead we defined this logic inside of `render`, it may be hard to read/understand or convoluted.
    if(n > 10) {
      return n * 5;
    } else if (n > 5) {
      return n * 10;
    } else {
      return n * 2
    }
  }
  render() {
    const n = Math.floor(Math.random() * 12 + 1); //We can keep simple logic like this inside our `render` method.
    return (
    	<div>
      	<h1>The starting number is {n}. After doing some calculations....the number is {this.multiplySomeNumbers(n)}. </h1> 
      </div>
    )
  }
}
