Interprétation géométrique de l'intégration par parties
=======================================================


.. prf:theorem:: Continuité de la Trace (admis)

    Soit :math:`f` de classe :math:`\mathscr{C}^1` sur :math:`[a, b]` telle que :math:`f'` soit strictement positive sur :math:`[a, b]`. Alors,

    .. math:: \int_{a}^{b} f(t) \d t + \int_{f(a)}^{f(b)} f^{-1}(t) \d t = b f(b) - a f(a).



.. figure:: ../../img/i_01-une_propriete_geometrique_de_l_integrale.png
  :alt: Description de la figure


.. prf:proof::
    Comme :math:`f' > 0`, alors :math:`f` est strictement croissante. Comme :math:`f` est continue, d'après le théorème de la bijection monotone, :math:`f` réalise une bijection de :math:`[a, b]` sur :math:`[f(a), f(b)]`.
    
    On utilise le changement de variable :math:`\phi : [a, b] \to [f(a), f(b)],\, u \mapsto f(u)`. Alors, :math:`\phi` est de classe :math:`\mathscr{C}^1` et
    
    .. math:: 

        \begin{align*}
        \int_{f(a)}^{f(b)} f^{-1}(t) \d t
        &= \int_a^b f^{-1}(f(u)) f'(u) \d u\\
        &= \int_a^b u f'(u) \d u\\
        &= \left[u f(u)\right]_a^b - \int_a^b f(u) \d u,
        \end{align*}

    où on a réalisé une intégration par parties.

    Finalement,

    .. math:: \int_a^b f(t) \d t + \int_{f(a)}^{f(b)} f^{-1}(t) \d t = b f(b) - a f(a).
    
