# TF::RKE::Cluster SchedulerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ <a href="extraargsdefinition.md">ExtraArgsDefinition</a>, ... ]</i>,
    "<a href="#extrabinds" title="ExtraBinds">ExtraBinds</a>" : <i>[ String, ... ]</i>,
    "<a href="#extraenv" title="ExtraEnv">ExtraEnv</a>" : <i>[ String, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - <a href="extraargsdefinition.md">ExtraArgsDefinition</a></i>
<a href="#extrabinds" title="ExtraBinds">ExtraBinds</a>: <i>
      - String</i>
<a href="#extraenv" title="ExtraEnv">ExtraEnv</a>: <i>
      - String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
</pre>

## Properties

#### ExtraArgs

_Required_: No

_Type_: List of <a href="extraargsdefinition.md">ExtraArgsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraBinds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraEnv

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

