Calculs approchés d'intégrales (ChatGPT)
========================================

.. todo:: Texte réécrit, à relire avec attention en raison des copier-coller...

.. todo:: OK, je relirai également. Je viens de penser aussi à Centrale - PC - 2021 qui fait les méthodes de quadrature.

.. todo:: Le II.C fait un lien avec la section 5.5 sur les familles de polynômes orthogonaux.
   Le III permet d'avoir une application des polynômes / nombres de Bernoulli

Nous abordons dans cette section quelques méthodes dont le but est d’estimer la valeur numérique de l’intégrale d'une fonction donnée :math:`f` définie sur un domaine borné :math:`[a, b]`:

.. math::

    I = \int_a^b f(t) \, dt.

Ces méthodes nous fourniront une valeur approchée :math:`\widetilde{I}` de l'intégrale :math:`I` de sorte que

.. math::

    \widetilde{I} \approx I.

Soient :math:`a` et :math:`b` désignent deux réels tels que :math:`a < b`. Pour tout entier naturel :math:`p` non nul, on note :math:`(x_i)_{i\in\llbracket 0, p \rrbracket}` la subdivision régulière de :math:`[a, b]` de pas :math:`\frac{b-a}{p}`. Ainsi, pour tout :math:`i \in \llbracket 0, p \rrbracket`,

.. math::

    x_i = a + i \frac{b-a}{p}.

.. todo:: Doit-on définir la notion d'"exacte" dans la définition suivante ?

.. todo:: C'est peut être mieux, j'ai fait une proposition qui permet de ne pas trop rallonger la définition mais qui demande d'avoir défini :math:`I` et :math:`\widetilde{I}` avant.

.. rst-class:: deflist

    :Definition:
        Une méthode d'intégration est d'*ordre* au moins :math:`n` si elle est exacte (i.e. :math:`\widetilde{I} = I`) pour les polynômes de degrés inférieurs ou égaux :math:`n` et non exacte pour au moins un polynôme de degré :math:`n+1`.

Méthode des rectangles à gauche
-------------------------------

La méthode des rectangles à gauche consiste, pour chacun des intervalles de la subdivision, à approcher l'aire sous la courbe représentative de :math:`f` par celle d'un rectangle dont la hauteur correspond à la valeur de :math:`f` sur la borne de gauche. Plus précisément, on considère la quantité :

.. math::

    I_p^\mathrm{g}(f) = \frac{b-a}{p} \sum_{i=0}^{p-1} f(x_i).

.. marginfigure:: illustrations/i_rectangles_a_gauche
   :align: center

.. rst-class:: proposition

    **Proposition:**
        La méthode des rectangles à gauche est d'ordre 0. De plus, si :math:`f` est de classe :math:`\mathscr{C}^1`, l'erreur commise est en :math:`O(1/p)`.

.. rst-class:: elem_sol

    **Solution:**
        On suppose que :math:`f` désigne une fonction de classe :math:`\mathscr{C}^1` sur le segment :math:`[a, b]`. On note :math:`F` une primitive de :math:`f` et :math:`M_1 = \sup_{[a, b]} |f'|`.

        1. D'après la formule de Taylor avec reste intégral, pour tout :math:`i \in \llbracket 0, p-1 \rrbracket`,

        .. math::

            |F(x_{i+1}) - F(x_i) - (x_{i+1} - x_i) F'(x_i)| \leq \frac{M_1}{2} (x_{i+1}-x_i)^2.

        2. En utilisant la relation de Chasles,

        .. math::

            \begin{align*}
            |\int_{[a, b]} f - I_p^\mathrm{g}(f)| &\leq \sum_{i=0}^{p-1} |\int_{[x_i, x_{i+1}]} f - (x_{i+1} - x_i) f(x_i)|\\
            &\leq \sum_{i=0}^{p-1} \frac{M_1}{2} (x_{i+1} - x_i)^2\\
            &\leq \frac{M_1 (b-a)^2}{2 p}.
            \end{align*}

        3. De plus, on montre que cette borne est atteinte pour :math:`f : x \mapsto x - a`.

        4. La méthode des rectangles à gauche est exacte si :math:`f` est constante. Cependant, le calcul précédent montre que si :math:`f : x \mapsto x - a`, alors la méthode ne donne pas la valeur exacte de l'intégrale. La méthode est donc d'ordre 0.

Méthode des rectangles médians
------------------------------

La méthode des rectangles médians consiste, pour chacun des intervalles de la subdivision, à approcher l'aire sous la courbe représentative de :math:`f` par celle d'un rectangle dont la hauteur correspond à la valeur de :math:`f` au milieu de la subdivision. Plus précisément, on considère la quantité :

