# TF::FortiOS::SwitchcontrollerLldpprofile

Configure FortiSwitch LLDP profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SwitchcontrollerLldpprofile",
    "Properties" : {
        "<a href="#autoisl" title="AutoIsl">AutoIsl</a>" : <i>String</i>,
        "<a href="#autoislhellotimer" title="AutoIslHelloTimer">AutoIslHelloTimer</a>" : <i>Double</i>,
        "<a href="#autoislportgroup" title="AutoIslPortGroup">AutoIslPortGroup</a>" : <i>Double</i>,
        "<a href="#autoislreceivetimeout" title="AutoIslReceiveTimeout">AutoIslReceiveTimeout</a>" : <i>Double</i>,
        "<a href="#automclagicl" title="AutoMclagIcl">AutoMclagIcl</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#medtlvs" title="MedTlvs">MedTlvs</a>" : <i>String</i>,
        "<a href="#n8021tlvs" title="N8021Tlvs">N8021Tlvs</a>" : <i>String</i>,
        "<a href="#n8023tlvs" title="N8023Tlvs">N8023Tlvs</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#customtlvs" title="CustomTlvs">CustomTlvs</a>" : <i>[ <a href="customtlvsdefinition.md">CustomTlvsDefinition</a>, ... ]</i>,
        "<a href="#medlocationservice" title="MedLocationService">MedLocationService</a>" : <i>[ <a href="medlocationservicedefinition.md">MedLocationServiceDefinition</a>, ... ]</i>,
        "<a href="#mednetworkpolicy" title="MedNetworkPolicy">MedNetworkPolicy</a>" : <i>[ <a href="mednetworkpolicydefinition.md">MedNetworkPolicyDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SwitchcontrollerLldpprofile
Properties:
    <a href="#autoisl" title="AutoIsl">AutoIsl</a>: <i>String</i>
    <a href="#autoislhellotimer" title="AutoIslHelloTimer">AutoIslHelloTimer</a>: <i>Double</i>
    <a href="#autoislportgroup" title="AutoIslPortGroup">AutoIslPortGroup</a>: <i>Double</i>
    <a href="#autoislreceivetimeout" title="AutoIslReceiveTimeout">AutoIslReceiveTimeout</a>: <i>Double</i>
    <a href="#automclagicl" title="AutoMclagIcl">AutoMclagIcl</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#medtlvs" title="MedTlvs">MedTlvs</a>: <i>String</i>
    <a href="#n8021tlvs" title="N8021Tlvs">N8021Tlvs</a>: <i>String</i>
    <a href="#n8023tlvs" title="N8023Tlvs">N8023Tlvs</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#customtlvs" title="CustomTlvs">CustomTlvs</a>: <i>
      - <a href="customtlvsdefinition.md">CustomTlvsDefinition</a></i>
    <a href="#medlocationservice" title="MedLocationService">MedLocationService</a>: <i>
      - <a href="medlocationservicedefinition.md">MedLocationServiceDefinition</a></i>
    <a href="#mednetworkpolicy" title="MedNetworkPolicy">MedNetworkPolicy</a>: <i>
      - <a href="mednetworkpolicydefinition.md">MedNetworkPolicyDefinition</a></i>
</pre>

## Properties

#### AutoIsl

Enable/disable auto inter-switch LAG. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoIslHelloTimer

Auto inter-switch LAG hello timer duration (1 - 30 sec, default = 3).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoIslPortGroup

Auto inter-switch LAG port group ID (0 - 9).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoIslReceiveTimeout

Auto inter-switch LAG timeout if no response is received (3 - 90 sec, default = 9).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoMclagIcl

Enable/disable MCLAG inter chassis link. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MedTlvs

Transmitted LLDP-MED TLVs (type-length-value descriptions): inventory management TLV and/or network policy TLV.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### N8021Tlvs

Transmitted IEEE 802.1 TLVs. Valid values: `port-vlan-id`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### N8023Tlvs

Transmitted IEEE 802.3 TLVs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomTlvs

_Required_: No

_Type_: List of <a href="customtlvsdefinition.md">CustomTlvsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MedLocationService

_Required_: No

_Type_: List of <a href="medlocationservicedefinition.md">MedLocationServiceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MedNetworkPolicy

_Required_: No

_Type_: List of <a href="mednetworkpolicydefinition.md">MedNetworkPolicyDefinition</a>

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

