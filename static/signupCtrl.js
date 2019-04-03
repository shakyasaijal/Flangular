app.controller("signupCtrl",function($scope,$http){
  $scope.submitForm = function(){
     var j = {
        "email":$scope.email,
        "password":$scope.password,
       };

     $http.post("/auth/signup", j)
     .then(function (response){
        alert('Success');
     },function (error){
        alert('Error');
     });
   };
});
