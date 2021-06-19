# TF::AVI::Pool ServersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>" : <i>String</i>,
    "<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#externalorchestrationid" title="ExternalOrchestrationId">ExternalOrchestrationId</a>" : <i>String</i>,
    "<a href="#externaluuid" title="ExternalUuid">ExternalUuid</a>" : <i>String</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
    "<a href="#nwref" title="NwRef">NwRef</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#prsthdrval" title="PrstHdrVal">PrstHdrVal</a>" : <i>String</i>,
    "<a href="#ratio" title="Ratio">Ratio</a>" : <i>Double</i>,
    "<a href="#resolveserverbydns" title="ResolveServerByDns">ResolveServerByDns</a>" : <i>Boolean</i>,
    "<a href="#rewritehostheader" title="RewriteHostHeader">RewriteHostHeader</a>" : <i>Boolean</i>,
    "<a href="#servernode" title="ServerNode">ServerNode</a>" : <i>String</i>,
    "<a href="#static" title="Static">Static</a>" : <i>Boolean</i>,
    "<a href="#verifynetwork" title="VerifyNetwork">VerifyNetwork</a>" : <i>Boolean</i>,
    "<a href="#vmref" title="VmRef">VmRef</a>" : <i>String</i>,
    "<a href="#discoverednetworks" title="DiscoveredNetworks">DiscoveredNetworks</a>" : <i>[ <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a>, ... ]</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>[ <a href="ipdefinition.md">IpDefinition</a>, ... ]</i>,
    "<a href="#location" title="Location">Location</a>" : <i>[ <a href="locationdefinition.md">LocationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#autoscalinggroupname" title="AutoscalingGroupName">AutoscalingGroupName</a>: <i>String</i>
<a href="#availabilityzone" title="AvailabilityZone">AvailabilityZone</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#externalorchestrationid" title="ExternalOrchestrationId">ExternalOrchestrationId</a>: <i>String</i>
<a href="#externaluuid" title="ExternalUuid">ExternalUuid</a>: <i>String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
<a href="#nwref" title="NwRef">NwRef</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#prsthdrval" title="PrstHdrVal">PrstHdrVal</a>: <i>String</i>
<a href="#ratio" title="Ratio">Ratio</a>: <i>Double</i>
<a href="#resolveserverbydns" title="ResolveServerByDns">ResolveServerByDns</a>: <i>Boolean</i>
<a href="#rewritehostheader" title="RewriteHostHeader">RewriteHostHeader</a>: <i>Boolean</i>
<a href="#servernode" title="ServerNode">ServerNode</a>: <i>String</i>
<a href="#static" title="Static">Static</a>: <i>Boolean</i>
<a href="#verifynetwork" title="VerifyNetwork">VerifyNetwork</a>: <i>Boolean</i>
<a href="#vmref" title="VmRef">VmRef</a>: <i>String</i>
<a href="#discoverednetworks" title="DiscoveredNetworks">DiscoveredNetworks</a>: <i>
      - <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a></i>
<a href="#ip" title="Ip">Ip</a>: <i>
      - <a href="ipdefinition.md">IpDefinition</a></i>
<a href="#location" title="Location">Location</a>: <i>
      - <a href="locationdefinition.md">LocationDefinition</a></i>
</pre>

## Properties

#### AutoscalingGroupName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailabilityZone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalOrchestrationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NwRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrstHdrVal

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

#### VerifyNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DiscoveredNetworks

_Required_: No

_Type_: List of <a href="discoverednetworksdefinition.md">DiscoveredNetworksDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: No

_Type_: List of <a href="ipdefinition.md">IpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: List of <a href="locationdefinition.md">LocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

