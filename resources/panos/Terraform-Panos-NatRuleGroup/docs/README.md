# Terraform::Panos::NatRuleGroup

This resource allows you to add/update/delete a group of NAT rules.

This resource manages clusters of NAT rules in a single vsys,
enforcing both the contents of individual rules as well as their
ordering.  Rules are defined in a `rule` config block.

Although you cannot modify non-group NAT rules with this
resource, the `position_keyword` and `position_reference` parameters allow you
to reference some other NAT rule that already exists, using it as
a means to ensure some rough placement within the ruleset as a whole.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::NatRuleGroup",
    "Properties" : {
        "<a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>" : <i>String</i>,
        "<a href="#positionreference" title="PositionReference">PositionReference</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>" : <i>[ <a href="originalpacket.md">OriginalPacket</a>, ... ]</i>,
        "<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>" : <i>[ <a href="translatedpacket.md">TranslatedPacket</a>, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="destination.md">Destination</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="source.md">Source</a>, ... ]</i>,
        "<a href="#dynamic" title="Dynamic">Dynamic</a>" : <i>[ <a href="dynamic.md">Dynamic</a>, ... ]</i>,
        "<a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>" : <i>[ <a href="dynamictranslation.md">DynamicTranslation</a>, ... ]</i>,
        "<a href="#static" title="Static">Static</a>" : <i>[ <a href="static.md">Static</a>, ... ]</i>,
        "<a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>" : <i>[ <a href="statictranslation.md">StaticTranslation</a>, ... ]</i>,
        "<a href="#dynamicip" title="DynamicIp">DynamicIp</a>" : <i>[ <a href="dynamicip.md">DynamicIp</a>, ... ]</i>,
        "<a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>" : <i>[ <a href="dynamicipandport.md">DynamicIpAndPort</a>, ... ]</i>,
        "<a href="#staticip" title="StaticIp">StaticIp</a>" : <i>[ <a href="staticip.md">StaticIp</a>, ... ]</i>,
        "<a href="#fallback" title="Fallback">Fallback</a>" : <i>[ <a href="fallback.md">Fallback</a>, ... ]</i>,
        "<a href="#interfaceaddress" title="InterfaceAddress">InterfaceAddress</a>" : <i>[ <a href="interfaceaddress.md">InterfaceAddress</a>, ... ]</i>,
        "<a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>" : <i>[ <a href="translatedaddress.md">TranslatedAddress</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::NatRuleGroup
Properties:
    <a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>: <i>String</i>
    <a href="#positionreference" title="PositionReference">PositionReference</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>: <i>
      - <a href="originalpacket.md">OriginalPacket</a></i>
    <a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>: <i>
      - <a href="translatedpacket.md">TranslatedPacket</a></i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="destination.md">Destination</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="source.md">Source</a></i>
    <a href="#dynamic" title="Dynamic">Dynamic</a>: <i>
      - <a href="dynamic.md">Dynamic</a></i>
    <a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>: <i>
      - <a href="dynamictranslation.md">DynamicTranslation</a></i>
    <a href="#static" title="Static">Static</a>: <i>
      - <a href="static.md">Static</a></i>
    <a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>: <i>
      - <a href="statictranslation.md">StaticTranslation</a></i>
    <a href="#dynamicip" title="DynamicIp">DynamicIp</a>: <i>
      - <a href="dynamicip.md">DynamicIp</a></i>
    <a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>: <i>
      - <a href="dynamicipandport.md">DynamicIpAndPort</a></i>
    <a href="#staticip" title="StaticIp">StaticIp</a>: <i>
      - <a href="staticip.md">StaticIp</a></i>
    <a href="#fallback" title="Fallback">Fallback</a>: <i>
      - <a href="fallback.md">Fallback</a></i>
    <a href="#interfaceaddress" title="InterfaceAddress">InterfaceAddress</a>: <i>
      - <a href="interfaceaddress.md">InterfaceAddress</a></i>
    <a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>: <i>
      - <a href="translatedaddress.md">TranslatedAddress</a></i>
</pre>

## Properties

#### PositionKeyword

A positioning keyword for this group.  This
can be `before`, `directly before`, `after`, `directly after`, `top`,
`bottom`, or left empty (the default) to have no particular placement.  This
param works in combination with the `position_reference` param.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionReference

Required if `position_keyword` is one of the
"above" or "below" variants, this is the name of a non-group rule to use
as a reference to place this group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys to put the NAT rule group into (default:
`vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalPacket

_Required_: No

_Type_: List of <a href="originalpacket.md">OriginalPacket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPacket

_Required_: No

_Type_: List of <a href="translatedpacket.md">TranslatedPacket</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamic

_Required_: No

_Type_: List of <a href="dynamic.md">Dynamic</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicTranslation

_Required_: No

_Type_: List of <a href="dynamictranslation.md">DynamicTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

_Required_: No

_Type_: List of <a href="static.md">Static</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticTranslation

_Required_: No

_Type_: List of <a href="statictranslation.md">StaticTranslation</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicIp

_Required_: No

_Type_: List of <a href="dynamicip.md">DynamicIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicIpAndPort

_Required_: No

_Type_: List of <a href="dynamicipandport.md">DynamicIpAndPort</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIp

_Required_: No

_Type_: List of <a href="staticip.md">StaticIp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fallback

_Required_: No

_Type_: List of <a href="fallback.md">Fallback</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceAddress

_Required_: No

_Type_: List of <a href="interfaceaddress.md">InterfaceAddress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedAddress

_Required_: No

_Type_: List of <a href="translatedaddress.md">TranslatedAddress</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

