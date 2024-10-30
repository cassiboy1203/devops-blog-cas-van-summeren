from kubernetes import client, config, watch

config.load_kube_config()

api_instance = client.CoreV1Api()

def process_event(event):
    obj = event['object']
    event_type = event['type']

    if event_type == 'ADDED':

    elif event_type == 'MODIFIED'

    elif event_type == 'DELETED':

water = watch.Watch()
for event in watcher.stream(api_instance.list_namespaced_custom_object,
                            group="example.com",
                            version="v1",
                            plural="devices"):
    process_event(event)