
# Data Classes
Data classes are a bread and butter tool for the everyday programmer that can save you literally hours every week.

## Data Classes Decoration Usecase
Imagine you're working on a small to mid-sized project, maybe there are other contributors on a github project, or maybe this is for work and you're working with your coworkers, or maybe, you just want to have good code style
for yourself.<br/>

For example, let's assume you're working on a web app and people can comment in your project. Comments have basically just been like a tuple of a unique index and the text content, or maybe you're just using dictionaries with ID and text keys but in any case, the project is starting to get to a point where it's getting a little bit too big to just have raw tuples floating around.
<br/>

For sake of readability, You've decided make comment into a class of its own right.
All the work that you would have to do, just to write a simple comment class, that is a wrapper around literally just an integer and a string. You'd have to write an <code>__init__</code> function, that's pretty  boiler plate, but
not too much work and people are gonna want print these things
out from time to time so we'll write a <code>__repr__</code> just to make things nice for people and it's always good practice to write an
<code>__equals__</code> function but, for type safety, we should probably make sure we're not comparing ourselves with things
of different classes. We don't have to write a not equals but it
does improve code performance a little bit
<br/>

I can definitely see someone wanting to put one of these things inside a dictionary, so that means it needs to be hashable, we need to write a <code>__hash__</code> function and if some thing's gonna be hashable we should really make it immutable as well
to make it immutable, I just replace the ID and text with double under ID and text, and make ID and text properties so that way people can read those properties, but they can't write to them.
<br/>

**Imagine you have to add authors to comments!**<br/>
In fact, you should update all the other methods and maybe it's better to say you need to rewrite the entire class. 
<br/>

There's gotta be a better way!
**@dataclasses**<br/>

Here's the implementation of that class.


```python 
@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str
```




so now, I can construct a comment, just as
usual, pass its arguments, 1 and "I just subscribed!"

and I can print it out
and you can see it has a nice repr and

I would just use this as I would any normal
class

of course, if I ever did need to convert it
into a tuple or dictionary, dataclasses has

an astuple and asdict function which will
convert for you

so, let me just print those out
you can see, it will give it back to me as

a tuple or a dictionary if I really want that
but, for now, let's just assume that we're

just gonna be using the class
so, to take a look at what dataclasses actually

done for me, I'm gonna be using the inspect
module, which allows me to look at what are

all the functions that are written in this
class

so when I print them out, you can see that
equals, greater than equals, greater than,

all these things have all been written for
me and they've all been implemented correctly

there's no chance of, you know, missing a
self dot or switching the order of some arguments

or something like that
by default, if I didn't have those frozen

or ordered arguments, then you would see this:
by default, it just writes the equals and 

the repr
if you wanted it to write the hash, then it needs

to be immutable, so you do that by saying
frozen equals true

you can see that it added a hash function
and it also added a setattr which is necessary

to make it immutable
so now, if I try to say comment.id = 3, well,

first off, PyCharm already knows: it says
this ID is read only and if I try to run the

code I'll get a frozen instance error, so
it's not allowing me to change that ID

of course, if you don't want your data structure
to be immutable, it doesn't have to be

I think the order keyword argument is pretty
self-explanatory, if I just added that one

in, then it would just write all the things
that the total ordering method would write

but notice here, I didn't have to write less
than

it wrote all of them for me
so the order that's actually creating is the

same one that you would get for a tuple that
has its arguments in this order

generally, I do think it's a good idea to
make most dataclasses frozen, so people can

use them as keys in dictionaries
if you wanna make a copy of an immutable data

class, with something changed in it, then
you can use the replace method from the dataclasses

library
you can also set default values like this,

so that if I leave off an argument, it just
gets that default value

now, as usual, you always wanna watch out
for default mutable arguments

in this case, we do not want every instance
of the comment class to share the same list

the way to avoid that is by using a default
factory

so that every instance should call this function
with no arguments in order to create this

attribute if it wasn't passed in
notice here that I'm using this field method

from the dataclasses library
this is actually what's being used in all

of these cases behind the scene
so, in reality, this is equivalent

in very simple cases, and most cases, I think
you can leave off the field and just use the

simpler syntax of before
but in classes that have more attributes you're

gonna find yourself wanting to use this
this field function takes other arguments

which can allow you to modify how each attribute
acts with respect to things like the order

and hash
so I can do something like compare = False

to prevent replies from being compared when
you compare two comments

similarly, I may not want it to participate
in the hashing or show up when I print it

so you can see that when I print it out, it
still just shows ID and text even though the

replies field is there
so that's data classes and how you use them,

but I do also wanna mention a very similar
library

in most cases, data classes do everything
that I need, but I do want to at least mention

another library, the attr.s library that the
dataclasses were based off of

the attr.s library does essentially the same
thing that the data classes library does except

with slightly different names
now I say attr.ib and attr.s instead of dataclass

and field, but it also does a little bit more
in particular, attr.s allow you to specify

validators to do something like actually check
the type of something at runtime

or converters to convert something to a specified
type

the last major feature that attr.s supports
that dataclass doesn't is the slots feature,

so if you want your class to use slots instead
of an instance dictionary

then attr.s supports that, but dataclasses
doesn't

to me, there are only two real downsides to
using the attr.s library

the first is that it does not support this
bare syntax

you have to say = attr.ib() and = attr.ib()
now, the one exception to this is that if

all of your fields have a default value you
can use this syntax

but if any of them doesn't then they all need
attr.ib()s

and to me, the only other downside of using
the attr.s library is that it is a separate

dependency
it's not builtin to Python, so you do have

to download it separately
if you're someone who worries a lot about

including outside dependencies in your project,
then attr.s would not be for you

but you could still use dataclasses
so that's my take on dataclasses and the attr.s

library
they're gonna save you a huge amount of time

I hope that you can work them into your workflow
if you liked the video, don't forget to give

it a like,
and if you especially liked it, please consider

subscribing
thanks for watching

see you next time

