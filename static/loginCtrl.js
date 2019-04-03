app.controller('loginCtrl',['$scope', '$auth','$routeChangeSuccess' function($scope, $auth,$http,$routeChangeSuccess){
  $scope.submitForm = function(){
     var j = {
        "email":$scope.email,
        "password":$scope.password,
       };

     $http({
			method:"POST",
			url: '/auth/login'
			data: j
		}).then(function mySuccess(response){
			$scope.data = response.data;
			redirectTo: '/index.html'


      }).function myError(response) {
	        alert(response.statusText);
	        redirectTo: '/index.html'
        };
	 }
   }]);
