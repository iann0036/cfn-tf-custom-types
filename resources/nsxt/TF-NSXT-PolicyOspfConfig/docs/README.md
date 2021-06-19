# TF::NSXT::PolicyOspfConfig

This resource provides a method for the management of OSPF for T0 Gateway on default locale service. A single resource should be specified per T0 Gateway. Edge Cluster is expected to be configured on the Gateway.

This resource is applicable to NSX Policy Manager only.
This resource is supported with NSX 3.1.0 onwards.

~> **NOTE:** NSX does not support deleting OSPF config on gateway, therefore this resource will update NSX object, but never delete it. To undo OSPF configuration, please disable it within the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyOspfConfig",
    "Properties" : {
        "<a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#ecmp" title="Ecmp">Ecmp</a>" : <i>Boolean</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#gatewaypath" title="GatewayPath">GatewayPath</a>" : <i>String</i>,
        "<a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>" : <i>String</i>,
        "<a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>" : <i>[ <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyOspfConfig
Properties:
    <a href="#defaultoriginate" title="DefaultOriginate">DefaultOriginate</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#ecmp" title="Ecmp">Ecmp</a>: <i>Boolean</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#gatewaypath" title="GatewayPath">GatewayPath</a>: <i>String</i>
    <a href="#gracefulrestartmode" title="GracefulRestartMode">GracefulRestartMode</a>: <i>String</i>
    <a href="#summaryaddress" title="SummaryAddress">SummaryAddress</a>: <i>
      - <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### DefaultOriginate

A boolean flag to configure advertisement of default route into OSPF domain. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Description of the resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

Display name of the resource.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ecmp

A boolean flag to enable/disable ECMP. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

A boolean flag to enable/disable OSPF. Default is `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayPath

Policy Path for Tier0 Gateway.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GracefulRestartMode

Graceful Restart Mode, one of `HELPER_ONLY` or `DISABLED`. Defaut is `HELPER_ONLY`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SummaryAddress

_Required_: No

_Type_: List of <a href="summaryaddressdefinition.md">SummaryAddressDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### GatewayId

Returns the <code>GatewayId</code> value.

#### Id

Returns the <code>Id</code> value.

#### LocaleServiceId

Returns the <code>LocaleServiceId</code> value.

#### Path

Returns the <code>Path</code> value.

#### Revision

Returns the <code>Revision</code> value.

