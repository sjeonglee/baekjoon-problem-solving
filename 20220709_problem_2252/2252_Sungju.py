import sys
N_M = sys.stdin.readline().split()
N = int(N_M[0])
M = int(N_M[-1])

class Vertex:
  def __init__(self, id):
    self.id = id
    self.inbound = list() ## more fronter than self
    self.outbound = list() ## rearer than self

  def add_inbound(self, id):
    self.inbound.append(id)

  def add_outbound(self, id):
    self.outbound.append(id)

students = {}
for i in range(N):
  id = i+1
  students[id] = Vertex(id)

for _ in range(M):
  A_B = sys.stdin.readline().split()
  A = int(A_B[0])
  B = int(A_B[-1])
  students.get(A).add_outbound(B)
  students.get(B).add_inbound(A)

## to find starter vertex
  

## for print
for key, value in students.items():
  print(value.id)
  print(value.inbound)
  print(value.outbound)