.. math::

    I_p^\mathrm{m}(f) = \frac{b-a}{p} \sum_{i=0}^{p-1} f\left(\frac{x_i + x_{i+1}}{2}\right).

.. rst-class:: proposition

    **Proposition:**
        La méthode des rectangles médians est d'ordre 1. De plus, si :math:`f` est de classe :math:`\mathscr{C}^2`, l'erreur commise est en :math:`O(1/p^2)`.

.. marginfigure:: illustrations/i_rectangles_medians
   :align: center

.. rst-class:: elem_sol

    **Solution:**
        On suppose que :math:`f` désigne une fonction de classe :math:`\mathscr{C}^2` sur le segment :math:`[a, b]`. On note :math:`F` une primitive de :math:`f` et :math:`M_2 = \sup_{[a, b]} |f''|`. Pour tout entier :math:`i \in \llbracket 0, p-1 \rrbracket`, on pose :math:`\gamma_i = \frac{x_i + x_{i+1}}{2}` le milieu du segment :math:`[x_i, x_{i+1}]`.

        .. todo:: On pourrait hachurer les intégrales de chaque côté de la tangente afin de montrer que les aires se compensent ?

        1. Soit :math:`i \in \llbracket 0, p-1 \rrbracket`. Un simple calcul ou le graphique suivant permet de montrer que :

        .. math::

            (x_{i+1} - x_i) f(\gamma_i) = \int_{x_i}^{x_{i+1}} \left(f(\gamma_i) + (t - \gamma_i) f'(\gamma_i) \right) \, dt.

        2. Ainsi, d'après la formule de Taylor avec reste intégral,

        .. math::

            \begin{align*}
            |F(x_{i+1}) - F(x_i) - (x_{i+1} - x_i) F'(\gamma_i)| &= |\int_{x_i}^{x_{i+1}} \left(f(t) - f(\gamma_i) - (t - \gamma_i) f'(\gamma_i)\right) \, dt|\\
            &\leq \frac{M_2}{24} (x_{i+1} - x_i)^3.
            \end{align*}

        3. Comme pour la méthode des rectangles à gauche, la formule de Chasles permet de montrer que

        .. math::

            |\int_{[a,b]} f - I_p^\mathrm{m}(f)| \leq \frac{M_2 (b-a)^3}{24 p^2}.

        4. De plus, on montre que cette borne est atteinte pour :math:`f : x \mapsto (x - a)^2`.

        5. La méthode des rectangles médians est exacte si :math:`f` est un polynôme de degré 1. Cependant, si :math:`f` est la fonction :math:`x \mapsto (x - a)^2`, le calcul précédent montre que la méthode des rectangles médians ne donne pas la valeur exacte de l'intégrale. La méthode est donc d'ordre 1.

Méthode des trapèzes
--------------------

La méthode des trapèzes consiste, pour chacun des intervalles de la subdivision, à approcher l'aire sous la courbe représentative de :math:`f` par celle d'un trapèze. Plus précisément, on considère la quantité :

.. math::

    I_p^\mathrm{t}(f) =  \frac{b-a}{2p} \left( f(x_0) + 2 \sum_{i=1}^{p-1} f(x_i) + f(x_p) \right).

.. marginfigure:: illustrations/i_trapezes
   :align: center

.. rst-class:: proposition

    **Proposition:**
        La méthode des trapèzes est d'ordre 1. De plus, si :math:`f` est de classe :math:`\mathscr{C}^2`, l'erreur commise est en :math:`O(1/p^2)`.

.. rst-class:: elem_sol

    **Solution:**
        On suppose que :math:`f` désigne une fonction de classe :math:`\mathscr{C}^2` sur le segment :math:`[a, b]`. On note :math:`F` une primitive de :math:`f` et :math:`M_2 = \sup_{[a, b]} |f''|`.

        1. La formule de Taylor-Lagrange appliquée à :math:`f` permet d'écrire, pour tout :math:`i \in \llbracket 0, p-1 \rrbracket`,

        .. math::

            f(x_{i+1}) = f(x_i) + (x_{i+1} - x_i) f'(\gamma_i) + \frac{(x_{i+1} - x_i)^2}{2} f''(\theta_i),

        où :math:`\gamma_i \in [x_i, x_{i+1}]` et :math:`\theta_i \in [x_i, x_{i+1}]`.

        2. En intégrant cette inégalité entre :math:`x_i` et :math:`x_{i+1}`,

        .. math::

            \int_{x_i}^{x_{i+1}} f = (x_{i+1} - x_i) \left( \frac{f(x_i) + f(x_{i+1})}{2} \right) - \frac{(x_{i+1} - x_i)^3}{12} f''(\theta_i).

        3. En sommant sur tous les :math:`i \in \llbracket 0, p-1 \rrbracket`,

        .. math::

            |\int_{[a,b]} f - I_p^\mathrm{t}(f)| \leq \frac{M_2 (b-a)^3}{12 p^2}.

        4. De plus, on montre que cette borne est atteinte pour :math:`f : x \mapsto (x - a)^2`.

        5. La méthode des trapèzes est exacte si :math:`f` est un polynôme de degré 1. Cependant, si :math:`f` est la fonction :math:`x \mapsto (x - a)^2`, le calcul précédent montre que la méthode des trapèzes ne donne pas la valeur exacte de l'intégrale. La méthode est donc d'ordre 1.

