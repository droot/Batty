(function() {
  var AppController, AppModel, EventDispatcher, NavBar, ScheduleView, SessionCollection, SessionModel, SessionView, SpeakerCollection, SpeakerItemView, SpeakerModel, SpeakerView, TweetCollection, TweetModel, TweetView, TwitterView, initialize_app, page_change_handler, root;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
  root = typeof exports != "undefined" && exports !== null ? exports : this;
  EventDispatcher = {
    EVENT_TYPE_USER_ACTION: 'user_action',
    EVENT_SUBTYPE_SWITCH_VIEW: 'switch_view'
  };
  _.extend(EventDispatcher, Backbone.Events);
  SpeakerModel = (function() {
    function SpeakerModel() {
      SpeakerModel.__super__.constructor.apply(this, arguments);
    }
    __extends(SpeakerModel, Backbone.Model);
    return SpeakerModel;
  })();
  SpeakerCollection = (function() {
    function SpeakerCollection() {
      SpeakerCollection.__super__.constructor.apply(this, arguments);
    }
    __extends(SpeakerCollection, Backbone.Collection);
    SpeakerCollection.prototype.model = SpeakerModel;
    return SpeakerCollection;
  })();
  SpeakerItemView = (function() {
    function SpeakerItemView() {
      this.render = __bind(this.render, this);;
      this.initialize = __bind(this.initialize, this);;      SpeakerItemView.__super__.constructor.apply(this, arguments);
    }
    __extends(SpeakerItemView, Backbone.View);
    SpeakerItemView.prototype.tagName = 'li';
    SpeakerItemView.prototype.initialize = function() {
      this.template = $('#speaker-template').template();
      return this.model.bind('change', this.render);
    };
    SpeakerItemView.prototype.events = {
      'click': "click_handler"
    };
    SpeakerItemView.prototype.click_handler = function(ev) {
      return ev.preventDefault();
    };
    SpeakerItemView.prototype.render = function() {
      $(this.el).html($.tmpl(this.template, this.model.toJSON()));
      return this;
    };
    return SpeakerItemView;
  })();
  SpeakerView = (function() {
    function SpeakerView() {
      this.hide = __bind(this.hide, this);;
      this.show = __bind(this.show, this);;
      this.refreshAll = __bind(this.refreshAll, this);;
      this.render = __bind(this.render, this);;      SpeakerView.__super__.constructor.apply(this, arguments);
    }
    __extends(SpeakerView, Backbone.View);
    SpeakerView.prototype.initialize = function() {
      return this.model.speakers.bind('reset', this.refreshAll);
    };
    SpeakerView.prototype.render = function() {
      return this;
    };
    SpeakerView.prototype.refreshAll = function() {
      this.$('#speaker-list').html('');
      this.$('#speaker-list').listview();
      this.model.speakers.each(function(speaker) {
        var view;
        view = new SpeakerItemView({
          model: speaker
        });
        return this.$('#speaker-list').append(view.render().el);
      });
      return this.$('#speaker-list').listview('refresh');
    };
    SpeakerView.prototype.show = function() {
      return $(this.el).show();
    };
    SpeakerView.prototype.hide = function() {
      return $(this.el).hide();
    };
    SpeakerView.prototype.showLoading = function() {
      return $.mobile.pageLoading();
    };
    SpeakerView.prototype.hideLoading = function() {
      return $.mobile.pageLoading(true);
    };
    return SpeakerView;
  })();
  SessionModel = (function() {
    function SessionModel() {
      SessionModel.__super__.constructor.apply(this, arguments);
    }
    __extends(SessionModel, Backbone.Model);
    return SessionModel;
  })();
  SessionCollection = (function() {
    function SessionCollection() {
      SessionCollection.__super__.constructor.apply(this, arguments);
    }
    __extends(SessionCollection, Backbone.Collection);
    SessionCollection.prototype.model = SessionModel;
    return SessionCollection;
  })();
  SessionView = (function() {
    function SessionView() {
      this.render = __bind(this.render, this);;
      this.initialize = __bind(this.initialize, this);;      SessionView.__super__.constructor.apply(this, arguments);
    }
    __extends(SessionView, Backbone.View);
    SessionView.prototype.tagName = 'li';
    SessionView.prototype.initialize = function() {
      this.template = $('#session-template').template();
      return this.model.bind('change', this.render);
    };
    SessionView.prototype.events = {
      'click': "click_handler"
    };
    SessionView.prototype.click_handler = function(ev) {
      return ev.preventDefault();
    };
    SessionView.prototype.render = function() {
      $(this.el).html($.tmpl(this.template, this.model.toJSON()));
      $(this.el).attr('data-role', "list-divider");
      return this;
    };
    return SessionView;
  })();
  ScheduleView = (function() {
    function ScheduleView() {
      this.hide = __bind(this.hide, this);;
      this.show = __bind(this.show, this);;
      this.refreshAll = __bind(this.refreshAll, this);;
      this.render = __bind(this.render, this);;      ScheduleView.__super__.constructor.apply(this, arguments);
    }
    __extends(ScheduleView, Backbone.View);
    ScheduleView.prototype.initialize = function() {
      return this.model.sessions.bind('reset', this.refreshAll);
    };
    ScheduleView.prototype.render = function() {
      return this;
    };
    ScheduleView.prototype.refreshAll = function() {
      this.$('#session-list').html('');
      this.$('#session-list').listview();
      this.model.sessions.each(function(session) {
        var view;
        view = new SessionView({
          model: session
        });
        return this.$('#session-list').append(view.render().el);
      });
      return this.$('#session-list').listview('refresh');
    };
    ScheduleView.prototype.show = function() {
      return $(this.el).show();
    };
    ScheduleView.prototype.hide = function() {
      return $(this.el).hide();
    };
    ScheduleView.prototype.showLoading = function() {
      return $.mobile.pageLoading();
    };
    ScheduleView.prototype.hideLoading = function() {
      return $.mobile.pageLoading(true);
    };
    return ScheduleView;
  })();
  TweetModel = (function() {
    function TweetModel() {
      TweetModel.__super__.constructor.apply(this, arguments);
    }
    __extends(TweetModel, Backbone.Model);
    return TweetModel;
  })();
  TweetCollection = (function() {
    function TweetCollection() {
      TweetCollection.__super__.constructor.apply(this, arguments);
    }
    __extends(TweetCollection, Backbone.Collection);
    TweetCollection.prototype.model = TweetModel;
    return TweetCollection;
  })();
  TweetView = (function() {
    function TweetView() {
      this.render = __bind(this.render, this);;
      this.initialize = __bind(this.initialize, this);;      TweetView.__super__.constructor.apply(this, arguments);
    }
    __extends(TweetView, Backbone.View);
    TweetView.prototype.tagName = 'li';
    TweetView.prototype.initialize = function() {
      this.template = $('#tweet-template').template();
      return this.model.bind('change', this.render);
    };
    TweetView.prototype.events = {
      'click': "click_handler"
    };
    TweetView.prototype.click_handler = function(ev) {};
    TweetView.prototype.render = function() {
      $(this.el).html($.tmpl(this.template, this.model.toJSON()));
      return this;
    };
    return TweetView;
  })();
  TwitterView = (function() {
    function TwitterView() {
      this.refreshAll = __bind(this.refreshAll, this);;
      this.hide = __bind(this.hide, this);;
      this.show = __bind(this.show, this);;
      this.render = __bind(this.render, this);;      TwitterView.__super__.constructor.apply(this, arguments);
    }
    __extends(TwitterView, Backbone.View);
    TwitterView.prototype.initialize = function() {
      return this.model.tweets.bind('reset', this.refreshAll);
    };
    TwitterView.prototype.render = function() {
      return this;
    };
    TwitterView.prototype.show = function() {
      return $(this.el).show();
    };
    TwitterView.prototype.hide = function() {
      return $(this.el).hide();
    };
    TwitterView.prototype.refreshAll = function() {
      this.$('#tweet-list').html('');
      this.$('#tweet-list').listview();
      this.model.tweets.each(function(tweet) {
        var view;
        view = new TweetView({
          model: tweet
        });
        return this.$('#tweet-list').append(view.render().el);
      });
      return this.$('#tweet-list').listview('refresh');
    };
    TwitterView.prototype.showLoading = function() {
      return $.mobile.pageLoading();
    };
    TwitterView.prototype.hideLoading = function() {
      return $.mobile.pageLoading(true);
    };
    return TwitterView;
  })();
  AppModel = (function() {
    function AppModel() {
      AppModel.__super__.constructor.apply(this, arguments);
    }
    __extends(AppModel, Backbone.Model);
    AppModel.prototype.initialize = function() {
      this.tweets = new TweetCollection();
      this.sessions = new SessionCollection();
      return this.speakers = new SpeakerCollection();
    };
    return AppModel;
  })();
  NavBar = (function() {
    function NavBar() {
      this.click_handler = __bind(this.click_handler, this);;      NavBar.__super__.constructor.apply(this, arguments);
    }
    __extends(NavBar, Backbone.View);
    NavBar.prototype.initialize = function() {};
    NavBar.prototype.events = {
      'click li': 'click_handler'
    };
    NavBar.prototype.click_handler = function(ev) {
      var $current_target, id;
      $current_target = $(ev.currentTarget);
      id = "" + ($current_target.attr('id'));
      return EventDispatcher.trigger(EventDispatcher.EVENT_TYPE_USER_ACTION, EventDispatcher.EVENT_SUBTYPE_SWITCH_VIEW, id);
    };
    return NavBar;
  })();
  AppController = (function() {
    function AppController() {
      this.load_session_view = __bind(this.load_session_view, this);;
      this.load_speaker_view = __bind(this.load_speaker_view, this);;
      this.twitter_response_callback = __bind(this.twitter_response_callback, this);;
      this.load_twitter_view = __bind(this.load_twitter_view, this);;
      this.show_view = __bind(this.show_view, this);;
      this.event_handler = __bind(this.event_handler, this);;
      this.initialize = __bind(this.initialize, this);;      AppController.__super__.constructor.apply(this, arguments);
    }
    __extends(AppController, Backbone.Router);
    AppController.prototype.initialize = function(args) {
      this.model = new AppModel(args);
      this.nav_bar = new NavBar({
        model: this.model,
        el: $('#nav-bar')
      });
      this.twitter_view = new TwitterView({
        model: this.model,
        el: $('#twitter-view')
      });
      this.schedule_view = new ScheduleView({
        model: this.model,
        el: $('#session-view')
      });
      this.speaker_view = new SpeakerView({
        model: this.model,
        el: $('#speaker-view')
      });
      this.views = [this.twitter_view, this.schedule_view, this.speaker_view];
      EventDispatcher.bind(EventDispatcher.EVENT_TYPE_USER_ACTION, this.event_handler);
      EventDispatcher.trigger(EventDispatcher.EVENT_TYPE_USER_ACTION, EventDispatcher.EVENT_SUBTYPE_SWITCH_VIEW, 'schedule');
      return this;
    };
    AppController.prototype.event_handler = function(e_type, e_data) {
      switch (e_type) {
        case EventDispatcher.EVENT_SUBTYPE_SWITCH_VIEW:
          return this.show_view(e_data);
      }
    };
    AppController.prototype.show_view = function(e_data) {
      var v, _fn, _i, _len, _ref;
      _ref = this.views;
      _fn = function(v) {
        return v.hide();
      };
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        v = _ref[_i];
        _fn(v);
      }
      switch (e_data) {
        case 'schedule':
          this.schedule_view.show();
          return this.load_session_view();
        case 'twitter':
          this.twitter_view.show();
          return this.load_twitter_view(this.model.get('tw_kwd'));
        case 'speakers':
          this.speaker_view.show();
          return this.load_speaker_view();
      }
    };
    AppController.prototype.load_twitter_view = function(term) {
      var query_url;
      if (this.model.tweets.length > 0) {
        return;
      }
      this.twitter_view.showLoading();
      query_url = "http://search.twitter.com/search.json?lang=en&callback=?&q=" + term;
      $.getJSON(query_url, this.twitter_response_callback);
      return this;
    };
    AppController.prototype.twitter_response_callback = function(data) {
      var app, t_coll, x, _fn, _i, _len, _ref;
      this.twitter_view.hideLoading();
      app = this;
      t_coll = [];
      _ref = data.results;
      _fn = function(x) {
        var tweet;
        tweet = new TweetModel({
          screen_name: x.from_user,
          text: x.text,
          profile_pic: x.profile_image_url
        });
        return t_coll.push(tweet);
      };
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        x = _ref[_i];
        _fn(x);
      }
      app.model.tweets.reset(t_coll);
    };
    AppController.prototype.load_speaker_view = function() {
      var app;
      if (this.model.speakers.length > 0) {
        return;
      }
      this.speaker_view.showLoading();
      app = this;
      return $.ajax({
        url: '/speakers',
        dataType: 'json',
        success: function(data) {
          var t_coll, x, _fn, _i, _len;
          t_coll = [];
          _fn = function(x) {
            var speaker;
            speaker = new SpeakerModel(x);
            return t_coll.push(speaker);
          };
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            x = data[_i];
            _fn(x);
          }
          app.model.speakers.reset(t_coll);
          return app.speaker_view.hideLoading();
        },
        failure: function() {
          return alert('data failure...');
        }
      });
    };
    AppController.prototype.load_session_view = function() {
      var app;
      if (this.model.sessions.length > 0) {
        return;
      }
      this.schedule_view.showLoading();
      app = this;
      return $.ajax({
        url: '/sessions',
        dataType: 'json',
        data: {
          conf_id: this.model.get('conf_id')
        },
        success: function(data) {
          var t_coll, x, _fn, _i, _len;
          t_coll = [];
          _fn = function(x) {
            var session;
            session = new SessionModel(x);
            return t_coll.push(session);
          };
          for (_i = 0, _len = data.length; _i < _len; _i++) {
            x = data[_i];
            _fn(x);
          }
          app.model.sessions.reset(t_coll);
          return app.schedule_view.hideLoading();
        },
        failure: function() {
          return alert('data failure...');
        }
      });
    };
    return AppController;
  })();
  root.EventDispatcher = EventDispatcher;
  page_change_handler = function(e, data) {
    if (typeof data.toPage === 'string') {
      return e.preventDefault();
    }
  };
  initialize_app = function(x) {
    var appc;
    appc = new AppController(x);
    return $(document).bind("pagebeforechange", page_change_handler);
  };
  root.initialize_app = initialize_app;
}).call(this);
