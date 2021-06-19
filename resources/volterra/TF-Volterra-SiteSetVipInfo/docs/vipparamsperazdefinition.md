# TF::Volterra::SiteSetVipInfo VipParamsPerAzDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#azname" title="AzName">AzName</a>" : <i>String</i>,
    "<a href="#insidevip" title="InsideVip">InsideVip</a>" : <i>[ String, ... ]</i>,
    "<a href="#insidevipcname" title="InsideVipCname">InsideVipCname</a>" : <i>String</i>,
    "<a href="#outsidevip" title="OutsideVip">OutsideVip</a>" : <i>[ String, ... ]</i>,
    "<a href="#outsidevipcname" title="OutsideVipCname">OutsideVipCname</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#azname" title="AzName">AzName</a>: <i>String</i>
<a href="#insidevip" title="InsideVip">InsideVip</a>: <i>
      - String</i>
<a href="#insidevipcname" title="InsideVipCname">InsideVipCname</a>: <i>String</i>
<a href="#outsidevip" title="OutsideVip">OutsideVip</a>: <i>
      - String</i>
<a href="#outsidevipcname" title="OutsideVipCname">OutsideVipCname</a>: <i>String</i>
</pre>

## Properties

#### AzName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideVip

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideVipCname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideVip

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideVipCname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

