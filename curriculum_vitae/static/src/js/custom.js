odoo.define('curriculum_vitae.LanguageSelection', function(require){
    'use strict';

    var UserMenu = require('web.UserMenu');

    UserMenu.include({
        init: function(){
            this._super.apply(this, arguments);
            var self = this;
            var session = this.getSession();
            var lang_list = '';

            self._rpc({
                model: 'res.lang',
                method: 'search_read',
                domain: [],
                fields: ['name', 'code'],
                lazy: false,
            }).then(function(res){
                _.each(res, function(lang){
                    var a = '';
                    if (lang['code'] === session.user_context.lang){
                        a = '<i class="fa fa-check"/>';
                    } else {
                        a = '';
                    }
                    lang_list += '<a href="#" data-lang-menu="lang" data-lang-id="'+lang['code']+'">' +
                    '<img src="curriculum_vitae/static/img/flags/' + lang['code'] + '.png"/>' +
                    lang['name'] + ' ' + a + '</a><br/>';
                });
                $('switch-lang').replaceWith(lang_list);
            })
        },

        start: function(){
            var self = this;
            return this._super.apply(this, arguments).then(function(){
                self.$el.on('click', 'a[data-lang-menu]', function(ev){
                    ev.preventDefault();
                    var f = self['_onMenuLang']
                    f.call(self, $(this));
                });
            });
        },

        _onMenuLang: function(ev){
            var self = this;
            var lang = ($(ev).data("lang-id"));
            var session = this.getSession();
            return this._rpc({
                model: 'res.users',
                method: 'write',
                args: [session.uid, {'lang': lang}],
            }).then(function(result){
                self.do_action({
                    type: 'ir.actions.client',
                    res_model: 'res.users',
                    tag: 'reload_context',
                    target: 'current',
                });
            });
        }
    })
})