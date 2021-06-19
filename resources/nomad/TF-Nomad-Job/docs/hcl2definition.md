# TF::Nomad::Job Hcl2Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowfs" title="AllowFs">AllowFs</a>" : <i>Boolean</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="varsdefinition.md">VarsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowfs" title="AllowFs">AllowFs</a>: <i>Boolean</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="varsdefinition.md">VarsDefinition</a></i>
</pre>

## Properties

#### AllowFs

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

_Required_: No

_Type_: List of <a href="varsdefinition.md">VarsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

