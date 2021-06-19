# TF::Volterra::FastAcl SiteAclDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allservices" title="AllServices">AllServices</a>" : <i>Boolean</i>,
    "<a href="#insidenetwork" title="InsideNetwork">InsideNetwork</a>" : <i>Boolean</i>,
    "<a href="#interfaceservices" title="InterfaceServices">InterfaceServices</a>" : <i>Boolean</i>,
    "<a href="#outsidenetwork" title="OutsideNetwork">OutsideNetwork</a>" : <i>Boolean</i>,
    "<a href="#vipservices" title="VipServices">VipServices</a>" : <i>Boolean</i>,
    "<a href="#fastaclrules" title="FastAclRules">FastAclRules</a>" : <i>[ <a href="fastaclrulesdefinition.md">FastAclRulesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allservices" title="AllServices">AllServices</a>: <i>Boolean</i>
<a href="#insidenetwork" title="InsideNetwork">InsideNetwork</a>: <i>Boolean</i>
<a href="#interfaceservices" title="InterfaceServices">InterfaceServices</a>: <i>Boolean</i>
<a href="#outsidenetwork" title="OutsideNetwork">OutsideNetwork</a>: <i>Boolean</i>
<a href="#vipservices" title="VipServices">VipServices</a>: <i>Boolean</i>
<a href="#fastaclrules" title="FastAclRules">FastAclRules</a>: <i>
      - <a href="fastaclrulesdefinition.md">FastAclRulesDefinition</a></i>
</pre>

## Properties

#### AllServices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InsideNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceServices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutsideNetwork

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipServices

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FastAclRules

_Required_: No

_Type_: List of <a href="fastaclrulesdefinition.md">FastAclRulesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

