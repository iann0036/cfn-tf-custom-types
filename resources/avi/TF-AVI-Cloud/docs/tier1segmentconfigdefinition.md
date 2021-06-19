# TF::AVI::Cloud Tier1SegmentConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#segmentconfigmode" title="SegmentConfigMode">SegmentConfigMode</a>" : <i>String</i>,
    "<a href="#automatic" title="Automatic">Automatic</a>" : <i>[ <a href="automaticdefinition.md">AutomaticDefinition</a>, ... ]</i>,
    "<a href="#manual" title="Manual">Manual</a>" : <i>[ <a href="manualdefinition.md">ManualDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#segmentconfigmode" title="SegmentConfigMode">SegmentConfigMode</a>: <i>String</i>
<a href="#automatic" title="Automatic">Automatic</a>: <i>
      - <a href="automaticdefinition.md">AutomaticDefinition</a></i>
<a href="#manual" title="Manual">Manual</a>: <i>
      - <a href="manualdefinition.md">ManualDefinition</a></i>
</pre>

## Properties

#### SegmentConfigMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Automatic

_Required_: No

_Type_: List of <a href="automaticdefinition.md">AutomaticDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manual

_Required_: No

_Type_: List of <a href="manualdefinition.md">ManualDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

