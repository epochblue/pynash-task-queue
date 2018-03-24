# Let's Write a Task Queue!

_This repo was created as part of a presentation to the PyNash meetup group in March 2018.
The page for this specific meeting can be found here: [https://www.meetup.com/PyNash/events/248765600/](https://www.meetup.com/PyNash/events/248765600/)._

The purpose of this talk was to illustrate a very basic task queue.
It was intended to introduce the basic concepts of delayed execution, serialization, and demystify a piece of software used by many developers everyday.
The talk intentionally avoided some of the most complicated parts of a more robust task queue (process forking, retrying, managing multiple queues, threading, etc).

The presentation was strictly a live coding presentation, and each commit in this repo represents a way point during the presentation.
I started out laying the foundation for what we were doing with a simple script to illustrate the concept of delayed execution.
We improved upon that by breaking our original script up into more maintainable pieces.
We then improved further by introducing a broker to give our queue some safety against app/worker crashes, and give our app and workers the ability to read and write from the same queue.
Our next improvement was to introduce the idea of serializing Python objects via `pickle` when storing them in places that don't natively understand Python objects.
And the final improvement was to "upgrade" our worker process to run forever and patiently wait for work to be done, rather than being run by hand.


The code here should be considered public domain and available for anyone to use without need for attribution of any kind. 
