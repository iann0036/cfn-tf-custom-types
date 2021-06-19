# TF::GoogleBeta::GoogleCloudRunService SecretDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#secretname" title="SecretName">SecretName</a>" : <i>String</i>,
    "<a href="#items" title="Items">Items</a>" : <i>[ <a href="itemsdefinition.md">ItemsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#secretname" title="SecretName">SecretName</a>: <i>String</i>
<a href="#items" title="Items">Items</a>: <i>
      - <a href="itemsdefinition.md">ItemsDefinition</a></i>
</pre>

## Properties

#### SecretName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Items

_Required_: No

_Type_: List of <a href="itemsdefinition.md">ItemsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

