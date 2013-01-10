'use strict';

/*
 * фильтр для локализации.
 * использование:
 *
 *  обычный текст:
 *  - {{'Привет, мир'|i18n}}
 *    в файле locales.js:
 *    var _locales = { 'ru-ru': { 'Привет, мир': 'Привет, мир' }, 'en-us': { 'Привет, мир': 'Hello, world' } };
 *
 *  переменные:
 *  - {{'%1 яблоко. Весёлый %2'|i18n:'Красное':'мальчик'}}
 *    в файле locales.js:
 *    var _locales = { 'ru-ru': { '%1 яблоко. Весёлый %2': '%1 яблоко. Весёлый %2' }, 'en-us': { '%1 яблоко. Весёлый %2': 'Apple is %1. Happy %2' } };
 *
 *  склонения:
 *  - {{'Всего %1 яблоко в %2 корзине'|i18n:'plural':4:'моей'}}
 *    в файле locales.js:
 *    var _locales = {
 *        'ru-ru': {
 *            'Всего %1 яблоко в %2 корзине': [
 *                'Всего %1 яблоко в %2 корзине',
 *                'Всего %1 яблока в %2 корзине',
 *                'Всего %1 яблок в %2 корзине'
 *            ]
 *        },
 *        'en-us': {
 *            'Всего %1 яблоко в %2 корзине': [
 *                'There is %1 apple in %2 basket',
 *                'There are %1 apples in %2 basket',
 *            ]
 *        }
 *    }
 *
 *  в js:
 *  - $filter('i18n')('Строка в js');
 *    в файле locales.js:
 *    var _locales = { 'ru-ru': { 'Строка в js': 'Строка в js' }, 'en-us': { 'Строка в js': 'String in js' } };
 *
 *  - $filter('i18n')('Текущая локаль: %1', $locale.id);
 *    var _locales = { 'ru-ru': { 'Текущая локаль: %1': 'Текущая локаль: %1' }, 'en-us': { 'Текущая локаль: %1': 'Current locale: %1' } };
 *
 */

angular.module('tanzFilters', []);

angular.module('tanzFilters', []).filter('i18n', function($locale) {
	return function(str) {
		var offset = 1;
		if (arguments[1] && arguments[1] === 'plural') {
			var n = arguments[2],
					plural;

			switch ($locale.id) {
				case 'en-us':
					plural = 0 + (n != 1);
					break;
				case 'ru-ru':
					plural = (n % 10 == 1 && n % 100 != 11 ? 0 : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20) ? 1 : 2);
					break;
				default:
					plural = 0 + (n != 1);
			}

			str = _locales[$locale.id][str][plural] || str;
			offset = 2;
		} else {
			str = _locales[$locale.id][str] || str;
		}

		for (var i = offset; i < arguments.length; i++) {
			str = str.split('%' + (i - offset + 1)).join(arguments[i]);
		}

		return str;
	}
});