app.controller("myCtrl", function($scope,$http){
	console.log("sdvlknl -----> 4");

	console.log("sdvlknl -----> 3");

	$scope.myFunction = function(){
		var components = $scope.url.split("/");
		$scope.owner = components[0];
		$scope.repo = components[1];
		$http({
			method:"GET",
			url: 'https://api.github.com/repos/'+$scope.owner+'/'+$scope.repo+'/issues'
		}).then(function mySuccess(response){
			$scope.data = response.data;
		},function myError(response){
			alert(response.statusText);
		});
	};

});

