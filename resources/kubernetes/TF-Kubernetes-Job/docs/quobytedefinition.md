# TF::Kubernetes::Job QuobyteDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#group" title="Group">Group</a>" : <i>String</i>,
    "<a href="#readonly" title="ReadOnly">ReadOnly</a>" : <i>Boolean</i>,
    "<a href="#registry" title="Registry">Registry</a>" : <i>String</i>,
    "<a href="#user" title="User">User</a>" : <i>String</i>,
    "<a href="#volume" title="Volume">Volume</a>" : <i>[ <a href="volumedefinition.md">VolumeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#group" title="Group">Group</a>: <i>String</i>
<a href="#readonly" title="ReadOnly">ReadOnly</a>: <i>Boolean</i>
<a href="#registry" title="Registry">Registry</a>: <i>String</i>
<a href="#user" title="User">User</a>: <i>String</i>
<a href="#volume" title="Volume">Volume</a>: <i>
      - <a href="volumedefinition.md">VolumeDefinition</a></i>
</pre>

## Properties

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Registry

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Volume

_Required_: Yes

_Type_: List of <a href="volumedefinition.md">VolumeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

