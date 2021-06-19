# TF::AVI::Role SubresourceDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#excludesubresources" title="ExcludeSubresources">ExcludeSubresources</a>" : <i>Boolean</i>,
    "<a href="#subresources" title="Subresources">Subresources</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#excludesubresources" title="ExcludeSubresources">ExcludeSubresources</a>: <i>Boolean</i>
<a href="#subresources" title="Subresources">Subresources</a>: <i>
      - String</i>
</pre>

## Properties

#### ExcludeSubresources

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subresources

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

