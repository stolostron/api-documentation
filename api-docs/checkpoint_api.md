# Checkpoint API

CheckpointStatus defines the observed state of Checkpoint

## Spec Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **lastBackupChecksum** | `string` | LastBackupChecksum is the checksum of all Hive objects in the namespace at the time of the last backup. | N/A |
|  **lastBackupRef** | `object` | LastBackupRef is a reference to last backup object created | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | No description provided. | N/A |
|  **lastBackupTime** | `string` | LastBackupTime is the last time we performed a backup of the namespace | N/A |
## Status Fields

| Field | Type | Description | Validations |
|:---|---|---|---|
