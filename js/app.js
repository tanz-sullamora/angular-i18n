'use strict';


/* тестовое приложение */
angular.module('test-app', ['tanzFilters']);

function test($scope, $locale, $filter) {
	$scope.q = 0;

	$scope.jsString = $filter('i18n')('Строка в js');
	$scope.jsString2 = $filter('i18n')('Текущая локаль: %1', $locale.id);

	$scope.setLocale = function(l) {
		$locale.id = l;
		$scope.jsString = $filter('i18n')('Строка в js');
		$scope.jsString2 = $filter('i18n')('Текущая локаль: %1', $locale.id);
	}
}
