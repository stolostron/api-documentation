# MachinePoolNameLease API

MachinePoolNameLease is the Schema for the MachinePoolNameLeases API. This resource is mostly empty
as we're primarily relying on the name to determine if a lease is available.
Note that not all cloud providers require the use of a lease for naming, at present this
is only required for GCP where we're extremely restricted on name lengths.

## Spec Fields

MachinePoolNameLeaseSpec is a minimal resource for obtaining unique machine pool names of a limited length.

| Field | Type | Description | Validations |
|:---|---|---|---|
## Status Fields

MachinePoolNameLeaseStatus defines the observed state of MachinePoolNameLease.

| Field | Type | Description | Validations |
|:---|---|---|---|
