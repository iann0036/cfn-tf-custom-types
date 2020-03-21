# Terraform::AWS::DlmLifecyclePolicy Schedule CreateRule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#interval" title="Interval">Interval</a>" : <i>Double</i>,
    "<a href="#intervalunit" title="IntervalUnit">IntervalUnit</a>" : <i>String</i>,
    "<a href="#times" title="Times">Times</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#interval" title="Interval">Interval</a>: <i>Double</i>
<a href="#intervalunit" title="IntervalUnit">IntervalUnit</a>: <i>String</i>
<a href="#times" title="Times">Times</a>: <i>
      - String</i>
</pre>

## Properties

#### Interval

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalUnit

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Times

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

