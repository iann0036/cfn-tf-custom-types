# Terraform::AWS::S3Bucket Rules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#destination" title="Destination">Destination</a>" : <i>[ <a href="rules-destination.md">Destination</a>, ... ]</i>,
    "<a href="#filter" title="Filter">Filter</a>" : <i>[ <a href="rules-filter.md">Filter</a>, ... ]</i>,
    "<a href="#sourceselectioncriteria" title="SourceSelectionCriteria">SourceSelectionCriteria</a>" : <i>[ <a href="rules-sourceselectioncriteria.md">SourceSelectionCriteria</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#destination" title="Destination">Destination</a>: <i>
      - <a href="rules-destination.md">Destination</a></i>
<a href="#filter" title="Filter">Filter</a>: <i>
      - <a href="rules-filter.md">Filter</a></i>
<a href="#sourceselectioncriteria" title="SourceSelectionCriteria">SourceSelectionCriteria</a>: <i>
      - <a href="rules-sourceselectioncriteria.md">SourceSelectionCriteria</a></i>
</pre>

## Properties

#### Id

Unique identifier for the rule.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Object keyname prefix identifying one or more objects to which the rule applies.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority associated with the rule.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The status of the rule. Either `Enabled` or `Disabled`. The rule is ignored if status is not Enabled.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Destination

_Required_: No

_Type_: List of <a href="rules-destination.md">Destination</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: No

_Type_: List of <a href="rules-filter.md">Filter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceSelectionCriteria

_Required_: No

_Type_: List of <a href="rules-sourceselectioncriteria.md">SourceSelectionCriteria</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

