
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

Dataclass decorator has all the functionality that above mentioned.
