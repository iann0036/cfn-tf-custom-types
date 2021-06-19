# TF::FortiOS::VpnOcvpn

Configure Overlay Controller VPN settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::VpnOcvpn",
    "Properties" : {
        "<a href="#autodiscovery" title="AutoDiscovery">AutoDiscovery</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#eap" title="Eap">Eap</a>" : <i>String</i>,
        "<a href="#eapusers" title="EapUsers">EapUsers</a>" : <i>String</i>,
        "<a href="#ipallocationblock" title="IpAllocationBlock">IpAllocationBlock</a>" : <i>String</i>,
        "<a href="#multipath" title="Multipath">Multipath</a>" : <i>String</i>,
        "<a href="#nat" title="Nat">Nat</a>" : <i>String</i>,
        "<a href="#pollinterval" title="PollInterval">PollInterval</a>" : <i>Double</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#sdwan" title="Sdwan">Sdwan</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#forticlientaccess" title="ForticlientAccess">ForticlientAccess</a>" : <i>[ <a href="forticlientaccessdefinition.md">ForticlientAccessDefinition</a>, ... ]</i>,
        "<a href="#overlays" title="Overlays">Overlays</a>" : <i>[ <a href="overlaysdefinition.md">OverlaysDefinition</a>, ... ]</i>,
        "<a href="#waninterface" title="WanInterface">WanInterface</a>" : <i>[ <a href="waninterfacedefinition.md">WanInterfaceDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::VpnOcvpn
Properties:
    <a href="#autodiscovery" title="AutoDiscovery">AutoDiscovery</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#eap" title="Eap">Eap</a>: <i>String</i>
    <a href="#eapusers" title="EapUsers">EapUsers</a>: <i>String</i>
    <a href="#ipallocationblock" title="IpAllocationBlock">IpAllocationBlock</a>: <i>String</i>
    <a href="#multipath" title="Multipath">Multipath</a>: <i>String</i>
    <a href="#nat" title="Nat">Nat</a>: <i>String</i>
    <a href="#pollinterval" title="PollInterval">PollInterval</a>: <i>Double</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#sdwan" title="Sdwan">Sdwan</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#forticlientaccess" title="ForticlientAccess">ForticlientAccess</a>: <i>
      - <a href="forticlientaccessdefinition.md">ForticlientAccessDefinition</a></i>
    <a href="#overlays" title="Overlays">Overlays</a>: <i>
      - <a href="overlaysdefinition.md">OverlaysDefinition</a></i>
    <a href="#waninterface" title="WanInterface">WanInterface</a>: <i>
      - <a href="waninterfacedefinition.md">WanInterfaceDefinition</a></i>
</pre>

## Properties

#### AutoDiscovery

Enable/disable auto-discovery shortcuts. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Eap

Enable/disable EAP client authentication. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EapUsers

EAP authentication user group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAllocationBlock

Class B subnet reserved for private IP address assignment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Multipath

Enable/disable multipath redundancy. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nat

Enable/disable inter-overlay source NAT. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PollInterval

Overlay Controller VPN polling interval.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

Set device role. Valid values: `spoke`, `primary-hub`, `secondary-hub`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdwan

Enable/disable adding OCVPN tunnels to SDWAN. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable Overlay Controller cloud assisted VPN. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForticlientAccess

_Required_: No

_Type_: List of <a href="forticlientaccessdefinition.md">ForticlientAccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Overlays

_Required_: No

_Type_: List of <a href="overlaysdefinition.md">OverlaysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WanInterface

_Required_: No

_Type_: List of <a href="waninterfacedefinition.md">WanInterfaceDefinition</a>

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

