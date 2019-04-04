var app = angular.module("myApp",["ngRoute", "satellizer"]);
console.log("sdvlknl -----> ");



app.config(function($routeProvider){
	$routeProvider
	.when("/",{
		templateUrl : "static/main.html",
		controller : "myCtrl"
	})
	.when("/IssueIdComments/:owner/:repo/:number",{
		templateUrl : "static/comments.html",
		controller : "comCtrl"
	})
	.when("/signup",{
	    templateUstaticrl : "/signup.html",
	    controller : "signupCtrl"
	})
	.when("/login",{
	    templateUrl : "static/login.html",
	    controller : "loginCtrl"
	})
	.when("/logout",{
	    templateUrl : "static/login.html",
	    controller : "logoutCtrl"
	});
});

app.run(function ($rootScope, $auth) {
    $rootScope.$on('$routeChangeStart',
        function (event, toState) {
            var requiredLogin = false;
            if (toState.data && toState.data.requiredLogin)
                requiredLogin = true;

            if (requiredLogin && !$auth.isAuthenticated()) {
                event.preventDefault();
               $state.go('login');
        }
    });

});
