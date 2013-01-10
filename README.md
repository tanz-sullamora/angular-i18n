angular-i18n
============

<a href="#en">English version</a> <a href="http://tanz-sullamora.github.com/angular-i18n/">Demo</a>

Фильтр для локализации.

Использование:
-------

### обычный текст:
в шаблоне:

    {{'Привет, мир'|i18n}}

в файле locales.js:

    var _locales = { 'ru-ru': { 'Привет, мир': 'Привет, мир' }, 'en-us': { 'Привет, мир': 'Hello, world' } };

### переменные:
в шаблоне:

    {{'%1 яблоко. Весёлый %2'|i18n:'Красное':'мальчик'}}
    
в файле locales.js:

    var _locales = { 'ru-ru': { '%1 яблоко. Весёлый %2': '%1 яблоко. Весёлый %2' }, 'en-us': { '%1 яблоко. Весёлый %2': 'Apple is %1. Happy %2' } };

### множественные формы:
в шаблоне:

    {{'Всего %1 яблоко в %2 корзине'|i18n:'plural':4:'моей'}}
    
в файле locales.js:

     var _locales = {
         'ru-ru': {
             'Всего %1 яблоко в %2 корзине': [
                 'Всего %1 яблоко в %2 корзине',
                 'Всего %1 яблока в %2 корзине',
                 'Всего %1 яблок в %2 корзине'
             ]
         },
         'en-us': {
             'Всего %1 яблоко в %2 корзине': [
                 'There is %1 apple in %2 basket',
                 'There are %1 apples in %2 basket',
             ]
         }
     }

### в js:
в контроллере:

    $filter('i18n')('Строка в js');
    
в файле locales.js:

     var _locales = { 'ru-ru': { 'Строка в js': 'Строка в js' }, 'en-us': { 'Строка в js': 'String in js' } };

с переменными:

    $filter('i18n')('Текущая локаль: %1', $locale.id);
    
в файле locales.js:

     var _locales = { 'ru-ru': { 'Текущая локаль: %1': 'Текущая локаль: %1' }, 'en-us': { 'Текущая локаль: %1': 'Current locale: %1' } };


<a name="en"></a>
English
============

Localization fliter.

Using:
-------

### regular text:
in template:

    {{'Hello, world'|i18n}}

in locales.js:

    var _locales = { 'ru-ru': { 'Hello, world': 'Привет, мир' }, 'en-us': { 'Hello, world': 'Hello, world' } };

### variables:
in template:

    {{'%1 apple. Happy %2'|i18n:'Red':'boy'}}
    
in locales.js:

    var _locales = { 'ru-ru': { '%1 apple. Happy %2': '%1 яблоко. Счастливый %2' }, 'en-us': { '%1 apple. Happy %2': '%1 apple. Happy %2' } };

### plural forms:
in template:

    {{'There is %1 apple in %2 basket'|i18n:'plural':4:'my'}}
    
in locales.js:

     var _locales = {
         'ru-ru': {
             'There is %1 apple in %2 basket': [
                 'Всего %1 яблоко в %2 корзине',
                 'Всего %1 яблока в %2 корзине',
                 'Всего %1 яблок в %2 корзине'
             ]
         },
         'en-us': {
             'There is %1 apple in %2 basket': [
                 'There is %1 apple in %2 basket',
                 'There are %1 apples in %2 basket',
             ]
         }
     }

### in js:
in controller:

    $filter('i18n')('String in js');
    
in locales.js:

     var _locales = { 'ru-ru': { 'String in js': 'Строка в js' }, 'en-us': { 'String in js': 'String in js' } };

with variables:

    $filter('i18n')('Current locale: %1', $locale.id);
    
in locales.js:

     var _locales = { 'ru-ru': { 'Current locale: %1': 'Текущая локаль: %1' }, 'en-us': { 'Current locale: %1': 'Current locale: %1' } };

