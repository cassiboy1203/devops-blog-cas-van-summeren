# Optimaliseer Applicatiebeheer en Uitbreiding: Een Diepgaande Duik in Kubernetes Custom Resources voor Ontwikkelaars

*Cas van Summeren*, October 2023
<hr>

## Inhoudsopgave

## Inleiding

In de wereld van softwareontwikkeling draait alles om snelheid, schaalbaarheid en efficiëntie. Als softwareontwikkelaar ben je altijd op zoek naar krachtige tools om complexe applicaties moeiteloos te beheren en uit te breiden. Kubernetes heeft al veel veranderd in container- en microservices-beheer, maar er is nog een krachtige troef: Kubernetes Custom Resources.

Deze blogpost duikt dieper in Kubernetes Custom Resources en onderzoekt hoe ze ontwikkelaars kunnen helpen bij het effectief beheren en uitbreiden van complexe applicaties. We beginnen met het begrijpen van wat Kubernetes Custom Resources zijn, waarom ze relevant zijn voor ontwikkelaars, en welke voordelen ze bieden ten opzichte van traditionele Kubernetes-resources. We zullen ook laten zien hoe ontwikkelaars aangepaste Kubernetes-resources kunnen definiëren om specifieke applicatievereisten te modelleren en hoe dit kan bijdragen aan de vereenvoudiging en optimalisatie van microservices-architecturen.

## Wat zijn Kubernetes Custom Resources?

Kubernetes is al lang de gouden standaard voor containerorkestratie in de wereld van cloud-native applicaties geweest. Het biedt de krachtige mogelijkheid om containerized applicaties op te schalen en te beheren. Maar wat als je de mogelijkheden van Kubernetes verder zou kunnen aanpassen om specifieke behoeften van jouw applicatie te ondersteunen? Dit is precies waar Kubernetes Custom Resources in beeld komen.

### Definitie van Kubernetes Custom Resources

Kubernetes Custom Resources, vaak afgekort als CRs, zijn extensies van de Kubernetes API waarmee je aangepaste bronnen kunt definiëren en beheren die specifiek zijn voor jouw applicatie. In wezen kun je met Custom Resources je eigen Kubernetes-objecttypen creëren, afgestemd op de eisen en vereisten van je applicatie.

### Relevantie voor Ontwikkelaars

Maar waarom zouden ontwikkelaars zich bezighouden met Custom Resources? De relevantie ervan voor ontwikkelaars ligt in de mogelijkheid om de infrastructuur op applicatieniveau te definiëren en aan te passen zonder diepgaande kennis van Kubernetes-internals. In plaats van te worstelen met complexe YAML-bestanden en manifesten, kunnen ontwikkelaars zich richten op het beschrijven van de gewenste toestand van hun applicaties op een meer abstract niveau. Dit maakt het ontwikkelen en beheren van applicaties in Kubernetes aanzienlijk efficiënter.

## Definiëren en Gebruiken van Custom Resources

Nu we weten wat Kubernetes Custom Resources zijn, laten we eens kijken hoe je ze kunt definiëren en gebruiken om specifieke applicatievereisten te modelleren. We zullen een praktisch voorbeeld bekijken om deze concepten te verduidelijken.
Custom Resource Definition (CRD)

Allereerst moet je een Custom Resource Definition (CRD) maken. Dit definieert het nieuwe aangepaste bronobjecttype dat je wilt gebruiken. Hier is een voorbeeld van een CRD-definitie in YAML-formaat:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: example.stable.example.com
spec:
  group: stable.example.com
  names:
    plural: example
    kind: example
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                string:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  scope: Namespaced
```

Dit definieert een Custom Resource example onder de api stable.example.com. Het vereist de volgende waardes van implementatie van example om de volgende de properties te hebben: string, image en replicas.

### CRD toepassen

Nadat je de CRD hebt gedefinieerd, moet je deze toepassen op je Kubernetes-cluster met het volgende commando:

```bash
kubectl apply -f example-crd.yml
```

Dit zal de definitie van de Custom Resource aan je cluster toevoegen.
Gebruik van Custom Resources

Nu kun je Custom Resources van het nieuwe type maken en gebruiken. Hier is een voorbeeld van een Custom Resource YAML-definitie:

```yaml
apiVersion: stable.example.com/v1
kind: example
metadata:
  name: example-instance
spec:
  replicas: 1
  string: "string"
  image: "ubuntu:latest"

```

Dit voorbeeld maakt een aangepaste bron met de naam "example-instance" met specifieke eigenschappen zoals string, replicas, en image.

### Aangepaste Resource Toepassen

Om deze aangepaste bron toe te passen op je Kubernetes-cluster, gebruik je het volgende commando:

```bash
kubectl apply -f example.yml
```

### Aangepaste Resource Controleren

Je kunt de aangepaste bronnen controleren met het volgende commando:

```bash
kubectl get example
```

Dit zal alle aangepaste broninstanties weergeven die zijn gemaakt op basis van je definitie.

Dit voorbeeld illustreert hoe je Kubernetes Custom Resources kunt definiëren, toepassen en gebruiken om aangepaste objecttypen te maken en beheren die zijn afgestemd op de behoeften van je applicatie. Custom Resources bieden ontwikkelaars een krachtige tool om Kubernetes aan te passen voor specifieke toepassingen.

## Optimalisatie van Microservices met Custom Resources

## Conclusie

## Bronnen

* Custom resources. (2023, August 8). Kubernetes. <https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/>  
* Extend the Kubernetes API with CustomResourceDefinitions. (2023, September 20). Kubernetes. <https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/>
