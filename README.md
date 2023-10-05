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

### Custom Resource Toepassen

Om deze aangepaste bron toe te passen op je Kubernetes-cluster, gebruik je het volgende commando:

```bash
kubectl apply -f example.yml
```

### Custom Resource Controleren

Je kunt de aangepaste bronnen controleren met het volgende commando:

```bash
kubectl get example
```

Dit zal alle custom resourceinstanties weergeven die zijn gemaakt op basis van je definitie.

Dit voorbeeld illustreert hoe je Kubernetes Custom Resources kunt definiëren, toepassen en gebruiken om aangepaste objecttypen te maken en beheren die zijn afgestemd op de behoeften van je applicatie. Custom Resources bieden ontwikkelaars een krachtige tool om Kubernetes aan te passen voor specifieke toepassingen.

## Optimalisatie van Microservices met Custom Resources

Een van de meest opwindende toepassingen van Kubernetes Custom Resources is hun vermogen om de implementatie van microservices-architecturen te vereenvoudigen en optimaliseren. Laten we eens kijken hoe Custom Resources kunnen bijdragen aan een effectievere microservices-implementatie.

### Schaalbare Microservices

Een kernaspect van microservices-architecturen is de mogelijkheid om individuele microservices onafhankelijk te schalen op basis van de actuele belasting en behoeften van de applicatie. Met Kubernetes Custom Resources kunnen ontwikkelaars aangepaste schaalregels definiëren voor specifieke microservices. Dit betekent dat je de schaalbaarheid van elke microservice kunt aanpassen aan de hand van de door jou gedefinieerde criteria.

### Service Mesh Integratie

Service meshes, zoals Istio of Linkerd, worden vaak gebruikt om de communicatie en beveiliging tussen microservices te beheren. Kubernetes Custom Resources kunnen naadloos worden geïntegreerd met service meshes, waardoor ontwikkelaars aangepaste instellingen en configuraties kunnen toepassen op specifieke microservices. Dit vergemakkelijkt de controle over het gedrag en de interactie van microservices binnen de architectuur.

### Applicatiespecifieke Configuraties

Elke microservice kan unieke configuraties en vereisten hebben. Met Custom Resources kunnen ontwikkelaars applicatiespecifieke configuratieparameters definiëren en beheren voor elke microservice. Dit maakt het mogelijk om flexibel in te spelen op de behoeften van elke microservice zonder de complexiteit van globale configuratiebestanden.

## Conclusie

Kubernetes Custom Resources zijn een waardevolle troef voor softwareontwikkelaars. Ze bieden flexibiliteit, aanpasbaarheid en vereenvoudiging in het beheer van applicaties op Kubernetes. Deze extensies stellen ontwikkelaars in staat om specifieke applicatievereisten te modelleren, schaalbaarheid te verbeteren, en microservices-architecturen te optimaliseren.

Als softwareontwikkelaar kun je met Kubernetes Custom Resources complexe applicaties effectief beheren en uitbreiden, terwijl je profiteert van de voordelen van Kubernetes. Het loont de moeite om deze krachtige tool te verkennen en te ontdekken hoe deze je kan helpen bij het bouwen van veerkrachtige en schaalbare applicaties in de wereld van containerorkestratie.

Kortom, Kubernetes Custom Resources zijn een essentieel instrument voor ontwikkelaars die de mogelijkheden van Kubernetes ten volle willen benutten. Ze bieden maatwerkoplossingen voor complexe uitdagingen in de moderne applicatieontwikkeling.

## Bronnen

* Custom resources. (2023, August 8). Kubernetes. <https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/>  
* Extend the Kubernetes API with CustomResourceDefinitions. (2023, September 20). Kubernetes. <https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/>
* The Distributed System ToolKit: Patterns for composite containers. (2020, July 24). Kubernetes. <https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns/>
* What’s a service mesh? (n.d.). <https://www.redhat.com/en/topics/microservices/what-is-a-service-mesh>
