rider(A,B):-
parent(A,B).
rider(A,B):-
parent(A,X),
rider(X,B).


parent(aden,reuben).
parent(reuben,sonny).

