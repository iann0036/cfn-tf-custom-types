# TF::OCI::DatabaseVmClusterNetwork

This resource provides the Vm Cluster Network resource in Oracle Cloud Infrastructure Database service.

Creates the VM cluster network. Applies to Exadata Cloud@Customer instances only.
To create a cloud VM cluster in an Exadata Cloud Service instance, use the [CreateCloudVmCluster ](https://docs.cloud.oracle.com/iaas/api/#/en/database/latest/CloudVmCluster/CreateCloudVmCluster) operation.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::DatabaseVmClusterNetwork",
    "Properties" : {
        "<a href="#compartmentid" title="CompartmentId">CompartmentId</a>" : <i>String</i>,
        "<a href="#definedtags" title="DefinedTags">DefinedTags</a>" : <i>[ <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>, ... ]</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#dns" title="Dns">Dns</a>" : <i>[ String, ... ]</i>,
        "<a href="#exadatainfrastructureid" title="ExadataInfrastructureId">ExadataInfrastructureId</a>" : <i>String</i>,
        "<a href="#freeformtags" title="FreeformTags">FreeformTags</a>" : <i>[ <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>, ... ]</i>,
        "<a href="#ntp" title="Ntp">Ntp</a>" : <i>[ String, ... ]</i>,
        "<a href="#validatevmclusternetwork" title="ValidateVmClusterNetwork">ValidateVmClusterNetwork</a>" : <i>Boolean</i>,
        "<a href="#scans" title="Scans">Scans</a>" : <i>[ <a href="scansdefinition.md">ScansDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>,
        "<a href="#vmnetworks" title="VmNetworks">VmNetworks</a>" : <i>[ <a href="vmnetworksdefinition.md">VmNetworksDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::DatabaseVmClusterNetwork
Properties:
    <a href="#compartmentid" title="CompartmentId">CompartmentId</a>: <i>String</i>
    <a href="#definedtags" title="DefinedTags">DefinedTags</a>: <i>
      - <a href="definedtagsdefinition.md">DefinedTagsDefinition</a></i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#dns" title="Dns">Dns</a>: <i>
      - String</i>
    <a href="#exadatainfrastructureid" title="ExadataInfrastructureId">ExadataInfrastructureId</a>: <i>String</i>
    <a href="#freeformtags" title="FreeformTags">FreeformTags</a>: <i>
      - <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a></i>
    <a href="#ntp" title="Ntp">Ntp</a>: <i>
      - String</i>
    <a href="#validatevmclusternetwork" title="ValidateVmClusterNetwork">ValidateVmClusterNetwork</a>: <i>Boolean</i>
    <a href="#scans" title="Scans">Scans</a>: <i>
      - <a href="scansdefinition.md">ScansDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    <a href="#vmnetworks" title="VmNetworks">VmNetworks</a>: <i>
      - <a href="vmnetworksdefinition.md">VmNetworksDefinition</a></i>
</pre>

## Properties

#### CompartmentId

The [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefinedTags

(Updatable) Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).

_Required_: No

_Type_: List of <a href="definedtagsdefinition.md">DefinedTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The user-friendly name for the Exadata Cloud@Customer VM cluster network. The name does not need to be unique.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns

(Updatable) The list of DNS server IP addresses. Maximum of 3 allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExadataInfrastructureId

The Exadata infrastructure [OCID](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FreeformTags

(Updatable) Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see [Resource Tags](https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).  Example: `{"Department": "Finance"}`.

_Required_: No

_Type_: List of <a href="freeformtagsdefinition.md">FreeformTagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ntp

(Updatable) The list of NTP server IP addresses. Maximum of 3 allowed.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidateVmClusterNetwork

(Updatable) A boolean flag indicating whether or not to validate VM cluster network after creation. Updates are not allowed on validated exadata VM cluster network. Note: Deleting a [VM Cluster](https://registry.terraform.io/providers/hashicorp/oci/latest/docs/resources/database_vm_cluster) resource puts a VM Cluster Network in `REQUIRES_VALIDATION` state. This results in `After applying this step and refreshing, the plan was not empty` error and users should apply the terraform configuration again to validate the VM Cluster Network.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scans

_Required_: No

_Type_: List of <a href="scansdefinition.md">ScansDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmNetworks

_Required_: No

_Type_: List of <a href="vmnetworksdefinition.md">VmNetworksDefinition</a>

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

#### LifecycleDetails

Returns the <code>LifecycleDetails</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

#### VmClusterId

Returns the <code>VmClusterId</code> value.

