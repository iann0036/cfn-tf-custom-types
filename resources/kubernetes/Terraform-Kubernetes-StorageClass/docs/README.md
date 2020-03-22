# Terraform::Kubernetes::StorageClass

Storage class is the foundation of dynamic provisioning, allowing cluster administrators to define abstractions for the underlying storage platform.

Read more at https://kubernetes.io/blog/2017/03/dynamic-provisioning-and-storage-classes-kubernetes/

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Kubernetes::StorageClass",
    "Properties" : {
        "<a href="#allowvolumeexpansion" title="AllowVolumeExpansion">AllowVolumeExpansion</a>" : <i>Boolean</i>,
        "<a href="#mountoptions" title="MountOptions">MountOptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#reclaimpolicy" title="ReclaimPolicy">ReclaimPolicy</a>" : <i>String</i>,
        "<a href="#storageprovisioner" title="StorageProvisioner">StorageProvisioner</a>" : <i>String</i>,
        "<a href="#volumebindingmode" title="VolumeBindingMode">VolumeBindingMode</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Kubernetes::StorageClass
Properties:
    <a href="#allowvolumeexpansion" title="AllowVolumeExpansion">AllowVolumeExpansion</a>: <i>Boolean</i>
    <a href="#mountoptions" title="MountOptions">MountOptions</a>: <i>
      - String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#reclaimpolicy" title="ReclaimPolicy">ReclaimPolicy</a>: <i>String</i>
    <a href="#storageprovisioner" title="StorageProvisioner">StorageProvisioner</a>: <i>String</i>
    <a href="#volumebindingmode" title="VolumeBindingMode">VolumeBindingMode</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
</pre>

## Properties

#### AllowVolumeExpansion

Indicates whether the storage class allow volume expand, default true.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountOptions

Persistent Volumes that are dynamically created by a storage class will have the mount options specified.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

The parameters for the provisioner that should create volumes of this storage class.
Read more about [available parameters](https://kubernetes.io/docs/concepts/storage/storage-classes/#parameters).

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReclaimPolicy

Indicates the reclaim policy to use.  If no reclaimPolicy is specified when a StorageClass object is created, it will default to Delete.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageProvisioner

Indicates the type of the provisioner.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeBindingMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

