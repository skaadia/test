Lemme de Lebesgue
=================

.. container:: lemme

   Soit :math:`a < b`.

   #. On suppose que :math:`f` est une fonction de classe
      :math:`\mathscr{C}^1` sur :math:`[a, b]`. Alors,

      .. math:: \lim_{ \lambda \to +\infty} \int_a^b \sin(\lambda t) f(t) \d t = 0.

   #. Redémontrer le même résultat en supposant simplement que la
      fonction :math:`f` est continue par morceaux sur :math:`[a, b]`.

On constate sur la figure suivante que plus :math:`\lambda` est grand,
plus les oscillations sont élevées et plus les aires comptées
positivement et négativement se compensent.

.. container:: center

   .. figure:: ../../img/integration-02_lebesgue.png
      :alt: image
      :width: 75.0%

.. container:: solution

   #. Puisque la fonction :math:`f` est de classe :math:`\mathscr{C}^1`
      sur :math:`[a, b]`, on peut effectuer une intégration par parties
      qui fournit pour :math:`\lambda > 0`:

      .. math:: \left| \int_a^b f(t) \sin(\lambda t) \d t \right| = \left| \frac{1}{\lambda} \left( -\big[ \cos(\lambda t) f(t) \big]_a^b + \int_a^b f'(t) \cos(\lambda t) \d t  \right) \right| \leqslant \frac{1}{\lambda} \left( |f(a)| + |f(b)| + \int_a^b |f'(t)| \d t \right).

      Cette dernière expression tend vers :math:`0` quand
      :math:`\lambda` tend vers :math:`+ \infty`, et donc
      :math:`\int_a^b f(t) \sin(\lambda t) \d t` tend vers :math:`0`
      quand :math:`\lambda` tend vers :math:`+\infty`.

   #. | Si la fonction :math:`f` est simplement supposée continue par
        morceaux, on ne peut donc plus effectuer une intégration par
        parties.
      | Le résultat est clair si :math:`f = 1`, car pour
        :math:`\lambda > 0`,
        :math:`\left| \int_a^b \sin(\lambda t) \d t \right| = \left| \frac{\cos(\lambda a) - \cos(\lambda b)}{\lambda} \right| \leqslant \frac{2}{\lambda}`.
      | Le résultat s’étend aux fonctions constantes par linéarité de
        l’intégrale puis aux fonctions constantes par morceaux par
        additivité par rapport à l’intervalle d’intégration,
        c’est-à-dire aux fonctions en escaliers. Pour toute fonction
        :math:`g` continue par morceaux sur :math:`[a, b]`, on note
        :math:`\|g\|_{\infty} = \sup_{[a, b]} |g|`.
      | Soit alors :math:`f` une fonction continue par morceaux sur
        :math:`[a, b]`.
      | Soit :math:`\varepsilon > 0`. Il existe une fonction en escalier
        :math:`\varphi` telle que
        :math:`\|f - \varphi\|_\infty \leq \varepsilon`. De plus,
        d’après le point précédent, il existe un réel :math:`\lambda_0`
        strictement positif tel que pour tout
        :math:`\lambda > \lambda_0`,

        .. math:: \left|\int_a^b \sin(\lambda t) \varphi(t) \d t\right| \leq \varepsilon.

        Finalement, d’après l’inégalité triangulaire, pour tout
        :math:`\lambda > \lambda_0`,

        .. math::

           \begin{aligned}
                   \left|\int_a^b f(t) \sin(\lambda t) \d t\right|
                   &\leq         \left|\int_a^b (f(t) - \varphi(t)) \sin(\lambda t) \d t\right| + \left|\int_a^b \varphi(t) \sin(\lambda t) \d t\right|\\
                   &\leq \norme{f - \varphi}_\infty (b - a) + \varepsilon\\
                   &\leq \varepsilon (1 + b - a).
           \end{aligned}

        Finalement,
        :math:`\lim\limits_{\lambda \to +\infty} \int_a^b f(t) \sin(\lambda t) \d t = 0`.

Nous allons utiliser le lemme de Lebesgue pour calculer certaines
valeurs de la fonction :math:`\zeta` de Riemann. Nous verrons
ultérieurement une autre utilisation au calcul de la valeur de
l’\ `intégrale de Dirichlet <#sec:intDirichlet>`__.

On note :math:`(B_n)` la suite des `polynômes de
Bernoulli <#sec:polynomes_de_bernoulli>`__ et, pour tout :math:`x > 1`,
:math:`\zeta(x) = \sum\limits_{k=1}^{+\infty} \frac{1}{k^x}`.

.. container:: theo

   Pour tout :math:`m \geq 1`,
   :math:`\zeta(2m) = (-1)^{m-1} (2 \pi)^{2m} \frac{B_{2m}(0)}{2}`.

