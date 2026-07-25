% Facts
man(marcus).
pompeian(marcus).
ruler(caesar).
tried_to_assassinate(marcus, caesar).

% Rules
roman(X) :- pompeian(X).
person(X) :- man(X).

not_loyal(X, Y) :-
    tried_to_assassinate(X, Y),
    ruler(Y).

% Keep loyal rules together
loyal(X, someone) :-
    person(X).

loyal(X, caesar) :-
    roman(X),
    \+ not_loyal(X, caesar).

% Hate rule
hates(X, caesar) :-
    roman(X),
    not_loyal(X, caesar).