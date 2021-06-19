# TF::Volterra::OriginPool TlsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultsecurity" title="DefaultSecurity">DefaultSecurity</a>" : <i>Boolean</i>,
    "<a href="#lowsecurity" title="LowSecurity">LowSecurity</a>" : <i>Boolean</i>,
    "<a href="#mediumsecurity" title="MediumSecurity">MediumSecurity</a>" : <i>Boolean</i>,
    "<a href="#customsecurity" title="CustomSecurity">CustomSecurity</a>" : <i>[ <a href="customsecuritydefinition.md">CustomSecurityDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultsecurity" title="DefaultSecurity">DefaultSecurity</a>: <i>Boolean</i>
<a href="#lowsecurity" title="LowSecurity">LowSecurity</a>: <i>Boolean</i>
<a href="#mediumsecurity" title="MediumSecurity">MediumSecurity</a>: <i>Boolean</i>
<a href="#customsecurity" title="CustomSecurity">CustomSecurity</a>: <i>
      - <a href="customsecuritydefinition.md">CustomSecurityDefinition</a></i>
</pre>

## Properties

#### DefaultSecurity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LowSecurity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediumSecurity

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSecurity

_Required_: No

_Type_: List of <a href="customsecuritydefinition.md">CustomSecurityDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