Méthode de Simpson
------------------

La méthode de Simpson consiste, pour chacun des intervalles de la subdivision, à approcher la courbe représentative de :math:`f` par un arc de parabole passant par trois points de la courbe :math:`(x_i, f(x_i))`, :math:`(\gamma_i, f(\gamma_i))` et :math:`(x_{i+1}, f(x_{i+1}))`. Plus précisément, on considère la quantité :

.. math::

    I_p^\mathrm{s}(f) = \frac{b-a}{6p} \left( f(x_0) + 4 \sum_{i=0}^{p-1} f(\gamma_i) + 2 \sum_{i=1}^{p-1} f(x_i) + f(x_p) \right).

.. marginfigure:: illustrations/i_simpson
   :align: center

.. rst-class:: proposition

    **Proposition:**
        La méthode de Simpson est d'ordre 3. De plus, si :math:`f` est de classe :math:`\mathscr{C}^4`, l'erreur commise est en :math:`O(1/p^4)`.

.. rst-class:: elem_sol

    **Solution:**
        On suppose que :math:`f` désigne une fonction de classe :math:`\mathscr{C}^4` sur le segment :math:`[a, b]`. On note :math:`F` une primitive de :math:`f` et :math:`M_4 = \sup_{[a, b]} |f^{(4)}|`.

        1. Pour tout :math:`i \in \llbracket 0, p-1 \rrbracket`, la formule de Taylor-Lagrange permet d'écrire

        .. math::

            \begin{aligned}
            f(x_{i+1}) &= f(x_i) + (x_{i+1} - x_i) f'(\gamma_i) + \frac{(x_{i+1} - x_i)^2}{2} f''(\gamma_i) + \frac{(x_{i+1} - x_i)^3}{6} f^{(3)}(\gamma_i) + \frac{(x_{i+1} - x_i)^4}{24} f^{(4)}(\theta_i),\\
            f(\gamma_i) &= f(x_i) + (x_{i+1} - x_i) f'(\gamma_i) + \frac{(x_{i+1} - x_i)^2}{2} f''(\gamma_i) + \frac{(x_{i+1} - x_i)^3}{8} f^{(3)}(\gamma_i) + \frac{(x_{i+1} - x_i)^4}{16} f^{(4)}(\theta_i),
            \end{aligned}

        où :math:`\gamma_i = \frac{x_i + x_{i+1}}{2}` est le milieu de :math:`[x_i, x_{i+1}]` et :math:`\theta_i \in [x_i, x_{i+1}]`.

        2. En intégrant entre :math:`x_i` et :math:`x_{i+1}`,

        .. math::

            \begin{aligned}
            \int_{x_i}^{x_{i+1}} f &= (x_{i+1} - x_i) \left( \frac{f(x_i) + 4 f(\gamma_i) + f(x_{i+1})}{6} \right)\\
            &\quad + (x_{i+1} - x_i)^5 \left( \frac{f^{(4)}(\theta_i)}{1920} \right).
            \end{aligned}

        3. En sommant sur tous les :math:`i \in \llbracket 0, p-1 \rrbracket`,

        .. math::

            |\int_{[a,b]} f - I_p^\mathrm{s}(f)| \leq \frac{M_4 (b-a)^5}{1920 p^4}.

        4. De plus, on montre que cette borne est atteinte pour :math:`f : x \mapsto (x - a)^4`.

        5. La méthode de Simpson est exacte si :math:`f` est un polynôme de degré inférieur ou égal à 3. Cependant, si :math:`f` est la fonction :math:`x \mapsto (x - a)^4`, le calcul précédent montre que la méthode de Simpson ne donne pas la valeur exacte de l'intégrale. La méthode est donc d'ordre 3.

