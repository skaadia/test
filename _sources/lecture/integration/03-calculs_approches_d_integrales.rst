Calculs approchés d’intégrales
==============================

Nous abordons dans cette section quelques méthodes dont le but est
d’estimer la valeur numérique de l’intégrale d’une fonction donnée
:math:`f` définie sur un domaine borné :math:`\interff{a}{b}`:

.. math:: I = \int_a^b f(t) \d t.

Ces méthodes nous fourniront une valeur approchée :math:`\widetilde{I}`
de l’intégrale :math:`I` de sorte que

.. math:: \widetilde{I} \approx I.

Soient :math:`a` et :math:`b` désignent deux réels tels que
:math:`a < b`. Pour tout entier naturel :math:`p` non nul, on note
:math:`(x_i)_{i\in\llbracket 0, p \rrbracket}` la subdivision régulière
de :math:`[a, b]` de pas :math:`\frac{b-a}{p}`. Ainsi, pour tout
:math:`i \in \llbracket 0, p \rrbracket`,

.. math:: x_i = a + i \frac{b-a}{p}.

.. container:: defi

   Une méthode d’intégration est d’\ *ordre* au moins :math:`n` si elle
   est exacte (*i.e.* :math:`\widetilde{I} = I`) pour les polynômes de
   degrés inférieurs ou égaux :math:`n` et non exacte pour au moins un
   polynôme de degré :math:`n+1`.

Méthode des rectangles à gauche
-------------------------------

La méthode des rectangles à gauche consiste, pour chacun des intervalles
de la subdivision, à approcher l’aire sous la courbe représentative de
:math:`f` par celle d’un rectangle dont la hauteur correspond à la
valeur de :math:`f` sur la borne de gauche. Plus précisément, on
considère la quantité :

.. math:: I_p^\mathrm{g}(f) = \frac{b-a}{p} \sum_{i=0}^{p-1} f(x_i).

.. container:: marginfigure

.. container:: prop

   La méthode des rectangles à gauche est d’ordre :math:`0`. De plus, si
   :math:`f` est de classe :math:`\mathscr{C}^1`, l’erreur commise est
   en :math:`O(1/p)`.

