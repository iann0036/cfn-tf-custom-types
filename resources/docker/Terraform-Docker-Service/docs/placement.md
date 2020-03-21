# Terraform::Docker::Service Placement

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#constraints" title="Constraints">Constraints</a>" : <i>[ String, ... ]</i>,
    "<a href="#prefs" title="Prefs">Prefs</a>" : <i>[ String, ... ]</i>,
    "<a href="#platforms" title="Platforms">Platforms</a>" : <i>[ <a href="placement-platforms.md">Platforms</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#constraints" title="Constraints">Constraints</a>: <i>
      - String</i>
<a href="#prefs" title="Prefs">Prefs</a>: <i>
      - String</i>
<a href="#platforms" title="Platforms">Platforms</a>: <i>
      - <a href="placement-platforms.md">Platforms</a></i>
</pre>

## Properties

#### Constraints

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefs

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Platforms

_Required_: No
_Type_: List of <a href="placement-platforms.md">Platforms</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

