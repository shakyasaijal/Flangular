app.controller('logoutCtrl',['$scope', '$auth' function($scope, $auth,$http){
   $scope.submit = function() {
    	$auth.logout().then(function (response) {
	        $state.go('login.html');
	    }).catch(function (response) {
	        console.log('failure signout!')

	    })
    }
   }]);
