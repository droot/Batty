import requests
from datetime import datetime
import simplejson as json

SERVER_PREFIX="http://localhost:6767"
#schedule data in dict form

conference = dict(
		    title = "PyCon India 2011",
		    url_title = 'pyconindia',
		    desc = "PyCon India 2011 is the primary Python conference in India. A purely volunteer effort, it is being hosted for the third time in India, and will attract some of the best Python developers in India and abroad.  The conference will take place at Symbiosis Vishwabhavan, S.B. Road, Pune (map) on 16th, 17th and 18th September 2011.",
		    venue = "Symbiosis Vishwabhavan, S.B. Road, Pune, India",
		    start_date = '%s' % datetime(2011, 9, 16, 00, 00, 00),
		    end_date = '%s' % datetime(2011, 9, 18, 00, 00, 00),
		    twitter_handle = 'pyconindia',
		    twitter_hashcode = 'pyconindia'
		) 
	
sessions = [

	dict(title = "Sun Rise",
	     desc = ".....",
	     duration = "180",
	     talk_type = 'sunrise',
	     start_date = '%s' % datetime(2011, 9, 16, 06 , 00, 00),
	     end_date = '%s' % datetime(2011, 9, 16, 07, 00, 00),
	     speaker_title = 'God'),

	dict(title = "Web API programming using Python",
	     desc = "This talk will teach Python programmers how to build applications that fetch data from third-party websites like Twitter, Facebook, Linked-in, Google (gmail, contacts), or any other site that exposes a (Restful) Web API. The talk will cover the basics, including signing up for developer access, authentication using OAuth, using the APIs directly via HTTP calls, overviews of a few selected third-party libraries for accessing popular websites, and finally how to incorporate this into a web based application - with django as a specific example.",
	     duration = "180",
	     talk_type = 'Tutorial',
	     start_date = '%s' % datetime(2011, 9, 16, 10, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 16, 13, 00, 00),
	     speaker_title = 'Navin Kabra'),

	dict(title = "Art of Web Scrapping using Python",
	    desc = "Web scrapping involves fetching formatted data from websites, which otherwise do not provide any API to do so. This means that using this technique you can script programs, that can go to different websites, and get you the data which has importance. For Ex: making an desktop interface for a website. For automatically posting data after doing some analysis. Fetching data offline in formatted manner. Web scrapping is very useful for everyday and personal use also.",
	     duration = "180",
	     talk_type = 'Tutorial',
	     start_date = '%s' % datetime(2011, 9, 16, 10, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 16, 13, 00, 00),
	     speaker_title = 'Siddhant Sanyam'),

	dict(title = "Image processing and computer interaction",
	    desc = "tutorial aims to introduce simple image processing and computer interaction (ip & hci ) processes by teaching all how to make custom applications and how to interact with computer and other devices using python libraries like numpy, scipy, kivy and opencv. tutorial starts from a gentle and beginners introduction to ip & hci, their applications ( and why everyone is mad about them! ), teaches all to make applications like logging in your systems using face recognition ( using webcams ) or fingerprints or taking input from custom devices ( like a touchscreen ) and analysing and processing that data and ends up at a stage from where everyone can start exploring more.",
	     duration = "180",
	     talk_type = 'Tutorial',
	     start_date = '%s' % datetime(2011, 9, 16, 10, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 16, 13, 00, 00),
	     speaker_title = 'Nitin Chadha, Karan Pratap'),

	dict(title = "Redis & Python",
	    desc = "Redis has been gaining lot of popularity in the community and is being used in very interesting ways in the industry to solve some really complex problems. It is also one of the most popular NoSQL data stores around. The main focus of the talk is to introduce Redis to python community, discuss its strengths and usage pattern. The talk will also focus on the various libraries and tools like redis-py, retools etc. to demonstrate how Redis is accessed in an Python environment.",
	     duration = "180",
	     talk_type = 'Tutorial',
	     start_date = '%s' % datetime(2011, 9, 16, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 16, 17, 00, 00),
	     speaker_title = 'Sunil Arora'),

	dict(title = "Functional Programming with Python",
	    desc = "This tutorial presents various functional programming techniques used in the python world.",
	     duration = "180",
	     talk_type = 'Tutorial',
	     start_date = '%s' % datetime(2011, 9, 16, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 16, 17, 00, 00),
	     speaker_title = 'Anand Chitipothu'),
	
	dict(title = "Using Python with Other Languages",
	    desc = "Not every time a project is developed using single language. A Python project may need to use another language for some tasks or an existing project written in some other language may need to use Python for some tasks. No matter what, better productivity can definitely be obtained when Python comes into game. This tutorial shall walk through with some of the options that are available to extend your projects using different other languages and also on how can you use Python to extend your existing projects in other languages.",
	     duration = "180",
	     talk_type = 'Tutorial',
	     start_date = '%s' % datetime(2011, 9, 16, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 16, 17, 00, 00),
	     speaker_title = 'Vishesh Yadav, Siddhant Sanyam'),

	dict(title = "Sun Rise",
	     desc = ".....",
	     duration = "180",
	     talk_type = 'sunrise',
	     start_date = '%s' % datetime(2011, 9, 17, 06 , 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 07, 00, 00),
	     speaker_title = 'God'),

	dict(title = "Keynote",
	    desc = "Pycon India 2011 Keynote",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 10, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 11, 00, 00),
	     speaker_title = 'Raymond Hettinger'),

	dict(title = "Pyjs: compiling python to javascript",
	    desc = "pyjs is an attempt to compile python into javascript. This project started as an attempt to avoid duplication of writing javascript templates.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 11, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 12, 00, 00),
	     speaker_title = 'Anand Chitipothu'),

	dict(title = "Wikipedia, Dead Authors, Naive Bayes and Python",
	    desc = "This talk is about implementing one of the simplest to understand machine learning algorithm, Naive Bayes Classifier in Python. We will use it for classifying Wikipedia pages. Options range from using ready made implementations available in toolkits like NLTK & Scikits.learn to rolling out your own. This talk will cover both the options, comparing the computational performance and discuss the tradeoffs.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 11, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 12, 00, 00),
	     speaker_title = 'Abhaya Agarwal'),

	dict(title = "Creating Domain Specific Languages in Python",
	    desc = "In this session I'll talk about using domain specific languages (DSL) in Python. DSLs are small languages specific to a particular domain that make it easier to read and write code in that domain. We'll see how you can parse DSLs using the PyParsing library as well as using regular python code to create DSLs.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 12, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 13, 00, 00),
	     speaker_title = 'Siddharta Govindaraj'),

	dict(title = "Snakes for your GIS",
	    desc = "Location based services created a lot of buzz last year. While building prototypes at MapQuest, I observed that python has got no single solution to GIS, but many modules, frameworks and toolsets. They fit in, like the pieces of a bigger puzzle.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 13, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 14, 00, 00),
	     speaker_title = 'Abhishek Mishra'),

	dict(title = "Python on Android",
	    desc = "The talk introduces the Scripting Layer on Android focusing Python. Writing apps on Android without involving Java and Eclipse. A quick sprint through the most used APIs and some demos.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 17, 13, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 14, 00, 00),
	     speaker_title = "Sajjad Anwar"),

	dict(title = "Emacs as a Python IDE",
	    desc = "This is a talk about my Emacs setup particularly the bits relevant to coding Python. The first 20-30 minutes will be purely focussing on Python (IDE like) capabilities and after that on slightly more meta things like programmer productivity and issue tracking in general.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 15, 00, 00),
	     speaker_title = "Noufal Ibrahim"),

	dict(title = "Doing your homework with Python",
	    desc = "This talk will teach you how to use NumPy, SciPy, and Matplotlib to do your college homework, assignments, thesis work, or just random foo things you like to work on. The ecosystem that forms around NumPy, SciPy, Matplotlib, Make, LaTeX, and Git is so powerful and convenient that once you get the hang of it, nothing will ever replace it for you. At the end of the talk, you'll be able to do your work more efficiently, and brag to your friends about how neat, professional, and in general, how awesome your work looks.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 15, 00, 00),
	     speaker_title = "Nirbheek Chauhan"),
	
	dict(title = "PyTI(PyPI Testing Infrastructure)",
	    desc = "This talk describes about PyTI (Python Testing Infrastructure), a project started during GSoC 2011. The goal of the project is to test distributions from PyPI repository to assess quality and also to check if the distribution is malicious or not. Even though PyTI is not yet launched and being developed , there are lot of design decisions whch are firm and that is what this talk is going to deal with. Documentation of the project is provided here",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 15, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 16, 00, 00),
	     speaker_title = "Yeshwanth"),

	dict(title = "Machine Learning Using Python",
	    desc = "Machine Learning, although a relatively nascent field, has found itself to be an integral part of both academia and industry.The basic aim, is an introduction to Machine Learning,a few of the basic algorithms and the libraries in python for implementation of the algorithms.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 15, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 16, 00, 00),
	     speaker_title = "Vikram Kamath"),

	dict(title = "Decorators as composable abstractions",
	    desc = "Decorators are syntactic sugar for creating higher order functions in Python and I'm going to show you how you can use them to introduce a new level of succinctness into your code.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 16, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 17, 00, 00),
	     speaker_title = "Sidhant Godiwala"),

	dict(title = "Python in the Life Sciences",
	    desc = "With increasing amounts of quantitative data in biology, in particular sequencing and image data, use of Python to process the data and to bridge different tools together is increasing.",
	     duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 16, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 17, 00, 00),
	     speaker_title = "Farhat Habib"),

	dict(title = "Python threads: Dive into GIL!",
	    desc = "Benefit of multi-threaded application grows with ubiquity of multi-core architecture that potentially can simultaneously run multiple threads of execution. Python supports multi-threaded applications and developers are flocking to realize the assured gain of multiple cores with threaded applications.  Unfortunately, Python has significant bottleneck for multi-threading. Any thread in CPython interpreter requires a special lock (GIL) which results in serial, rather than parallel execution of multi-threaded applications, irrespective of cores availability and design techniques.  This talk focuses on the problem, dissects the root cause and its implications. The problem alleviation is discussed with introduction of Python3.0 which has new GIL implementation, improving the overall performance of Python threads.",
	    duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 17, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 18, 00, 00),
	     speaker_title = "Vishal Kanaujia, Chetan Giridhar"),

	dict(title = "Using Python for Data Analysis and Business Intelligence",
	    desc = "Using python and associated tools (Scikits/SciPy/NumPy, R, Disco) for data analysis and business intelligence. The focus of the actual samples is likely to be econometric, social and business data.",
	    duration = "45",
	     talk_type = 'Talk',
	     start_date = '%s' % datetime(2011, 9, 17, 17, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 17, 18, 00, 00),
	     speaker_title = "Dhananjay Nene"),

	dict(title = "Sun Rise",
	     desc = ".....",
	     duration = "180",
	     talk_type = 'sunrise',
	     start_date = '%s' % datetime(2011, 9, 18, 06 , 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 07, 00, 00),
	     speaker_title = 'God'),

	dict(title = "LastUser for user management",
	    desc = "LastUser is federated user management app. It runs standalone and supports authentication via OAuth2 using a protocol inspired by Twitter and Facebook. It can be plugged into your apps with minimal effort. LastUser is open source and available under the BSD license.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 10, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 11, 00, 00),
	     speaker_title = "Kiran Jonnalagadda"),

	dict(title = "Network programming with Umit Project",
	    desc = "This talk is about how network protocols are implemented in python. Demo will be shown using Umit Project. Topics are Umit Network Scanner, RadialNet, Visualizing networks, Packet Manipulation using Python, writing a protocol and utilizing it in a network scanner.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 10, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 11, 00, 00),
	     speaker_title = "Narendran Thangarajan"),

	#dict(title = "Sensors, Embedded Systems and Chuk Chuk",
	    #desc = "This talk is a run through of how we developed a cross platform PyQt application for report generation and data collection from our custom sensor node, for the Research Design and Standards Organization (RDSO) of the Indian railways. The talk aims to introduce users to various aspects of interfacing instruments / home grown embedded systems/ DIY projects with python, the patterns we followed and how using python simplified our whole development process.",
	    #duration = "45",
	     #start_date = '%s' % datetime(2011, 9, 18, 10, 00, 00),
	     #end_date = '%s' % datetime(2011, 9, 18, 11, 00, 00),
	     #speaker_title = "Praneeth Bodduluri"),


	dict(title = "Deployment and Hosting of your Python Web Applications",
	    desc = "So you built a web-app. Now what?  How do you deploy it, how do you scale it, how do you monitor it?  What deployment options are available? Is a shared server good enough or do you need a VPS? Who all are cost effective django-friendly VPS providers?  We will discuss these hosts, Amazon EC2, Google App Engine, and a host of (click deployment) options that are now available like AppHosted, Django-Zoom, ep.io, gondor.io, dotcloud and compare and contrast them.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 11, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 12, 00, 00),
	     speaker_title = "Lakshman Prasad"),

	dict(title = "Python in the Real World: From Everyday Applications to Advanced Robotics",
	    desc = "With the advent of 32bit microcontrollers, a greater flexibility is available for designing Real Time Operating Systems (RTOSs) in high level languages such as Python. Python modules such as Scipy, Numpy, matplotlib, etc. provide a platform to design more intelligent systems, especially for advanced robotics, giving more meaningful data for human interaction at the same time. This talk will focus on use of Python in such embedded systems.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 11, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 12, 00, 00),
	     speaker_title = "Jivitesh Singh Dhaliwal"),

	dict(title = "Manage your Amazon AWS assets using boto",
	    desc = "This talk aims to showcase how easy is it manage your Cloud Computing assets remotely. One can manage, monitor and automate recovery from failures. The talk focuses on managing Amazon AWS assets using the very popular boto python library. The talk will cover the basic concepts of Amazon AWS and how boto/python can be used effectively to manage the cloud assets.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 12, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 13, 00, 00),
	     speaker_title = "Chirag Jog"),

	dict(title = "From Python to Silicon",
	    desc = "MyHDL is a free, open source Python software package that can take you from Python to silicon! It is both a hardware description language and a verification language. The talk illustrates the wonderful features of MyHDL and Python for generating VHDL and Verilog code, converting a list of signals, doing co-simulation with Verilog, generating test benches with test vectors for VHDL and Verilog, et. al. The built-in simulator runs on top of the Python interpreter, and supports viewing waveforms by tracing signal changes in a VCD file. It is released under the LGPL license.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 13, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 14, 00, 00),
	     speaker_title = "Shakthi Kannan"),

	dict(title = "Quick Multitouch Apps using kivy and Python",
	    desc = "Multitouch screen enabled devices are now everywhere and all around us. Kivy is an open source Python software library for rapid development of applications equipped with novel user interfaces, such as multi-touch apps.  Using Kivy and Python we can quickly create multitouch apps which can run on Windows, MacOS and Linux based platforms.  In this talk I will show you how to setup kivy and make useful multitouch input based apps rapidly!",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 12, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 13, 00, 00),
	     speaker_title = "Karan Pratap Singh, Nitin Chadha"),

	dict(title = "Django: REST in peace",
	    desc = "The talk focuses on the need and importance of RESTful interfaces while developing Web Applications and how to achieve the same on Django.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 15, 00, 00),
	     speaker_title = "Shreyank Gupta"),


	dict(title = "gobject-introspection, a new friend to help",
	    desc = "This talk is a run through of how we developed a cross platform PyQt application for report generation and data collection from our custom sensor node, for the Research Design and Standards Organization (RDSO) of the Indian railways. The talk aims to introduce users to various aspects of interfacing instruments / home grown embedded systems/ DIY projects with python, the patterns we followed and how using python simplified our whole development process.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 15, 00, 00),
	     speaker_title = "Kushal Das"),


	dict(title = "Network programming with Umit Project",
	    desc = "This talk is about how network protocols are implemented in python. Demo will be shown using Umit Project. Topics are Umit Network Scanner, RadialNet, Visualizing networks, Packet Manipulation using Python, writing a protocol and utilizing it in a network scanner.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 14, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 15, 00, 00),
	     speaker_title = "Narendran Thangarajan"),
	

	dict(title = "Untitled Talk",
	    desc = "Untitled talk by Raymond Hettinger",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 15, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 16, 00, 00),
	     speaker_title = "Raymond Hettinger"),

	dict(title = "Interacting with the larger Python community around the world",
	    desc = "This talks is aiming at introducing a newbie programmer to the larger Python community around him. I aim to cover the Python development process, the communities, the forums and also role of PSF in Python evangelism and some of the programs run by PSF towards this.",
	    duration = "45",
	     start_date = '%s' % datetime(2011, 9, 18, 16, 00, 00),
	     end_date = '%s' % datetime(2011, 9, 18, 17, 00, 00),
	     speaker_title = "Anand B Pillai"),
	]

def populate_conference(conference):
    r = requests.post('%s/confs' % (SERVER_PREFIX), data = conference)
    conf = json.loads(r.content) 
    return conf 


def populate_sessions(conf, sessions):
    for x in sessions:
	x['conf_id'] = conf.get('id')
	r = requests.post('%s/sessions' % (SERVER_PREFIX), data = x)

if __name__ == '__main__':
    conf = populate_conference(conference)
    if conf:
	populate_sessions(conf, sessions)



