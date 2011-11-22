#Global Event Dispatcher
root = exports ? this
EventDispatcher =
	EVENT_TYPE_USER_ACTION:'user_action'
	EVENT_SUBTYPE_SWITCH_VIEW:'switch_view'

_.extend(EventDispatcher, Backbone.Events)

class SpeakerModel extends Backbone.Model

class SpeakerCollection extends Backbone.Collection
	model: SpeakerModel

class SpeakerItemView extends Backbone.View
	tagName: 'li',
	initialize: =>
	    @template = $('#speaker-template').template()
	    @model.bind('change', @render)

	events:
		'click': "click_handler"

	click_handler: (ev)->
		#alert 'you clicked on a particular tweet...'
		ev.preventDefault()

	render: =>
	    $(@el).html($.tmpl(@template, @model.toJSON()))
	    @

class SpeakerView extends Backbone.View
	initialize: ->
	    @model.speakers.bind('reset', @refreshAll)

	#events:
		#'click .search': "search"

	render: =>
		@

	refreshAll: ()=>
		@$('#speaker-list').html('')
		@$('#speaker-list').listview()
		@model.speakers.each (speaker)->
				view = new SpeakerItemView model: speaker
				@$('#speaker-list').append(view.render().el)
		@$('#speaker-list').listview('refresh')

	show: ()=>
		$(@el).show()
	
	hide: ()=>
		$(@el).hide()

	showLoading: ->
	    $.mobile.pageLoading()

	hideLoading: ->
	    $.mobile.pageLoading(true)

#Session related data
class SessionModel extends Backbone.Model

class SessionCollection extends Backbone.Collection
	model: SessionModel

class SessionView extends Backbone.View
	tagName: 'li',
	initialize: =>
	    @template = $('#session-template').template()
	    @model.bind('change', @render)

	events:
		'click': "click_handler"

	click_handler: (ev)->
		#alert 'you clicked on a particular tweet...'
		ev.preventDefault()

	render: =>
		$(@el).html($.tmpl(@template, @model.toJSON()))
		$(@el).attr('data-role', "list-divider")
		@

class ScheduleView extends Backbone.View
	initialize: ->
	    @model.sessions.bind('reset', @refreshAll)

	#events:
		#'click .search': "search"

	render: =>
		@

	refreshAll: ()=>
		@$('#session-list').html('')
		@$('#session-list').listview()
		@model.sessions.each (session)->
				view = new SessionView model: session
				@$('#session-list').append(view.render().el)
		@$('#session-list').listview('refresh')

	show: ()=>
		$(@el).show()
	
	hide: ()=>
		$(@el).hide()

	showLoading: ->
	    $.mobile.pageLoading()

	hideLoading: ->
	    $.mobile.pageLoading(true)

#Twitter related data
class TweetModel extends Backbone.Model

class TweetCollection extends Backbone.Collection
	model: TweetModel

class TweetView extends Backbone.View
	tagName: 'li',
	initialize: =>
	    @template = $('#tweet-template').template()
	    @model.bind('change', @render)

	events:
		'click': "click_handler"

	click_handler: (ev)->
		#alert 'you clicked on a particular tweet...'

	render: =>
	    $(@el).html($.tmpl(@template, @model.toJSON()))
	    @

class TwitterView extends Backbone.View
	initialize: ->
	    @model.tweets.bind('reset', @refreshAll)

	#events:
		#'click .search': "search"

	render: =>
		@

	show: ()=>
		$(@el).show()
	
	hide: ()=>
		$(@el).hide()

	refreshAll: ()=>
		@$('#tweet-list').html('')
		@$('#tweet-list').listview()
		@model.tweets.each (tweet)->
				view = new TweetView model: tweet
				@$('#tweet-list').append(view.render().el)
		@$('#tweet-list').listview('refresh')

	showLoading: ->
	    $.mobile.pageLoading()

	hideLoading: ->
	    $.mobile.pageLoading(true)

