# TF::Gridscale::Server NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bootdevice" title="Bootdevice">Bootdevice</a>" : <i>Boolean</i>,
    "<a href="#firewalltemplateuuid" title="FirewallTemplateUuid">FirewallTemplateUuid</a>" : <i>String</i>,
    "<a href="#objectuuid" title="ObjectUuid">ObjectUuid</a>" : <i>String</i>,
    "<a href="#ordering" title="Ordering">Ordering</a>" : <i>Double</i>,
    "<a href="#rulesv4in" title="RulesV4In">RulesV4In</a>" : <i>[ <a href="rulesv4indefinition.md">RulesV4InDefinition</a>, ... ]</i>,
    "<a href="#rulesv4out" title="RulesV4Out">RulesV4Out</a>" : <i>[ <a href="rulesv4outdefinition.md">RulesV4OutDefinition</a>, ... ]</i>,
    "<a href="#rulesv6in" title="RulesV6In">RulesV6In</a>" : <i>[ <a href="rulesv6indefinition.md">RulesV6InDefinition</a>, ... ]</i>,
    "<a href="#rulesv6out" title="RulesV6Out">RulesV6Out</a>" : <i>[ <a href="rulesv6outdefinition.md">RulesV6OutDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#bootdevice" title="Bootdevice">Bootdevice</a>: <i>Boolean</i>
<a href="#firewalltemplateuuid" title="FirewallTemplateUuid">FirewallTemplateUuid</a>: <i>String</i>
<a href="#objectuuid" title="ObjectUuid">ObjectUuid</a>: <i>String</i>
<a href="#ordering" title="Ordering">Ordering</a>: <i>Double</i>
<a href="#rulesv4in" title="RulesV4In">RulesV4In</a>: <i>
      - <a href="rulesv4indefinition.md">RulesV4InDefinition</a></i>
<a href="#rulesv4out" title="RulesV4Out">RulesV4Out</a>: <i>
      - <a href="rulesv4outdefinition.md">RulesV4OutDefinition</a></i>
<a href="#rulesv6in" title="RulesV6In">RulesV6In</a>: <i>
      - <a href="rulesv6indefinition.md">RulesV6InDefinition</a></i>
<a href="#rulesv6out" title="RulesV6Out">RulesV6Out</a>: <i>
      - <a href="rulesv6outdefinition.md">RulesV6OutDefinition</a></i>
</pre>

## Properties

#### Bootdevice

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallTemplateUuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectUuid

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ordering

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV4In

_Required_: No

_Type_: List of <a href="rulesv4indefinition.md">RulesV4InDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV4Out

_Required_: No

_Type_: List of <a href="rulesv4outdefinition.md">RulesV4OutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV6In

_Required_: No

_Type_: List of <a href="rulesv6indefinition.md">RulesV6InDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RulesV6Out

_Required_: No

_Type_: List of <a href="rulesv6outdefinition.md">RulesV6OutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

