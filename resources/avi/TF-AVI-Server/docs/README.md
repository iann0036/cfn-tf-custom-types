# TF::AVI::Server

The Server resource allows the creation and management of Avi Server

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Server",
    "Properties" : {
        "<a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>" : <i>String</i>,
        "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#externalorchestrationid" title="ExternalOrchestrationId">ExternalOrchestrationId</a>" : <i>String</i>,
        "<a href="#externaluuid" title="ExternalUuid">ExternalUuid</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
        "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
        "<a href="#nwref" title="NwRef">NwRef</a>" : <i>String</i>,
        "<a href="#poolref" title="PoolRef">PoolRef</a>" : <i>String</i>,
        "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
        "<a href="#prsthdrval" title="PrstHdrVal">PrstHdrVal</a>" : <i>String</i>,
        "<a href="#ratio" title="Ratio">Ratio</a>" : <i>Double</i>,
        "<a href="#resolveserverbydns" title="ResolveServerByDns">ResolveServerByDns</a>" : <i>Boolean</i>,
        "<a href="#rewritehostheader" title="RewriteHostHeader">RewriteHostHeader</a>" : <i>Boolean</i>,
        "<a href="#servernode" title="ServerNode">ServerNode</a>" : <i>String</i>,
        "<a href="#static" title="Static">Static</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#verifynetwork" title="VerifyNetwork">VerifyNetwork</a>" : <i>Boolean</i>,
        "<a href="#vmref" title="VmRef">VmRef</a>" : <i>String</i>,
        "<a href="#discoverednetworks" title="DiscoveredNetworks">DiscoveredNetworks</a>" : <i>[ <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a>, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>[ <a href="locationdefinition.md">LocationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Server
Properties:
    <a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>: <i>String</i>
    <a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#externalorchestrationid" title="ExternalOrchestrationId">ExternalOrchestrationId</a>: <i>String</i>
    <a href="#externaluuid" title="ExternalUuid">ExternalUuid</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#ip" title="Ip">Ip</a>: <i>String</i>
    <a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
    <a href="#nwref" title="NwRef">NwRef</a>: <i>String</i>
    <a href="#poolref" title="PoolRef">PoolRef</a>: <i>String</i>
    <a href="#port" title="Port">Port</a>: <i>Double</i>
    <a href="#prsthdrval" title="PrstHdrVal">PrstHdrVal</a>: <i>String</i>
    <a href="#ratio" title="Ratio">Ratio</a>: <i>Double</i>
    <a href="#resolveserverbydns" title="ResolveServerByDns">ResolveServerByDns</a>: <i>Boolean</i>
    <a href="#rewritehostheader" title="RewriteHostHeader">RewriteHostHeader</a>: <i>Boolean</i>
    <a href="#servernode" title="ServerNode">ServerNode</a>: <i>String</i>
    <a href="#static" title="Static">Static</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#verifynetwork" title="VerifyNetwork">VerifyNetwork</a>: <i>Boolean</i>
    <a href="#vmref" title="VmRef">VmRef</a>: <i>String</i>
    <a href="#discoverednetworks" title="DiscoveredNetworks">DiscoveredNetworks</a>: <i>
      - <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a></i>
    <a href="#location" title="Location">Location</a>: <i>
      - <a href="locationdefinition.md">LocationDefinition</a></i>
</pre>

## Properties

#### AutoscalingGroupName

argument_description.
* `description` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_orchestration_id` - (Optional ) argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

argument_description.
* `enabled` - (Optional ) argument_description.
* `external_orchestration_id` - (Optional ) argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

argument_description.
* `external_orchestration_id` - (Optional ) argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalOrchestrationId

argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalUuid

argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

argument_description.
* `port` - (Optional ) argument_description.
* `type` - (Optional ) argument_description.
* `autoscaling_group_name` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_orchestration_id` - (Optional ) argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NwRef

argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolRef

argument_description.
* `ip` - (Required) argument_description.
* `port` - (Optional ) argument_description.
* `type` - (Optional ) argument_description.
* `autoscaling_group_name` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_orchestration_id` - (Optional ) argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

argument_description.
* `type` - (Optional ) argument_description.
* `autoscaling_group_name` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_orchestration_id` - (Optional ) argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrstHdrVal

argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ratio

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveServerByDns

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RewriteHostHeader

argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerNode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

argument_description.
* `autoscaling_group_name` - (Optional ) argument_description.
* `description` - (Optional ) argument_description.
* `enabled` - (Optional ) argument_description.
* `external_orchestration_id` - (Optional ) argument_description.
* `external_uuid` - (Optional ) argument_description.
* `hostname` - (Optional ) argument_description.
* `location` - (Optional ) argument_description.
* `nw_ref` - (Optional ) argument_description.
* `prst_hdr_val` - (Optional ) argument_description.
* `rewrite_host_header` - (Optional ) argument_description.
* `vm_ref` - (Optional ) argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifyNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmRef

argument_description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveredNetworks

_Required_: No

_Type_: List of <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: List of <a href="locationdefinition.md">LocationDefinition</a>

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