Méthodes de quadrature de Gauss
-------------------------------

On a vu dans le cours de nombreuses propriétés sur les familles de polynômes orthogonaux. Ces propriétés sont utiles dans les méthodes d'intégration numérique de type quadrature de Gauss. Pour simplifier les notations et la présentation, nous nous concentrons sur l'intégration de fonctions sur le segment :math:`[-1, 1]`.

.. todo:: Il faudrait mettre un encadré pour rappeler que l'intégrale d'une fonction sur n'importe quel segment borné :math:`[a,b]` se ramène à une intégrale sur :math:`[-1, 1]` en utilisant le changement de variable affine :math:`u \mapsto \frac{b-a}{2} u + \frac{a+b}{2}`. On a alors :math:`\int_a^b f(t) \, dt = \frac{b-a}{2} \int_{-1}^1 f\left( \frac{b-a}{2} u + \frac{a+b}{2} \right) \, du`. C'est déjà utilisé dans la section 5.5 sur les familles de polynômes orthogonaux.

En toute généralité, la méthode de quadrature de Gauss consiste à approximer l'intégrale d'une fonction par une combinaison linéaire de valeurs de la fonction en des points bien choisis (les points de Gauss), avec des coefficients associés (les poids de Gauss). Plus précisément, si :math:`(\xi_i)_{i\in\llbracket 1, n \rrbracket}` désignent les points de Gauss et :math:`(\alpha_i)_{i\in\llbracket 1, n \rrbracket}` les poids de Gauss associés, la méthode consiste à utiliser l'approximation suivante :

.. math::

    \int_{-1}^1 f(t) \, dt \approx \sum_{i=1}^n \alpha_i f(\xi_i).

Le choix des points et des poids de Gauss s'effectue de manière à rendre la méthode exacte pour les polynômes de degré au plus :math:`2n - 1`. Les points de Gauss sont les racines du :math:`n`-ième polynôme orthogonal de Legendre :math:`P_n`, et les poids de Gauss sont donnés par la formule suivante :

.. math::

    \alpha_i = \frac{2}{(1 - \xi_i^2) [P'_n(\xi_i)]^2}, \quad \forall i \in \llbracket 1, n \rrbracket.

Les illustrations ci-dessous présentent les résultats obtenus par application de la méthode des trapèzes, de la méthode de Simpson et de la méthode de quadrature de Gauss sur un exemple concret.

.. figure:: illustrations/example_trapezes
   :align: center

   Résultat de la méthode des trapèzes sur l'exemple.

.. figure:: illustrations/example_simpson
   :align: center

   Résultat de la méthode de Simpson sur l'exemple.

.. figure:: illustrations/example_gauss
   :align: center

   Résultat de la méthode de quadrature de Gauss sur l'exemple.

Conclusion
==========

Nous avons présenté les trois principales méthodes d'intégration numérique : la méthode des trapèzes, la méthode de Simpson et la méthode de quadrature de Gauss. Chacune de ces méthodes a ses avantages et ses inconvénients, et le choix de la méthode dépend du problème à résoudre et de la précision souhaitée.

Les méthodes d'intégration numérique sont essentielles pour de nombreux domaines d'application, notamment en physique, en ingénierie et en finance, où il est souvent nécessaire de calculer des intégrales de fonctions complexes qui ne peuvent pas être intégrées analytiquement.

Le code suivant permet d'illustrer l'application des trois méthodes sur un exemple simple. Vous pouvez modifier la fonction à intégrer et les paramètres des méthodes pour observer leur comportement dans différentes situations.

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt

    def f(x):
        return np.exp(-x**2)

    a, b = 0, 1
    n = 10
    x = np.linspace(a, b, n+1)
    y = f(x)

    # Méthode des trapèzes
    trapezes = np.trapz(y, x)

    # Méthode de Simpson
    simpson = np.simps(y, x)

    # Méthode de quadrature de Gauss
    from numpy.polynomial.legendre import leggauss
    x_gauss, w_gauss = leggauss(n)
    x_gauss = 0.5 * (b - a) * x_gauss + 0.5 * (b + a)
    w_gauss = 0.5 * (b - a) * w_gauss
    gauss = np.sum(w_gauss * f(x_gauss))

    print(f"Trapèzes : {trapezes}")
    print(f"Simpson : {simpson}")
    print(f"Gauss : {gauss}")

    # Plotting the results
    plt.plot(x, y, 'o', label='Data points')
    plt.plot(x, f(x), label='Function')
    plt.fill_between(x, y, step='mid', alpha=0.2, label='Trapèzes')
    plt.legend()
    plt.show()
