eats(anil, peanuts).
eats(harry, apple).

food(X) :-
    eats(_, X),
    \+ killed_by(X).

killed_by(dummy) :- fail.