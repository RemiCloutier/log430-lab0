**Question 1**: 
> Si l'un des tests échoue à cause d'un bug, comment pytest signale-t-il l'erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

Lorsqu'un test échoue, pytest nous le signalera avec une AssertionError. Voyons ce qui arrive si d'assert une fausse addition: 

```
def test_addition():
    calc = Calculator()
    assert calc.addition(2, 2) == 5
```

Lorsqu'on exécute le test, on aura comme erreur en console:
```
    def test_addition():
        calc = Calculator()
>       assert calc.addition(2, 2) == 5
E       assert 4 == 5
E        +  where 4 = <bound method Calculator.addition of <calculator.Calculator object at 0x79824dbed4c0>>(2, 2)
E        +    where <bound method Calculator.addition of <calculator.Calculator object at 0x79824dbed4c0>> = <calculator.Calculator object at 0x79824dbed4c0>.addition

tests/test_calculator.py:16: AssertionError
```

Lorsqu'on corrige le bug avec `assert calc.addition(2, 2) == 4`, on n'obtient plus d'erreur, et alors le test passe, et cela est affiché par du vert en console.