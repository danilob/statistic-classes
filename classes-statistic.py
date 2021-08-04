values = [
   33.21,42.13,38.27,41.81,26.73,38.69,39.85,40.02,27.71,36.54,46.54,44.68,37.83,40.5,26.01,47.01,31.56,42.77,41.84,12.83,41.3,39.7,20.87,42.23,27.81,31.85,34.47,30.59
]

n = len(values) #calcula o tamanho do vetor
print("Tamanho de dados: ",n)
R = max(values) - min(values) #amplitude maior - menor
print("Amplitude: ",R)

if (n<25):
    K = 5
else:
    K = n**0.5 #raiz quadrada **0.5

K = int(round(K))
print("Numero de classes",K)

h = R/(K*1.0)
print("Amplitude do intervalo", h)

min_i = min(values)
vector_classes = []

#12.83   |-- 12.83+h
#12.83+h |-- 12.83+2h


for i in range(K):
    min_k = min_i+i*h
    max_k = min_i+(i+1)*h
    f = 0
    for j in range(n):
        if (values[j]>=min_k and values[j]<=max_k):
            f = f + 1 
    class_value = {
        "min": min_k,
        "max": max_k,
        "f_i": f
    }
    print(class_value)
    vector_classes.append(class_value)

x_f = 0
f = 0
for i in range(K):
    Xi = (vector_classes[i]["max"] + vector_classes[i]["min"])/2
    fi = vector_classes[i]["f_i"]
    x_f = x_f + Xi*fi
    f = f + fi

print(x_f)
print(f)
x_barra = x_f/f
print("Media x barra",x_barra)

x = 0
for i in range(n):
    x = values[i] + x

x = x/n
print("Mu",x)
