# TF::Panos::PanoramaNatPolicy TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#serial" title="Serial">Serial</a>" : <i>String</i>,
    "<a href="#vsyslist" title="VsysList">VsysList</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#serial" title="Serial">Serial</a>: <i>String</i>
<a href="#vsyslist" title="VsysList">VsysList</a>: <i>
      - String</i>
</pre>

## Properties

#### Serial

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsysList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