.. container:: elem_sol

   On suppose que :math:`f` désigne une fonction de classe
   :math:`\mathscr{C}^1` sur le segment :math:`\interff{a}{b}`. On note
   :math:`F` une primitive de :math:`f` et
   :math:`M_1 = \sup_{\interff{a}{b}} \module{f'}`.

   #. D’après la formule de Taylor avec reste intégal, pour tout
      :math:`i \in \interent{0}{p-1}`,

      .. math:: \module{F(x_{i+1}) - F(x_i) - (x_{i+1} - x_i) F'(x_i)} \leq \frac{M_1}{2} (x_{i+1}-x_i)^2.

   #. En utilisant la relation de Chasles,

      .. math::

         \begin{aligned}
         \module{\int_{\interff{a}{b}} f - I_p^\mathrm{g}(f)}
         &\leq \sum_{i=1}^{p-1} \module{\int_{\interff{x_i}{x_{i+1}}} f - (x_{i+1} - x_i) f(x_i)}\\
         &\leq \sum_{i=1}^{p-1} \frac{M_1}{2} (x_{i+1} - x_i)^2\\
         % &\leq \frac{M_1}{2} (b - a) \sum_{i=1}^{p-1} (x_{i+1} - x_i)\\
         &\leq \frac{M_1 (b-a)^2}{2 p}.
         \end{aligned}

   #. De plus, on montre que cette borne est atteinte pour
      :math:`f : x \mapsto x - a`.

   #. La méthode des rectangles à gauche est exacte si :math:`f` est
      constante. Cependant, le calcul précédent montre que si
      :math:`f : x \mapsto x - a`, alors la méthode ne donne pas la
      valeur exacte de l’intégrale. La méthode est donc d’ordre
      :math:`0`.

Méthode des rectangles médians
------------------------------

La méthode des rectangles médians consiste, pour chacun des intervalles
de la subdivision, à approcher l’aire sous la courbe représentative de
:math:`f` par celle d’un rectangle dont la hauteur correspond à la
valeur de :math:`f` au milieu de la subdivision. Plus précisément, on
considère la quantité :

.. math:: I_p^\mathrm{m}(f) = \frac{b-a}{p} \sum_{i=0}^{p-1} f\left(\frac{x_i + x_{i+1}}{2} \right).

.. container:: prop

   La méthode des rectangles médians est d’ordre :math:`1`. De plus, si
   :math:`f` est de classe :math:`\mathscr{C}^2`, l’erreur commise est
   en :math:`O(1/p^2)`.

.. container:: marginfigure

.. container:: elem_sol

   On suppose que :math:`f` désigne une fonction de classe
   :math:`\mathscr{C}^2` sur le segment :math:`\interff{a}{b}`. On note
   :math:`F` une primitive de :math:`f` et
   :math:`M_2 = \sup_{\interff{a}{b}} \module{f''}`. Pour tout entier
   :math:`i \in \interent{0}{p-1}`, on pose
   :math:`\gamma_i = \frac{x_i + x_{i+1}}{2}` le milieu du segment
   :math:`\interff{x_i}{x_{i+1}}`.

   #. Soit :math:`i \in \interent{0}{p-1}`. Un simple calcul ou le
      graphique suivant permet de montrer que :

      .. math:: (x_{i+1} - x_i) f(\gamma_i) = \int_{x_i}^{x_{i+1}} \left(f(\gamma_i) + (t - \gamma_i) f'(\gamma_i) \right) \d t.

      .. figure:: ../../img/rectangles_medians.png
         :figclass: margin
         :alt: image

   #. Ainsi, d’après la formule de Taylor avec reste intégral,

      .. math::

         \begin{aligned}
         \module{F(x_{i+1}) - F(x_i) - (x_{i+1} - x_i) F'(\gamma_i)}
         &= \module{\int_{x_i}^{x_{i+1}} \left(f(t) - f(\gamma_i) - (t - \gamma_i) f'(\gamma_i)\right) \d t}\\
         &\leq \frac{M_2}{24} (x_{i+1} - x_i)^3.
         \end{aligned}

   #. Comme pour la méthode des rectangles à gauche, la formule de
      Chasles permet de montrer que

      .. math:: \module{\int_{[a,b]} f - I_p^\mathrm{m}(f)} \leq \frac{M_2 (b-a)^3}{24 p^2}.

   #. De plus, on montre que cette borne est atteinte pour
      :math:`f : x \mapsto (x - a)^2`.

   #. La méthode des rectangles médians est exacte si :math:`f` est un
      polynôme de degré :math:`1`. Cependant, si :math:`f` est la
      fonction :math:`x \mapsto (x - a)^2`, le calcul précédent montre
      que la méthode des rectangles médians ne donne pas la valeur
      exacte de l’intégrale. La méthode est donc d’ordre :math:`1`.

Méthode des trapèzes
--------------------

La méthode des trapèzes consiste, pour chacun des intervalles de la
subdivision, à approcher l’aire sous la courbe représentative de
:math:`f` par celle d’un trapèze. Plus précisément, on considère la
quantité :

.. math:: I_p^\mathrm{t}(f) =  \frac{b-a}{p} \sum_{i=0}^{p-1} \frac{f(x_i) + f(x_{i+1})}{2}.

.. container:: marginfigure

.. container:: prop

   La méthode des trapèzes est d’ordre :math:`2`. De plus, si :math:`f`
   est de classe :math:`\mathscr{C}^2`, l’erreur commise est en
   :math:`O(1/p^2)`.

.. container:: elem_sol

   On suppose que :math:`f` est une fonction de classe
   :math:`\mathscr{C}^2` et on note
   :math:`M_2 = \sup_{[a,b]} \module{f''}`. Pour tout
   :math:`i \in \interent{0}{p-1}`, on note :math:`\phi_i`
   l’approximation affine sur :math:`\interff{x_i}{x_{i+1}}` de
   :math:`f` et :math:`g_i = f - \phi_i`.

   #. À l’aide de deux intégrations par parties successives, on montre
      que, pour tout :math:`i \in \interent{0}{p-1}`,

      .. math:: \int_{x_i}^{x_{i+1}} f''(t) (t - x_i) (x_{i+1} - t) \d t = - 2 \int_{x_i}^{x_{i+1}} g_i(t) \d t.

   #. D’après la relation précédente, on établit que

      .. math::

         \begin{aligned}
         \module{\int_{x_i}^{x_{i+1}} f(t) \d t - I_p^\mathrm{t}(f)}
         &\leq \int_{x_i}^{x_{i+1}} \module{f(t) - \phi_i(t)} \d t\\
         &\leq \frac{M_2}{2} \int_{x_i}^{x_{i+1}} (t - x_i) (x_{i+1} - t) \d t\\
         &\leq \frac{M_2}{2} \cdot \frac{(b - a)^3}{6}.
         \end{aligned}

   #. Comme pour les méthodes précédentes, on utilise ensuite la
      relation de Chasles pour obtenir

      .. math:: \module{\int_{[a,b]} f - I_p^\mathrm{t}(f)} \leq \frac{M_2 (b-a)^3}{12 p^2}.

   #. De plus, on montre que cette borne est atteinte pour
      :math:`f : x \mapsto (x - a)^2`.

   #. La méthode des trapèzes est exacte si :math:`f` est un polynôme de
      degré :math:`1`. Cependant, si :math:`f` est la fonction
      :math:`x \mapsto (x - a)^2`, le calcul précédent montre qur la
      méthode des trapèzes ne donne pas la valeur exacte de l’intégrale.
      La méthode est donc d’ordre :math:`2`.

.. container:: remarque

   Lorsque :math:`f` est de classe :math:`\mathscr{C}^2` et convexe,
   alors :math:`f'' \geq 0` et, pour tout :math:`p` entier naturel,
   :math:`\int_{[a,b]} f \leq I_p^\mathrm{t}(f)`. On obtient ainsi une
   valeur approchée par excès de l’intégrale.

Méthode de Simpson
------------------

La méthode de Simpson consiste, pour chacun des intervalles de la
subdivision, à approcher la fonction :math:`f` par un polynôme de degré
inférieur ou égal à :math:`2`. Plus précisément, on considère la
quantité :

.. math:: I_p^\mathrm{s}(f) = \frac{b-a}{6 p} \sum_{i=0}^{p-1} \left[f(x_i)+ 4 f\left(\frac{x_i + x_{i+1}}{2}\right) + f(x_{i+1})\right].

.. container:: prop

   Dans la méthode de Simpson, si :math:`f` est de classe
   :math:`\mathscr{C}^4`, l’erreur commise est en :math:`O(1/p^4)`.

.. container:: elem_sol

   On suppose que :math:`f` est une fonction de classe
   :math:`\mathscr{C}^4` sur le segment :math:`[a, b]`. On pose
   :math:`M_4 = \sup_{[a,b]} \module{f^{(4)}}`.

   Pour tout :math:`i \in \interent{0}{p-1}`, notons
   :math:`\gamma_i = \frac{x_i + x_{i+1}}{2}` le milieu de la
   subdivision et :math:`h_i = \frac{x_{i+1} - x_i}{2}` la moitié de sa
   longueur.

   #. D’après la formule de Taylor avec reste intégral appliquée à une
      primitive :math:`F` de :math:`f`,

      .. math::

         \begin{aligned}
         F(\gamma_i + h_i)
         &= \begin{aligned}[t]F(\gamma_i) + h_i f(\gamma_i) + \frac{h_i{}^2}{2} f'(\gamma_i) + \frac{h_i{}^3}{6} f''(\gamma_i) + \frac{h_i{}^4}{24} f'''(\gamma_i) \\ + \frac{h_i{}^5}{24} \int_0^1 (1 - t)^4 f^{(4)}(\gamma_i + t h_i) \d t,\\
         \end{aligned} \\
         f(\gamma_i - h_i)
         &= \begin{aligned}[t]F(\gamma_i) - h_i f(\gamma_i) + \frac{h_i{}^2}{2} f'(\gamma_i) - \frac{h_i{}^3}{6} f''(\gamma_i) + \frac{h_i{}^4}{24} f'''(\gamma_i) \\ - \frac{h_i{}^5}{24} \int_0^1 (1 - t)^4 f^{(4)}(\gamma_i - t h_i) \d t.
         \end{aligned}
         \end{aligned}

      Comme :math:`\gamma_i - h_i = x_i` et
      :math:`\gamma_i + h_i = x_{i+1}`, en soustrayant les deux
      relations précédentes, on obtient

      .. math::

         \begin{aligned}
         F(x_{i+1}) - F(x_i)
         &= 2 h_i f(\gamma_i) + \frac{h_i^3}{3} f''(\gamma_i) + \frac{h_i^5}{24} \int_0^1 (1 - t)^4 \left[f^{(4)}(\gamma_i + t h_i) + f^{(4)}(\gamma_i - t h_i)\right] \d t.
         % \\
         % \int_{x_i}^{x_{i+1}} f(t) \d t
         % &= \frac{b - a}{p} f(\gamma_i) + \frac{(b - a)^3}{24 p^3} f''(\gamma_i) + \frac{(b - a)^5}{32 \times 24 p^5} \int_0^1 (1 - t)^4 \left[f^{(4)}(\gamma_i + t h_i) + f^{(4)}(\gamma_i - t h_i)\right] \d t.
         \end{aligned}

      Ainsi,

      .. math::

         \begin{aligned}
         &\module{\int_{x_i}^{x_{i+1}} f(t) \d t - \frac{h_i}{3} \left[f(x_i) + 4 f(\gamma_i) + f(x_{i+1})\right]}\\
         &\leq \module{\frac{h_i}{3} \left[f(x_i) - 2 f(\gamma_i) + f(x_{i+1}) - h_i^2 f''(\gamma_i)\right]} + \frac{h_i^5 2 M_4}{5! p^5}.
         \end{aligned}

   #. En utilisant la formule de Taylor avec reste intégral pour la
      fonction :math:`f` sur :math:`[\gamma_i - h_i, \gamma_i]` et
      :math:`[\gamma_i, \gamma_i + h_i]`, on obtient comme précédemment

      .. math:: \module{f(x_{i+1}) + f(x_i) - 2 f(\gamma_i) - h_i^2 f(\gamma_i)} \leq \frac{h_i^4 \times 2 M_4}{4!}.

   #. Finalement,

      .. math::

         \begin{aligned}
         \module{\int_{x_i}^{x_{i+1}} f(t) \d t - \frac{h_i}{3} \left[f(x_i) + 4 f(\gamma_i) + f(x_{i+1})\right]}
         &\leq h_i^5 \left[\frac{2}{3 \times 4!} + \frac{2}{5!}\right]\\
         &\leq \frac{2 h_i^5}{45}
         \leq \frac{(x_{i+1} - x_i)^5}{720}.
         \end{aligned}

   #. On conclut à l’aide de la relation de Chasles :

      .. math:: \module{I_p^s(f) - \int_a^b f(t) \d t} \leq \frac{M_4 (b-a)^5}{720 p^4}.

Et ensuite ?
------------

Nous constatons que, pour chacune des méthodes précédentes, la stratégie
est identique :

-  découper le segment en une subdivision régulière
   :math:`a = x_0 \leq \cdots \leq x_n = b`,

-  sur chacun des intervalles de cette subdivision, approcher la
   fonction par une fonction dont l’intégrale est plus simple.

   Sur l’intervalle :math:`[x_i, x_{i+1}]` : pour la méthode des
   rectangles, on approche la fonction par une droite horizontale, pour
   celle des trapèzes, par une droite affine passant par les points
   :math:`(x_i, f(x_i))` et :math:`(x_{i+1}, f(x_{i+1}))`.

Plus généralement, on peut découper le segment :math:`[x_i, x_{i+1}]` en
une subdivision régulière
:math:`x_i = y_{i,0} \leq \ldots \leq y_{i,p} \leq x_{i+1}`. On peut
ensuite approcher la fonction par le polynôme d’interpolation de
Lagrange qui passe par les points de coordonnées
:math:`(y_{i,0}, f(y_{i,0}), \ldots, (y_{i,p}, f(y_{i,p}))`.

Cette méthode est appelée *méthode de Newton–Cotes*.

Plus précisément, on considère une subdivision
:math:`0 = y_0 \leq \ldots \leq y_p = 1` de l’intervalle
:math:`\interff{0}{1}` et on note :math:`(L_0,\ldots,L_p)` la famille
des `polynômes d’interpolation de
Lagrange <#sec:polynomes_de_lagrange>`__ associée à cette subdivision,
i.e.

.. math:: \forall\ i \in \interent{0}{p},\, L_i(X) = \prod_{j \neq i} \frac{X - y_j}{y_i - y_j}.

On pose alors :math:`\lg_j = \int_0^1 L_j(t) \d t`.

On approche alors l’intégrale de :math:`f` sur :math:`[x_i, x_{i+1}]`
par la somme

.. math:: I_p^i(f) = (x_{i+1} - x_i) \sum_{j=0}^p \lg_j g(x_i + (x_{i+1} - x_i) y_j),

puis l’intégrale sur le segment :math:`[a, b]` par

.. math:: I_p(f) = \sum_{i=0}^{n-1} (x_{i+1} - x_i) \sum_{j=0}^p \lg_j f(x_i + (x_{i+1} - x_i) y_j).

On peut montrer que :

-  lorsque :math:`n = 1`, on retrouve la formule des trapèzes.

-  lorque :math:`n = 2`, on retrouve la méthode de Simpson.

| On peut montrer que la méthode de Simpson est d’ordre :math:`3`. On
  peut augmenter le nombre des nœuds où est évaluée la fonction à
  intégrer (:math:`2` nœuds pour la méthode des trapèzes, :math:`3` pour
  la méthode de Simpson,…). Cependant, lorsque le nombre de nœuds
  dépasse :math:`8`, des coefficients négatifs apparaissent ce qui
  engendre des erreurs d’arrondis.