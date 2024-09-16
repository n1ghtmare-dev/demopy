# DNA compiler
d = {"A": "T", "T": "A", "C": "G", "G": "C"}

def dna(inp: str) -> str:
  res = []
  for i in inp:
    i = d[i] if i in list(d) else i
    res.append(i)
  return "".join(res)

print(dna("TA"))
