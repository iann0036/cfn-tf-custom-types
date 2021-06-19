# TF::Volterra::FastAcl SelectedTenantVipDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaulttenantvip" title="DefaultTenantVip">DefaultTenantVip</a>" : <i>Boolean</i>,
    "<a href="#publiciprefs" title="PublicIpRefs">PublicIpRefs</a>" : <i>[ <a href="publiciprefsdefinition.md">PublicIpRefsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaulttenantvip" title="DefaultTenantVip">DefaultTenantVip</a>: <i>Boolean</i>
<a href="#publiciprefs" title="PublicIpRefs">PublicIpRefs</a>: <i>
      - <a href="publiciprefsdefinition.md">PublicIpRefsDefinition</a></i>
</pre>

## Properties

#### DefaultTenantVip

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpRefs

_Required_: No

_Type_: List of <a href="publiciprefsdefinition.md">PublicIpRefsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

