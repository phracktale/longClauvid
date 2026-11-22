# Calculs d'appui pour les entrées B013 à B021 de registre/banque.yaml (agent statistique, 2026-11-22).
# Chaque bloc donne ses hypothèses. Aucune donnée individuelle : seulement des chiffres publiés.
import math
from scipy.stats import norm
from scipy.stats import nct, t as tdist
from scipy.optimize import brentq

def puissance_t(d, n1, n2, alpha):
    """Test t bilatéral à deux groupes, loi t non centrée."""
    df = n1+n2-2
    nc = d*math.sqrt(n1*n2/(n1+n2))
    tc = tdist.isf(alpha/2, df)
    haut = nct.sf(tc, df, nc)
    bas = nct.cdf(-tc, df, nc)
    if bas != bas:  # la queue opposée, négligeable, peut renvoyer NaN pour un grand décentrage
        bas = 0.0
    return haut + bas

def n_deux_proportions(p0, p1, alpha, puissance):
    """Effectif par groupe, approximation normale, variances non regroupées."""
    za, zb = norm.isf(alpha/2), norm.isf(1-puissance)
    return (za+zb)**2*(p0*(1-p0)+p1*(1-p1))/(p0-p1)**2

def puissance_allelique(or_, p, n_cas, n_tem, alpha):
    """Test allélique additif, approximation normale du log-OR.
    SE = sqrt(1/(2*n_cas*p*(1-p)) + 1/(2*n_tem*p*(1-p))), p = fréquence de l'allèle chez les témoins."""
    se = math.sqrt(1/(2*n_cas*p*(1-p)) + 1/(2*n_tem*p*(1-p)))
    z = abs(math.log(or_))/se
    za = norm.isf(alpha/2)
    return norm.cdf(z-za) + norm.cdf(-z-za)

def cas_necessaires(or_, p, alpha, puissance, ratio_tem=10):
    lo, hi = 10, 10_000_000
    while hi-lo > 1:
        mid = (lo+hi)//2
        if puissance_allelique(or_, p, mid, mid*ratio_tem, alpha) >= puissance: hi = mid
        else: lo = mid
    return hi

def e_value(rr):
    rr = 1/rr if rr < 1 else rr
    return rr + math.sqrt(rr*(rr-1))

print("== 1. HLA ==")
fc, ft = 0.217, 0.232  # DQA1*05:01, DecodeME : fréquence cas / témoins
or_dqa = (fc/(1-fc))/(ft/(1-ft))
print(f"OR allélique DQA1*05:01 déduit des fréquences 21,7 % / 23,2 % : {or_dqa:.3f}")
for p in (0.1, 0.2, 0.3, 0.4, 0.5):
    print(f"  Puissance HGI (6 450 cas, 46 208 témoins) pour OR 1,06, fréquence {p:.1f}, alpha 0,05 : {puissance_allelique(1.06,p,6450,46208,0.05):.2f}")
for p in (0.01, 0.02, 0.05):
    print(f"  Puissance HGI pour DRB1*11:04 OR 1,18, fréquence {p:.2f}, alpha 0,05 : {puissance_allelique(1.18,p,6450,46208,0.05):.2f}")
print(f"  Cas nécessaires (10 témoins par cas) pour répliquer OR {or_dqa:.3f} à fréquence 0,232, alpha 0,05, puissance 0,90 : {cas_necessaires(or_dqa,0.232,0.05,0.90)}")
print(f"  Idem pour OR 1,06 à fréquence 0,3 : {cas_necessaires(1.06,0.3,0.05,0.90)}")

print("== 2. FOXP4 ==")
for or_ in (1.63, 1.34, 1.16):
    print(f"  Puissance 23andMe Européens (42 899 cas, 94 721 témoins), fréquence 0,016, OR {or_}, alpha 0,05 : {puissance_allelique(or_,0.016,42899,94721,0.05):.3f}")
print(f"  Puissance DecodeME (15 579 cas, 259 909 témoins), fréquence 0,016, OR 1,16 : {puissance_allelique(1.16,0.016,15579,259909,0.05):.3f}")
print(f"  Puissance DecodeME, fréquence 0,016, OR 1,34 : {puissance_allelique(1.34,0.016,15579,259909,0.05):.3f}")

print("== 3. Valeurs E (VanderWeele et Ding) ==")
for nom, est, borne in (("Grossesse PCORnet HR 0,86", 0.86, 0.90), ("Grossesse N3C HR 0,70", 0.70, 0.74)):
    print(f"  {nom} : valeur E {e_value(est):.2f} ; pour la borne {borne} : {e_value(borne):.2f}")
for nom, est in (("Apnée PCORnet OR 1,12", 1.12), ("Apnée N3C OR 1,75", 1.75)):
    print(f"  {nom} (OR pris comme rapport de risques, issue supposée rare) : valeur E {e_value(est):.2f}")
# Hypermobilité : issue fréquente (32 %), on prend RR ~ racine(OR)
for nom, est in (("Hypermobilité OR 1,33", 1.33), ("borne basse 1,10", 1.10)):
    print(f"  {nom} : RR approché racine(OR) = {math.sqrt(est):.3f} ; valeur E {e_value(math.sqrt(est)):.2f}")

print("== 4. Cohorte mononucléose : 18 formes sévères, 58 rétablis ==")
for alpha, lib in ((0.05, "alpha 0,05"), (0.05/3, "Bonferroni sur 3 cytokines"), (0.05/10, "Bonferroni sur 10 cytokines")):
    d = brentq(lambda x: puissance_t(x, 18, 58, alpha)-0.80, 0.01, 2.5)
    print(f"  Plus petit écart standardisé détectable à 80 % de puissance, {lib} : d = {d:.2f}")
for d in (0.5, 0.8):
    n1 = brentq(lambda n: puissance_t(d, n, 3*n, 0.05/3)-0.90, 3, 100000)
    print(f"  Réplication d = {d}, 3 témoins par cas, alpha 0,05/3, puissance 0,90 : {math.ceil(n1)} cas et {math.ceil(3*n1)} témoins")

print("== 5. UK Biobank : cas incidents nécessaires ==")
for d in (0.2, 0.3, 0.5):
    alpha = 0.05/14
    n = (norm.isf(alpha/2)+norm.isf(0.10))**2/d**2  # groupe témoin très grand : variance dominée par les cas
    print(f"  d = {d}, alpha 0,05/14, puissance 0,90, témoins très nombreux : {math.ceil(n)} cas incidents")

print("== 6. Apnée : comparaison traités / non traités ==")
for p0 in (0.05, 0.15):
    for rr in (0.8, 0.9):
        n = n_deux_proportions(p0, p0*rr, 0.05, 0.80)
        print(f"  Risque de base {p0:.2f}, rapport de risques {rr} : {math.ceil(n)} personnes par groupe")
