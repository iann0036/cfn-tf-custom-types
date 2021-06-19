# TF::LaunchDarkly::CustomRole PolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#actions" title="Actions">Actions</a>" : <i>[ String, ... ]</i>,
    "<a href="#effect" title="Effect">Effect</a>" : <i>String</i>,
    "<a href="#resources" title="Resources">Resources</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#actions" title="Actions">Actions</a>: <i>
      - String</i>
<a href="#effect" title="Effect">Effect</a>: <i>String</i>
<a href="#resources" title="Resources">Resources</a>: <i>
      - String</i>
</pre>

## Properties

#### Actions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Effect

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resources

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

