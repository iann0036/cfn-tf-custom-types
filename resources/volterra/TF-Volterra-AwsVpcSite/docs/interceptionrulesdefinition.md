# TF::Volterra::AwsVpcSite InterceptionRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#disableinterception" title="DisableInterception">DisableInterception</a>" : <i>Boolean</i>,
    "<a href="#enableinterception" title="EnableInterception">EnableInterception</a>" : <i>Boolean</i>,
    "<a href="#domainmatch" title="DomainMatch">DomainMatch</a>" : <i>[ <a href="domainmatchdefinition.md">DomainMatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#disableinterception" title="DisableInterception">DisableInterception</a>: <i>Boolean</i>
<a href="#enableinterception" title="EnableInterception">EnableInterception</a>: <i>Boolean</i>
<a href="#domainmatch" title="DomainMatch">DomainMatch</a>: <i>
      - <a href="domainmatchdefinition.md">DomainMatchDefinition</a></i>
</pre>

## Properties

#### DisableInterception

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableInterception

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainMatch

_Required_: No

_Type_: List of <a href="domainmatchdefinition.md">DomainMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

