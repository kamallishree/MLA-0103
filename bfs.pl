edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(d,f).

best_first(X,Y):-
    edge(X,Y).

best_first(X,Y):-
    edge(X,Z),
    best_first(Z,Y).