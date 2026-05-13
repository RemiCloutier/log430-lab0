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

**Question 2**:
 > Que fait GitHub pendant les étapes de « setup » et « checkout » ? Veuillez inclure la sortie du terminal GitHub CI dans votre réponse.

"Setup job" est l'étape qui prépare le serveur/cluster distant qui effectuera le processus CI:
```
Current runner version: '2.334.0'
Runner Image Provisioner
Operating System
Runner Image
GITHUB_TOKEN Permissions
Secret source: Actions
Prepare workflow directory
Prepare all required actions
Getting action download info
Download action repository 'actions/checkout@v3' (SHA:f43a0e5ff2bd294095638e18286ca9a3d1956744)
Download action repository 'actions/setup-python@v4' (SHA:7f4fc3e22c37d6ff65e88745f38bd3157c663f7c)
Complete job name: build
```

Ensuite, l'étape de "checkout" prépare le repository, ainsi que git:
```
Run actions/checkout@v3
Syncing repository: RemiCloutier/log430-lab0
Getting Git version info
Temporarily overriding HOME='/home/runner/work/_temp/7aa65316-a3e6-49d1-9b95-b368b0f12176' before making global git config changes
Adding repository directory to the temporary git global config as a safe directory
/usr/bin/git config --global --add safe.directory /home/runner/work/log430-lab0/log430-lab0
Deleting the contents of '/home/runner/work/log430-lab0/log430-lab0'
Initializing the repository
Disabling automatic garbage collection
Setting up auth
Fetching the repository
Determining the checkout info
Checking out the ref
/usr/bin/git log -1 --format='%H'
'67833433fabc14600be5110f7392d1b2a917e651'
```
