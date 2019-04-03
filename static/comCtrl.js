app.controller("comCtrl",function($scope,$http, $routeParams){
	$http({
			method:"GET",
			url: 'https://api.github.com/repos/'+$routeParams.owner+'/'+$routeParams.repo+'/issues/'+$routeParams.number+'/comments'
		}).then(function mySuccess(response){
			$scope.data = response.data;
		},function myError(response){
			alert(response.statusText);
		}); 
});
