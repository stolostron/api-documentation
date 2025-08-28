# Checkpoint API

Checkpoint is the Schema for the backup of Hive objects.

## Spec Fields

CheckpointSpec defines the metadata around the Hive objects state in the namespace at the time of the last backup.

| Field | Type | Description | Validations |
|:---|---|---|---|
|  **lastBackupChecksum** | `string` | LastBackupChecksum is the checksum of all Hive objects in the namespace at the time of the last backup. | N/A |
|  **lastBackupRef** | `object` | LastBackupRef is a reference to last backup object created | N/A |
| └>&nbsp;&nbsp; **name** | `string` | No description provided. | N/A |
| └>&nbsp;&nbsp; **namespace** | `string` | No description provided. | N/A |
|  **lastBackupTime** | `string` | LastBackupTime is the last time we performed a backup of the namespace | N/A |
## Status Fields

CheckpointStatus defines the observed state of Checkpoint

| Field | Type | Description | Validations |
|:---|---|---|---|