class AppModel extends Backbone.Model
	initialize: ()->
		@tweets = new TweetCollection()
		@sessions = new SessionCollection()
		@speakers = new SpeakerCollection()

class NavBar extends Backbone.View
	initialize: ()->

	events:
		'click li': 'click_handler'
	
	click_handler: (ev)=>
		$current_target = $(ev.currentTarget)
		#alert "navigation bar clicked... #{$current_target.attr('id')}"
		id = "#{$current_target.attr('id')}"
		EventDispatcher.trigger(EventDispatcher.EVENT_TYPE_USER_ACTION, EventDispatcher.EVENT_SUBTYPE_SWITCH_VIEW, id)


class AppController extends Backbone.Router
	initialize: (args)=>
		@model = new AppModel args
		@nav_bar = new NavBar model: @model, el: $('#nav-bar')
		@twitter_view = new TwitterView model: @model, el: $('#twitter-view')
		@schedule_view = new ScheduleView model: @model, el: $('#session-view')
		@speaker_view = new SpeakerView model: @model, el: $('#speaker-view')

		@views = [@twitter_view, @schedule_view, @speaker_view]

		EventDispatcher.bind(EventDispatcher.EVENT_TYPE_USER_ACTION, @event_handler)
		EventDispatcher.trigger(EventDispatcher.EVENT_TYPE_USER_ACTION, EventDispatcher.EVENT_SUBTYPE_SWITCH_VIEW, 'schedule')
		@

	event_handler: (e_type, e_data)=>
		switch e_type
			when EventDispatcher.EVENT_SUBTYPE_SWITCH_VIEW then @show_view(e_data)

	show_view: (e_data)=>
		for v in @views
			do (v)-> v.hide()

		switch e_data
			when 'schedule'
				@schedule_view.show()
				@load_session_view()
			when 'twitter'
				@twitter_view.show()
				@load_twitter_view(@model.get('tw_kwd'))
			when 'speakers'
				@speaker_view.show()
				@load_speaker_view()

	load_twitter_view: (term)=>
		#show twitter_view 
		return if @model.tweets.length > 0

		@twitter_view.showLoading()
		query_url = "http://search.twitter.com/search.json?lang=en&callback=?&q=#{term}"
		$.getJSON(query_url, @twitter_response_callback)
		@

	twitter_response_callback: (data)=>
		@twitter_view.hideLoading()
		app = @
		t_coll = []
		for x in data.results
			do (x) ->
				tweet = new TweetModel
								screen_name: x.from_user, text: x.text, profile_pic: x.profile_image_url
				t_coll.push(tweet)
				#app.model.tweets.add(tweet)
		app.model.tweets.reset(t_coll)
		return

	load_speaker_view: ()=>
		return if @model.speakers.length > 0
		@speaker_view.showLoading()
		app = @
		$.ajax
			url: '/speakers'
			dataType: 'json'
			success: (data)->
				t_coll = []
				for x in data
					do (x) ->
						speaker = new SpeakerModel x
						t_coll.push(speaker)
				app.model.speakers.reset(t_coll)
				app.speaker_view.hideLoading()
				
			failure: ()->
				alert 'data failure...'

	load_session_view: ()=>
		return if @model.sessions.length > 0
		@schedule_view.showLoading()
		app = @
		$.ajax
			url: '/sessions'
			dataType: 'json'
			data:
				conf_id: @model.get('conf_id')
			success: (data)->
				t_coll = []
				for x in data
					do (x) ->
						session = new SessionModel x
						#st_date = new Date(x.start_date)
						#session.set st_date: st_date, day: days[st_date.getDay()]
						t_coll.push(session)
				app.model.sessions.reset(t_coll)
				app.schedule_view.hideLoading()
				
			failure: ()->
				alert 'data failure...'

root.EventDispatcher = EventDispatcher

page_change_handler = (e, data)->
	if (typeof data.toPage == 'string')
		e.preventDefault()

initialize_app = (x)->
	appc = new AppController x
	$(document).bind( "pagebeforechange", page_change_handler)

root.initialize_app = initialize_app