L’exercice suivant, issu du concours de l’\ esm Saint-Cyr 1995, donne
une démonstration de ce résultat.

.. container:: exercice

   #. Pour :math:`k` et :math:`n` entiers strictement positifs, on
      définit:

      .. math:: I_{n,k} = \int_0^1 B_n(t) \cos(2 k \pi t) \d t.

      Trouver une relation entre :math:`I_{n,k}` et :math:`I_{n-2, k}`
      et en déduire selon la parité de :math:`n`, l’expression de
      :math:`I_{n,k}` en fonction de :math:`n` et de :math:`k`. Pour
      tout entier naturel :math:`n` strictement positif, on pose:

      .. math:: \forall t \in \interoo{0}{1}, \quad \varphi_n(t) = \frac{B_n(t) - B_n(0)}{\sin(\pi t)}.

   #. Montrer que pour :math:`N` entier naturel non nul:

      .. math:: \forall t \in \interoo{0}{1}, \quad 1 + 2 \sum_{k=1}^N \cos(2k \pi t) = \frac{\sin\big((2N+1) \pi t \big)}{\sin(\pi t)}.

   #. Montrer que pour tout entier :math:`n \geqslant 2`, la fonction
      :math:`\varphi_n` est prolongeable par continuité à
      :math:`\interff{0}{1}` et que la prolongement est de classe
      :math:`\mathscr{C}^1`.

   #. 

      #. En utilisant les questions précédentes, trouver, pour :math:`N`
         entier naturel, une expression de

         .. math:: \int_0^1 \varphi_{2m}(t) \sin \big( (2N+1) \pi t \big) \d t

         en fonction de :math:`m`, :math:`N` et :math:`B_{2m}(0)`.

      #. En déduire la valeur de
         :math:`\sum\limits_{k=1}^\infty \frac{1}{k^{2m}}` en fonction
         de :math:`m` et de :math:`B_{2m}(0)`.

On rappelle que

.. math::

   \begin{aligned}
   B_n(1 - x) &= (-1)^n B_n(x),\\
   B_n'(x) &= n B_{n-1}(x).
   \end{aligned}

