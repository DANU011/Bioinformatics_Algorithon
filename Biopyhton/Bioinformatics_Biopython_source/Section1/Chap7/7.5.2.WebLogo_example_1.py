#7.5.2.WebLogo_example_1.py

from Bio.motifs import Motif
from Bio import motifs
from Bio.Seq import Seq
import weblogo

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


instances = [Seq("TACAA"),
            Seq("TACGC"),
            Seq("TACAC"),
            Seq("TACCC"),
            Seq("AACCC"),
            Seq("AATGC"),
            Seq("AATGC"),
            ]

m = motifs.create(instances)

print(m.counts)
m.weblogo("test2.png", format='png')



