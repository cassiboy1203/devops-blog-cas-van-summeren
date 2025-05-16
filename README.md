# Optimaliseer Applicatiebeheer en Uitbreiding: Een Diepgaande Duik in Kubernetes Custom Resources voor Ontwikkelaars <!-- omit from toc -->

*Cas van Summeren*, Februari 2025
<hr>

## Inhoudsopgave <!-- omit from toc -->

- [Inleiding](#inleiding)
- [Wat zijn Kubernetes Custom Resources?](#wat-zijn-kubernetes-custom-resources)
- [Waarom zou je Kubernetes Custom Resources willen gebruiken?](#waarom-zou-je-kubernetes-custom-resources-willen-gebruiken)
- [Definiëren en Gebruiken van Custom Resources](#definiëren-en-gebruiken-van-custom-resources)
  - [Custom Resource Definition (CRD)](#custom-resource-definition-crd)
    - [Uitleg van de CRD](#uitleg-van-de-crd)
    - [CRD toepassen in Kubernetes](#crd-toepassen-in-kubernetes)
  - [Custom Resource (CR)](#custom-resource-cr)
    - [Uitleg van de Custom Resource](#uitleg-van-de-custom-resource)
    - [De Custom Resource deployen](#de-custom-resource-deployen)
    - [Controleren of de Custom Resource is toegevoegd](#controleren-of-de-custom-resource-is-toegevoegd)
  - [Controller maken](#controller-maken)
    - [Voorbeeld Kubernetes Operator](#voorbeeld-kubernetes-operator)
    - [Uitleg van de Operator](#uitleg-van-de-operator)
  - [Controller uitvoeren](#controller-uitvoeren)
    - [Operator in Kubernetes cluster](#operator-in-kubernetes-cluster)
    - [Controller testen in Kubernetes](#controller-testen-in-kubernetes)
- [Conclusie](#conclusie)
- [Bronnen](#bronnen)

## Inleiding

Kubernetes biedt krachtige ingebouwde resources, zoals Pods, Deployments en Services, deze zijn niet altijd voldoende om specifieke behoeften van applicaties en infrastructuren te ondersteunen. Gelukkig biedt Kubernetes een oplossing: Custom Resources.

Met Kubernetes Custom Resources kun je de functionaliteit van Kubernetes uitbreiden door eigen resource-typen te definiëren en te beheren. Dit opent de deur naar meer flexibiliteit, betere automatisering en diepere integraties met externe systemen. In deze blog duiken we diep in Kubernetes Custom Resources: we leggen uit wat ze zijn, waarom je ze zou gebruiken en hoe je ze implementeert met Custom Resource Definitions (CRD’s) en controllers. Of je nu een ontwikkelaar bent die Kubernetes wil aanpassen aan specifieke use cases of een DevOps-engineer die op zoek is naar efficiëntere workflows, deze blog biedt de kennis die je nodig hebt om aan de slag te gaan met Kubernetes Custom Resources.

## Wat zijn Kubernetes Custom Resources?

Kubernetes bevat een aantal ingebouwde resources, zoals Pods, Deployments en Services, waarmee gebruikers hun applicaties kunnen beheren. Soms zijn deze standaardresources echter niet voldoende. In zulke gevallen bieden Kubernetes Custom Resources een oplossing.

Kubernetes Custom Resources breiden de standaard Kubernetes API uit, waardoor gebruikers hun eigen resource-typen kunnen definiëren en beheren. Dit maakt het mogelijk om de functionaliteit van Kubernetes uit te breiden zonder wijzigingen aan de Kubernetes-broncode.

Een kubernetes custom resource bestaat uit:

- **Custom Resource Definition (CRD)**: Een Kubernetes-resource waarmee gebruikers nieuwe resource-typen kunnen definiëren.
- **Custom Resource (CR)**: Een instantie van een Custom Resource die voldoet aan de gedefinieerde CRD.
- **Controller**: Een proces dat Custom Resources binnen de Kubernetes-cluster beheert en de gewenste status handhaaft.

## Waarom zou je Kubernetes Custom Resources willen gebruiken?

Standaard Kubernetes-resources zijn krachtig, maar niet altijd voldoende voor specifieke use cases. Custom Resources bieden extra flexibiliteit door Kubernetes uit te breiden zonder de broncode aan te passen. Dit maakt het mogelijk om Kubernetes beter af te stemmen op de behoeften van jouw applicatie en infrastructuur.

Enkele redenen om Custom Resources te gebruiken:

- **Domeinspecifieke abstracties**: Definieer eigen resource-typen die beter aansluiten bij je applicatie, zoals een `Device`-resource voor IoT-apparaten of een `Pipeline`-resource voor CI/CD-workflows.
- **Automatisering en self-healing**: Controllers kunnen Custom Resources bewaken en acties ondernemen, zoals het automatisch schalen van database-replicas of het uitvoeren van back-ups.
- **Integratie met externe systemen**: Gebruik Custom Resources om Kubernetes te koppelen aan CI/CD-pipelines, cloudservices of andere externe tools, zonder handmatige configuratie.

Door Custom Resources te gebruiken, kun je Kubernetes aanpassen aan specifieke behoeften en complexiteit voor gebruikers verminderen.

## Definiëren en Gebruiken van Custom Resources

### Custom Resource Definition (CRD)

Om een Custom Resource (CR) te kunnen gebruiken, moet je deze eerst definiëren met een Custom Resource Definition (CRD). Een CRD breidt Kubernetes uit met nieuwe resource-typen, zodat je deze net als standaard Kubernetes-resources kunt beheren.

Hieronder zie je een voorbeeld van een CRD voor een IoT-device:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: devices.stable.example.com
spec:
  group: stable.example.com
  names:
    singular: device
    plural: devices
    kind: device
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
                deviceId:
                  type: string
                type:
                  type: string
                location:
                  type: string
                status:
                  type: integer
                  default: 0
                lastCheckIn:
                  type: integer
                  default: 0
                image:
                  type: string
                replicas:
                  type: integer
  scope: Namespaced
```

#### Uitleg van de CRD

1. **API-versie en type**: De CRD wordt gedefinieerd als een resource van het type `CustomResourceDefinition` en gebruikt de API-versie `apiextensions.k8s.io/v1`.
2. **Metadata**:
      - De naam van de CRD volgt het patroon `<plural>.<group>`, in dit geval `devices.stable.example.com`.
      - De `group` bepaalt onder welke API-groep de resource valt (`stable.example.com`).
3. **Resource-namen**:
     - `singular`: De naam in enkelvoud (`device`).
     - `plural`: De naam in meervoud (`devices`), wat gebruikt wordt in API-verzoeken.
     - `kind`: De naam die Kubernetes gebruikt voor dit resource-type (`Device`).
4. **Versiebeheer**:
      - In het `versions`-blok kun je meerdere versies van je CRD definiëren. In dit voorbeeld is er één versie (`v1`).
      - `served`: `true` betekent dat Kubernetes deze versie aanbiedt via de API.
5. **Schema en eigenschappen**:
    - Binnen de `spec`-sectie definieer je de eigenschappen die een Custom Resource moet bevatten.
    - Voor elke eigenschap geef je het type op (`string`, `integer`, etc.).
    - Je kunt optioneel standaardwaarden instellen, zoals `status: 0` en `lastCheckIn: 0`.

#### CRD toepassen in Kubernetes

Zodra de CRD is gedefinieerd, kun je deze toevoegen aan je Kubernetes-cluster met het volgende commando:

```bash
kubectl apply -f device-crd.yaml
```

Vervang `device-crd.yaml` met de bestandsnaam van jouw CRD-bestand.

### Custom Resource (CR)

Nu je de Custom Resource Definition (CRD) hebt aangemaakt, kun je een Custom Resource (CR) toevoegen. Een CR is een instantie van de resource die je met de CRD hebt gedefinieerd. Hieronder zie je een voorbeeld van een Custom Resource voor een IoT-device:

```yaml
apiVersion: stable.example.com/v1
kind: device
metadata:
  name: device1-instance
spec:
  replicas: 1
  image: "ubuntu:latest"
  deviceId: "1"
  type: "sensor"
  location: "nijmegen"
  status: 0
```

#### Uitleg van de Custom Resource

1. **API-versie en type**:
    - De `apiVersion` volgt het patroon `<group>/<version>`, zoals gedefinieerd in de CRD (`stable.example.com/v1`).
    - De `kind` komt overeen met de naam die je in de CRD hebt opgegeven (`Device`).
2. **Metadata**:
    - De `name`-waarde (`device1-instance`) identificeert deze specifieke instantie binnen Kubernetes.
3. **Specificatie (spec)**:
    - Hier vul je de eigenschappen in die je in de CRD hebt gedefinieerd, zoals `deviceId`, `type`, `location`, en `status`.

#### De Custom Resource deployen

Om de Custom Resource toe te voegen aan je cluster, gebruik je hetzelfde `kubectl apply`-commando als bij de CRD:

```bash
kubectl apply -f device.yaml
```

Vervang `device.yaml` met de bestandsnaam van jouw Custom Resource.

#### Controleren of de Custom Resource is toegevoegd

Je kunt controleren of de Custom Resource correct is aangemaakt met het volgende commando:

```bash
kubectl get devices
```

Let op: vervang `devices` met de meervoudsvorm die je in de CRD hebt gedefinieerd. Als je een `NotFound` error krijgt dan controller of je de CRD hebt gedeployed.

Een voorbeeld van de uitvoer:
`
NAME               AGE
device1-instance   17s
`

Op dit moment is de Custom Resource toegevoegd aan de cluster, maar er gebeurt nog niets mee. Om de resource daadwerkelijk te beheren, hebben we een Controller nodig.

### Controller maken

Als laatste stap moet je een controller maken om daadwerkelijk gebruik te maken van je Custom Resource. Een veelgebruikt patroon hiervoor is het Operator Pattern. Een operator monitort je Custom Resources en voert automatisch acties uit wanneer deze worden aangemaakt, bijgewerkt of verwijderd.

In dit voorbeeld gebruiken we Python met de `kopf`-library, maar je kunt ook een andere taal kiezen wanneer je dat fijner vindt.

#### Voorbeeld Kubernetes Operator

```python
import kopf

@kopf.on.create(group="stable.example.com", version="v1", plural="devices")
def on_create(spec, **kwargs):
    print(f"Device with the following spec has been created: {spec}", flush=True)


@kopf.on.update(group="stable.example.com", version="v1", plural="devices")
def on_create(spec, **kwargs):
    print(f"Device with the following spec has been updated: {spec}", flush=True)


@kopf.on.delete(group="stable.example.com", version="v1", plural="devices")
def on_create(spec, **kwargs):
    print(f"Device with the following spec has been deleted: {spec}", flush=True)
```

#### Uitleg van de Operator

1. **Kopf importeren**:
    - De `kopf`-library maakt het eenvoudig om controllers te schrijven die reageren op Kubernetes-events.
2. Event handlers definiëren
    - `@kopf.on.create(...)`: Wordt uitgevoerd wanneer een device-resource wordt aangemaakt.
    - `@kopf.on.update(...)`: Wordt uitgevoerd wanneer een device-resource wordt gewijzigd.
    - `@kopf.on.delete(...)`: Wordt uitgevoerd wanneer een device-resource wordt verwijderd.
3. Gebruik van parameters
    - `kopf` geeft verschillende parameters door aan de functies. In dit voorbeeld gebruiken we alleen `spec`, maar je kunt ook andere gegevens opvragen zoals `body` of `metadata`.

Op dit moment print de controller alleen een bericht naar de console. In een productieomgeving wil je hier bijvoorbeeld een container starten, een externe service aanroepen of automatische configuraties toepassen.

Naast de `create`, `update` en `delete` events zijn er ook nog andere die je op deze mannier kan implementeren. Kijk hiervoor naar de documentatie van `kopf`.

### Controller uitvoeren

Om de operator lokaal uit te voeren, gebruik je:

```bash
kopf run custom_controller.py
```

Vervang `custom_controller.py` met de bestandsnaam van je script. Nu kun je een resource aanmaken met:

```bash
kubectl apply -f device.yaml
```

Je zou in de logs moeten zien:

```
Device with the following spec has been created: {'deviceId': '1', 'image': 'ubuntu:latest', 'lastCheckIn': 0, 'location': 'nijmegen', 'replicas': 1, 'status': 0, 'type': 'sensor'}
```

#### Operator in Kubernetes cluster

Om de operator te laten draaien binnen Kubernetes, moeten we deze in een Docker-container plaatsen. Dit doen we met de volgende Dockerfile:

```dockerfile
FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY custom_controller.py .

CMD kopf run custom_controller.py
```

Nu kan je de image bouwen doormiddel van:

```bash
docker build -t device-operator .
```

Nu kan je de image pushen naar je container registry, zodat kubernetes er bij kan.

Om de operator in je Kubernetes-cluster te draaien, heb je een Service Account, Cluster Role Binding, en een Deployment nodig. Een voorbeeld is hieronder te zien.

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: operator-account

---

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: operator-account-rolebinding-cluster
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: operator-account
    namespace: default

---

apiVersion: apps/v1
kind: Deployment
metadata:
  name: device-operator-deployment
  labels:
    app: device-operator
spec:
  replicas: 1
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app: device-operator
  template:
    metadata:
      labels:
        app: device-operator
    spec:
      serviceAccountName: operator-account
      containers:
      - name: device-operator
        image: device-operator:latest
        imagePullPolicy: Never
```

Zorg dat je de image aanpast naar datgene wat jij gemaakt hebt. Nu kan je de operator in je cluster plaatsen door:

```bash
kubectl apply -f operator.yaml
```

Vervang `operator.yaml` met de naam van je deployment-bestand.

#### Controller testen in Kubernetes

Nu de operator in je cluster draait, kunnen we testen of deze goed werkt.

1. Verwijder de eerder gemaakt resource:

    ```bash
    kubectl delete devices device1-instance
    ```

    of

    ```bash
    kubectl delete -f device.yaml
    ```

2. Bekijk de logs van de operator:

    ```bash
    kubectl get pods
    ```

    Zoek de naam van de operator-pod (bijvoorbeeld `device-operator-deployment-b9d9fb474-mpmj8`) en voer uit:

    ```bash
    kubectl logs <pod-naam>
    ```

3. Controleer de output
    Je zou iets vegelijkbaars moeten zien:

    ```
    Device with the following spec has been deleted: {'deviceId': '1', 'image': 'ubuntu:latest', 'lastCheckIn': 0, 'location': 'nijmegen', 'replicas': 1, 'status': 0, 'type': 'sensor'}
    ```

## Conclusie

Kubernetes Custom Resources bieden een krachtige manier om de functionaliteit van Kubernetes uit te breiden en aan te passen aan specifieke use cases. Door gebruik te maken van Custom Resource Definitions (CRD’s) en controllers, kunnen ontwikkelaars hun eigen resource-typen definiëren en automatiseren binnen een Kubernetes-cluster. Dit opent de deur naar flexibele, domeinspecifieke oplossingen, betere automatisering en diepere integratie met externe systemen.

In deze blog hebben we de basisprincipes van Kubernetes Custom Resources behandeld, van het definiëren van een CRD tot het implementeren van een controller die automatisch reageert op wijzigingen. Door deze technieken toe te passen, kun je Kubernetes aanpassen aan de behoeften van jouw applicaties en infrastructuur, zonder de broncode van Kubernetes zelf te hoeven wijzigen.

Of je nu een ontwikkelaar bent die specifieke applicatiebehoeften wil ondersteunen, of een DevOps-engineer die streeft naar efficiëntere en beter beheersbare workflows, Kubernetes Custom Resources geven je de tools om op maat gemaakte en schaalbare oplossingen te bouwen. Met deze kennis ben je goed voorbereid om Kubernetes naar een hoger niveau te tillen en je applicaties slimmer en effectiever te beheren.

## Bronnen

- Custom resources. (2024, October 31). Kubernetes. <https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/>
- Muppeda, A. (2024, April 23).  A Hands-On Guide to Kubernetes Custom Resource Definitions (CRDs) with a practical example. Medium. <https://medium.com/@muppedaanvesh/a-hand-on-guide-to-kubernetes-custom-resource-definitions-crds-with-a-practical-example-%EF%B8%8F-84094861e90b>
- Kathayat, A. S. (2024, December 24). Custom Resource Definitions (CRDs) in Kubernetes: Extending the API for custom resources. DEV Community. <https://dev.to/abhay_yt_52a8e72b213be229/custom-resource-definitions-crds-in-kubernetes-extending-the-api-for-custom-resources-e94>
- Controllers. (2024, August 31). Kubernetes. <https://kubernetes.io/docs/concepts/architecture/controller/>
- Kopf: Kubernetes Operators Framework — Kopf documentation. (n.d.). <https://kopf.readthedocs.io/en/stable/>
