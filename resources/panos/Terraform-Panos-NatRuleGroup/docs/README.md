# Terraform::Panos::NatRuleGroup

CloudFormation equivalent of panos_nat_rule_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::NatRuleGroup",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>" : <i>String</i>,
        "<a href="#positionreference" title="PositionReference">PositionReference</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;, ... ]</i>,
        "<a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>" : <i>[ &lt;a href=&#34;originalpacket.md&#34;&gt;OriginalPacket&lt;/a&gt;, ... ]</i>,
        "<a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>" : <i>[ &lt;a href=&#34;translatedpacket.md&#34;&gt;TranslatedPacket&lt;/a&gt;, ... ]</i>,
        "<a href="#destination" title="Destination">Destination</a>" : <i>[ &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;, ... ]</i>,
        "<a href="#dynamic" title="Dynamic">Dynamic</a>" : <i>[ &lt;a href=&#34;dynamic.md&#34;&gt;Dynamic&lt;/a&gt;, ... ]</i>,
        "<a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>" : <i>[ &lt;a href=&#34;dynamictranslation.md&#34;&gt;DynamicTranslation&lt;/a&gt;, ... ]</i>,
        "<a href="#static" title="Static">Static</a>" : <i>[ &lt;a href=&#34;static.md&#34;&gt;Static&lt;/a&gt;, ... ]</i>,
        "<a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>" : <i>[ &lt;a href=&#34;statictranslation.md&#34;&gt;StaticTranslation&lt;/a&gt;, ... ]</i>,
        "<a href="#dynamicip" title="DynamicIp">DynamicIp</a>" : <i>[ &lt;a href=&#34;dynamicip.md&#34;&gt;DynamicIp&lt;/a&gt;, ... ]</i>,
        "<a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>" : <i>[ &lt;a href=&#34;dynamicipandport.md&#34;&gt;DynamicIpAndPort&lt;/a&gt;, ... ]</i>,
        "<a href="#staticip" title="StaticIp">StaticIp</a>" : <i>[ &lt;a href=&#34;staticip.md&#34;&gt;StaticIp&lt;/a&gt;, ... ]</i>,
        "<a href="#fallback" title="Fallback">Fallback</a>" : <i>[ &lt;a href=&#34;fallback.md&#34;&gt;Fallback&lt;/a&gt;, ... ]</i>,
        "<a href="#interfaceaddress" title="InterfaceAddress">InterfaceAddress</a>" : <i>[ &lt;a href=&#34;interfaceaddress.md&#34;&gt;InterfaceAddress&lt;/a&gt;, ... ]</i>,
        "<a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>" : <i>[ &lt;a href=&#34;translatedaddress.md&#34;&gt;TranslatedAddress&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::NatRuleGroup
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#positionkeyword" title="PositionKeyword">PositionKeyword</a>: <i>String</i>
    <a href="#positionreference" title="PositionReference">PositionReference</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;</i>
    <a href="#originalpacket" title="OriginalPacket">OriginalPacket</a>: <i>
      - &lt;a href=&#34;originalpacket.md&#34;&gt;OriginalPacket&lt;/a&gt;</i>
    <a href="#translatedpacket" title="TranslatedPacket">TranslatedPacket</a>: <i>
      - &lt;a href=&#34;translatedpacket.md&#34;&gt;TranslatedPacket&lt;/a&gt;</i>
    <a href="#destination" title="Destination">Destination</a>: <i>
      - &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;</i>
    <a href="#source" title="Source">Source</a>: <i>
      - &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;</i>
    <a href="#dynamic" title="Dynamic">Dynamic</a>: <i>
      - &lt;a href=&#34;dynamic.md&#34;&gt;Dynamic&lt;/a&gt;</i>
    <a href="#dynamictranslation" title="DynamicTranslation">DynamicTranslation</a>: <i>
      - &lt;a href=&#34;dynamictranslation.md&#34;&gt;DynamicTranslation&lt;/a&gt;</i>
    <a href="#static" title="Static">Static</a>: <i>
      - &lt;a href=&#34;static.md&#34;&gt;Static&lt;/a&gt;</i>
    <a href="#statictranslation" title="StaticTranslation">StaticTranslation</a>: <i>
      - &lt;a href=&#34;statictranslation.md&#34;&gt;StaticTranslation&lt;/a&gt;</i>
    <a href="#dynamicip" title="DynamicIp">DynamicIp</a>: <i>
      - &lt;a href=&#34;dynamicip.md&#34;&gt;DynamicIp&lt;/a&gt;</i>
    <a href="#dynamicipandport" title="DynamicIpAndPort">DynamicIpAndPort</a>: <i>
      - &lt;a href=&#34;dynamicipandport.md&#34;&gt;DynamicIpAndPort&lt;/a&gt;</i>
    <a href="#staticip" title="StaticIp">StaticIp</a>: <i>
      - &lt;a href=&#34;staticip.md&#34;&gt;StaticIp&lt;/a&gt;</i>
    <a href="#fallback" title="Fallback">Fallback</a>: <i>
      - &lt;a href=&#34;fallback.md&#34;&gt;Fallback&lt;/a&gt;</i>
    <a href="#interfaceaddress" title="InterfaceAddress">InterfaceAddress</a>: <i>
      - &lt;a href=&#34;interfaceaddress.md&#34;&gt;InterfaceAddress&lt;/a&gt;</i>
    <a href="#translatedaddress" title="TranslatedAddress">TranslatedAddress</a>: <i>
      - &lt;a href=&#34;translatedaddress.md&#34;&gt;TranslatedAddress&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

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

#### Vsys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of &lt;a href=&#34;rule.md&#34;&gt;Rule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginalPacket

_Required_: No

_Type_: List of &lt;a href=&#34;originalpacket.md&#34;&gt;OriginalPacket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedPacket

_Required_: No

_Type_: List of &lt;a href=&#34;translatedpacket.md&#34;&gt;TranslatedPacket&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of &lt;a href=&#34;destination.md&#34;&gt;Destination&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dynamic

_Required_: No

_Type_: List of &lt;a href=&#34;dynamic.md&#34;&gt;Dynamic&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicTranslation

_Required_: No

_Type_: List of &lt;a href=&#34;dynamictranslation.md&#34;&gt;DynamicTranslation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Static

_Required_: No

_Type_: List of &lt;a href=&#34;static.md&#34;&gt;Static&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticTranslation

_Required_: No

_Type_: List of &lt;a href=&#34;statictranslation.md&#34;&gt;StaticTranslation&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicIp

_Required_: No

_Type_: List of &lt;a href=&#34;dynamicip.md&#34;&gt;DynamicIp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicIpAndPort

_Required_: No

_Type_: List of &lt;a href=&#34;dynamicipandport.md&#34;&gt;DynamicIpAndPort&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIp

_Required_: No

_Type_: List of &lt;a href=&#34;staticip.md&#34;&gt;StaticIp&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fallback

_Required_: No

_Type_: List of &lt;a href=&#34;fallback.md&#34;&gt;Fallback&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceAddress

_Required_: No

_Type_: List of &lt;a href=&#34;interfaceaddress.md&#34;&gt;InterfaceAddress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TranslatedAddress

_Required_: No

_Type_: List of &lt;a href=&#34;translatedaddress.md&#34;&gt;TranslatedAddress&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

