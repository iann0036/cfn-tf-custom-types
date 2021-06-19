# TF::Alkira::ServicePan ZonesToGroupsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
    "<a href="#segmentname" title="SegmentName">SegmentName</a>" : <i>String</i>,
    "<a href="#zonename" title="ZoneName">ZoneName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
<a href="#segmentname" title="SegmentName">SegmentName</a>: <i>String</i>
<a href="#zonename" title="ZoneName">ZoneName</a>: <i>String</i>
</pre>

## Properties

#### Groups

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SegmentName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

