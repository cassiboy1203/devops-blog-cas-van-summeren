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