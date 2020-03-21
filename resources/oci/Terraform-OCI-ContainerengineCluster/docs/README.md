# Terraform::OCI::ContainerengineCluster

This resource provides the Cluster resource in Oracle Cloud Infrastructure Container Engine service.

Create a new cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OCI::ContainerengineCluster",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vcnid" title="VcnId">VcnId</a>" : <i>String</i>,
        "<a href="#options" title="Options">Options</a>" : <i>[ <a href="options.md">Options</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#addons" title="AddOns">AddOns</a>" : <i>[ <a href="addons.md">AddOns</a>, ... ]</i>,
        "<a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>" : <i>[ <a href="kubernetesnetworkconfig.md">KubernetesNetworkConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OCI::ContainerengineCluster
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vcnid" title="VcnId">VcnId</a>: <i>String</i>
    <a href="#options" title="Options">Options</a>: <i>
      - <a href="options.md">Options</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#addons" title="AddOns">AddOns</a>: <i>
      - <a href="addons.md">AddOns</a></i>
    <a href="#kubernetesnetworkconfig" title="KubernetesNetworkConfig">KubernetesNetworkConfig</a>: <i>
      - <a href="kubernetesnetworkconfig.md">KubernetesNetworkConfig</a></i>
</pre>

## Properties

#### CompartmentId

The OCID of the compartment in which to create the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

The OCID of the KMS key to be used as the master encryption key for Kubernetes secret encryption. When used, `kubernetesVersion` must be at least `v1.13.0`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

(Updatable) The version of Kubernetes to install into the cluster masters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

(Updatable) The name of the cluster. Avoid entering confidential information.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VcnId

The OCID of the virtual cloud network (VCN) in which to create the cluster.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

_Required_: No

_Type_: List of <a href="options.md">Options</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddOns

_Required_: No

_Type_: List of <a href="addons.md">AddOns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesNetworkConfig

_Required_: No

_Type_: List of <a href="kubernetesnetworkconfig.md">KubernetesNetworkConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailableKubernetesUpgrades

Returns the <code>AvailableKubernetesUpgrades</code> value.

#### Endpoints

Returns the <code>Endpoints</code> value.

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### Metadata

Returns the <code>Metadata</code> value.

#### State

Returns the <code>State</code> value.

