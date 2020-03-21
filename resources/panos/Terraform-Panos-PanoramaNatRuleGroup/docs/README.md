# Terraform::Panos::PanoramaNatRuleGroup

CloudFormation equivalent of panos_panorama_nat_rule_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaNatRuleGroup",
    "Properties" : {
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>" : <i>String</i>,
        "<a href="#positionreference" title="PositionReference">PositionReference</a>" : <i>String</i>,
        "<a href="#rulebase" title="Rulebase">Rulebase</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="rule.md">Rule</a>, ... ]</i>,
        "<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>" : <i>[ <a href="originalpacket.md">OriginalPacket</a>, ... ]</i>,
        "<a href="#target" title="Target">Target</a>" : <i>[ <a href="target.md">Target</a>, ... ]</i>,
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
Type: Terraform::Panos::PanoramaNatRuleGroup
Properties:
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>: <i>String</i>
    <a href="#positionreference" title="PositionReference">PositionReference</a>: <i>String</i>
    <a href="#rulebase" title="Rulebase">Rulebase</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="rule.md">Rule</a></i>
    <a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>: <i>
      - <a href="originalpacket.md">OriginalPacket</a></i>
    <a href="#target" title="Target">Target</a>: <i>
      - <a href="target.md">Target</a></i>
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

#### DeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionKeyword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PositionReference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rulebase

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

#### Target

_Required_: No

_Type_: List of <a href="target.md">Target</a>

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

