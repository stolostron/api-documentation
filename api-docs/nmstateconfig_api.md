# NMStateConfig API

Description not found in CRD.

## Spec Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **config** | `object` | yaml that can be processed by nmstate, using custom marshaling/unmarshaling that will allow to populate nmstate config as plain yaml. | N/A |
|  **interfaces** | `array` | Interfaces is an array of interface objects containing the name and MAC address for interfaces that are referenced in the raw nmstate config YAML. Interfaces listed here will be automatically renamed in the nmstate config YAML to match the real device name that is observed to have the corresponding MAC address. At least one interface must be listed so that it can be used to identify the correct host, which is done by matching any MAC address in this list to any MAC address observed on the host. | N/A |
| └>&nbsp;&nbsp; **macAddress** | `string` | mac address present on the host. | `Pattern=^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$` |
| └>&nbsp;&nbsp; **name** | `string` | nic name used in the yaml, which relates 1:1 to the mac address. Name in REST API: logicalNICName | N/A |
## Status Fields

No description available.

| Field | Type | Description | Validations |
|:---|---|---|---|