.. container:: elem_sol

   Pour :math:`k` et :math:`n` entiers strictement positifs, on définit:

   .. math:: I_{n, k} = \int_0^1 B_n(t) \cos(2 k \pi t) \d t.

   #. Pour tout entier :math:`p > 0`,

      .. math:: I_{2p, k} = \frac{(-1)^{p-1}}{(2 k \pi)^{2p}} \quad \text{et} \quad I_{2p+1,k} = 0.

      En effet, en utilisant deux intégrations par parties successives,

      .. math:: I_{n,k} = \frac{1}{4k^2 \pi^2} \big(B_{n-1}(1) - B_{n-1}(0) - I_{n-2, k} \big).

      De plus, :math:`I_{0,k} = 0`, :math:`I_{1,k} = 0`,
      :math:`I_{2,k} = \frac{1}{4 \pi^2}`. Donc,

      .. math:: \forall n \geqslant 3,\, I_{n,k} = - \frac{1}{4 k^2 \pi^2}I_{n-2, k}.

      On obtient ainsi le résultat annoncé.

   Pour tout entier naturel :math:`n` strictement positif, on pose:

   .. math:: \forall t \in \interoo{0}{1}, \quad \varphi_n(t) = \frac{B_n(t) - B_n(0)}{\sin(\pi t)}.

   #. Pour tout :math:`n \geq 2`, la fonction :math:`\varphi_n` est
      prolongeable par continuité à :math:`\interff{0}{1}` et le
      prolongement est de classe :math:`\mathscr{C}^1`. En effet,

      -  D’après les quotients de fonctions de classe
         :math:`\mathscr{C}^1` dont le dénominateur ne s’annule pas, la
         fonction :math:`\varphi_n` est de classe :math:`\mathscr{C}^1`
         sur :math:`\interoo{0}{1}`.

      -  La fonction :math:`B_n` étant polynomiale, elle est de classe
         :math:`\mathscr{C}^1` en :math:`0` et, en utilisant la formule
         de Taylor–Young,

         .. math::

            \begin{aligned}
            \varphi_n(t) &= \frac{B'_n(0)t + \frac{B''_n(0)}{2}t^2 + o(t^2)}{\pi t \big(1 + o(t) \big)} \\
            &= \frac{B'_n(0)}{\pi} + \frac{B''_n(0)}{2 \pi}t + o(t).
            \end{aligned}

         Ainsi,
         :math:`\lim\limits_{t \to 0} \varphi_n(t) = \frac{B'_n(0)}{\pi}`
         et :math:`\varphi_n` est une fonction prolongeable par
         continuité en :math:`0`.

      -  De plus, pour tout :math:`t` non nul,
         :math:`\varphi'_n(t) = \frac{B'_n(t) \sin(\pi t) - \big(B_n(t) - B_n(0) \big) \pi \cos(\pi t)}{\sin(\pi t)^2}`.
         Ainsi, en effectuant un développement limité à l’ordre
         :math:`2` du numérateur, alors
         :math:`\lim\limits_{t \to 0} \varphi'_n(t) = \frac{1}{2 \pi} B''_n(0)`.

         D’après le théorème de prolongement des dérivées,
         :math:`\varphi_n` est prolongeable en une fonction de classe
         :math:`\mathscr{C}^1` sur :math:`\interfo{0}{1}`.

         Enfin,
         :math:`\varphi_n(1-t) = (-1)^n \frac{B_n(t) - B_n(1)}{\sin(\pi t)}`.
         Comme, pour tout :math:`n \geqslant 2`,
         :math:`B_n(0) = B_n(1)`, alors la fonction :math:`\varphi_n`
         est bien prolongeable en une fonction de classe
         :math:`\mathscr{C}^1` sur :math:`\interff{0}{1}`.

   Pour tout :math:`N` entier naturel non nul et
   :math:`t \in \interoo{0}{1}`, on pose :

   .. math:: D_n(t) = 1 + 2 \sum_{k=1}^N \cos(2k \pi t) = \frac{\sin\big((2N+1) \pi t \big)}{\sin(\pi t)}.

   #. Cette quantité, appelée noyau de Dirichlet, s’exprime simplement à
      l’aide de la fonction sinus :

      .. math:: D_n(t) = \frac{\sin\big((2N+1) \pi t \big)}{\sin(\pi t)}.

      En effet, pour tout :math:`t \in \interoo{0}{1}`,
      :math:`\e^{2 \i k \pi t} \not= 1`. Ainsi, d’après la somme des
      termes d’une suite géométrique,

      .. math::

         \begin{aligned}
                 \sum_{k=0}^N \e^{2 \i k \pi t} &= \frac{\e^{2 \i (N+1) \pi} - 1}{\e^{2 \i \pi} - 1} \\
                 &= \e^{\i N \pi} \frac{\sin(N+1) \pi t}{\sin(\pi t)}. \\
                 \sum_{k=0}^N \cos(2 k \pi t) &= \cos(N \pi t) \frac{\sin \big((N+1) \pi t \big)}{\sin(\pi t)}\text{, en prenant les parties réelles,} \\
                 1 + 2 \sum_{k=1}^N \cos(2 k \pi t) &= 2 \frac{\cos(N \pi t) \sin \big((N+1) \pi t\big)}{\sin(\pi t)} - 1 \\
                 &= \frac{\sin\big((2N+1) \pi t \big) + \sin( \pi t)}{\sin(\pi t)} - 1 \\
                 &= \frac{\sin\big((2N+1) \pi t \big)}{\sin(\pi t)}.
         \end{aligned}

   #. Ainsi,

      .. math::

         \int_0^1 \varphi_{2m}(t) \sin \big((2N+1) \pi t \big) \d t
         = - B_{2m}(0) + 2 \sum_{k=1}^N \frac{(-1)^{m-1}}{(2 k \pi)^{2m}}.

      En effet, d’après la définition de :math:`\varphi_{2m}`,

      .. math::

         \begin{aligned}
         \int_0^1 \varphi_{2m}(t) \sin \big((2N+1) \pi t \big) \d t &= \int_0^1 \big(B_{2m}(t) - B_{2m}(0) \big) \frac{\sin\big((2N+1) \pi t \big)}{\sin(\pi t)} \d t \\
         &= \int_0^1 \big( B_{2m}(t) - B_{2m}(0) \big) \d t + \cdots \\
         &\cdots + 2 \sum_{k=1}^N \int_0^1 \big(B_{2m}(t) - B_{2m}(0) \big) \cos(2 k \pi t) \d t \\
         &= - B_{2m}(0) + 2 \sum_{k=1}^N \frac{(-1)^{m-1}}{(2 k \pi)^{2m}}.
         \end{aligned}

   #. D’après le lemme de Lebesgue,

      .. math:: \lim_{N\to+\infty} \int_0^1 \varphi_{2m}(t) \sin \big((2N+1) \pi t \big) \d t = 0

      et on obtient bien le résultat annoncé.

.. container:: remarque

   En utilisant les valeurs remarquables des premiers polynômes de
   Bernoulli, on obtient

   .. math::

      \begin{aligned}
      \sum_{k=1}^{+\infty} \frac{1}{k^2} &= 2 \pi^2 B_2(0) = \frac{\pi^2}{6} \\
      \sum_{k=1}^{+\infty} \frac{1}{k^4} &= -2^3 \pi^4 B_4(0) = \frac{\pi^4}{90}.
      \end{aligned}