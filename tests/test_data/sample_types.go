package v1alpha1

import (
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// SampleSpec defines the desired state of Sample
type SampleSpec struct {
	// Name is the name of the sample resource
	// +kubebuilder:validation:Pattern=^[a-z0-9]([-a-z0-9]*[a-z0-9])?$
	Name string `json:"name"`

	// Replicas is the number of replicas to run
	// +kubebuilder:validation:Minimum=1
	// +kubebuilder:validation:Maximum=10
	Replicas int32 `json:"replicas"`

	// Enabled determines if the sample is enabled
	Enabled bool `json:"enabled"`

	// Config contains configuration options
	Config SampleConfig `json:"config"`

	// Items is a list of items
	Items []SampleItem `json:"items"`

	// Embedded metav1.TypeMeta
	metav1.TypeMeta `json:",inline"`

	// Embedded metav1.ObjectMeta
	metav1.ObjectMeta `json:"metadata,omitempty"`

	// EmbeddedStruct is an embedded struct
	EmbeddedStruct `json:"embedded"`
}

// SampleConfig defines configuration options
type SampleConfig struct {
	// Timeout is the timeout in seconds
	// +kubebuilder:validation:Minimum=1
	Timeout int32 `json:"timeout"`

	// Retries is the number of retries
	// +kubebuilder:validation:Minimum=0
	// +kubebuilder:validation:Maximum=5
	Retries int32 `json:"retries"`

	// Settings contains additional settings
	Settings map[string]string `json:"settings"`
}

// SampleItem represents an item in the list
type SampleItem struct {
	// Name is the name of the item
	Name string `json:"name"`

	// Value is the value of the item
	Value int32 `json:"value"`

	// Description with special characters: < > & " '
	Description string `json:"description"`
}

// EmbeddedStruct is an embedded struct
type EmbeddedStruct struct {
	// EmbeddedField is a field in the embedded struct
	EmbeddedField string `json:"embeddedField"`

	// Another embedded field
	AnotherField int32 `json:"anotherField"`
}

// SampleStatus defines the observed state of Sample
type SampleStatus struct {
	// Phase represents the current phase
	// +kubebuilder:validation:Enum=Pending;Running;Completed;Failed
	Phase string `json:"phase"`

	// ReadyReplicas is the number of ready replicas
	ReadyReplicas int32 `json:"readyReplicas"`

	// Conditions represents the latest available observations
	Conditions []SampleCondition `json:"conditions"`

	// Self-referencing field for testing recursion
	Parent *SampleStatus `json:"parent"`
}

// SampleCondition represents a condition
type SampleCondition struct {
	// Type is the type of condition
	Type string `json:"type"`

	// Status is the status of the condition
	Status string `json:"status"`

	// Message is the message describing the condition
	Message string `json:"message"`

	// LastTransitionTime is the last time the condition transitioned
	LastTransitionTime metav1.Time `json:"lastTransitionTime"`
}

// +kubebuilder:object:root=true
// +kubebuilder:subresource:status

// Sample is the Schema for the samples API
type Sample struct {
	metav1.TypeMeta   `json:",inline"`
	metav1.ObjectMeta `json:"metadata,omitempty"`

	Spec   SampleSpec   `json:"spec,omitempty"`
	Status SampleStatus `json:"status,omitempty"`
}

// +kubebuilder:object:root=true

// SampleList contains a list of Sample
type SampleList struct {
	metav1.TypeMeta `json:",inline"`
	metav1.ListMeta `json:"metadata,omitempty"`
	Items           []Sample `json:"items"`
}
