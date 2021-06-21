# TF::AWS::GlueCrawler S3TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
    "<a href="#exclusions" title="Exclusions">Exclusions</a>" : <i>[ String, ... ]</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
<a href="#exclusions" title="Exclusions">Exclusions</a>: <i>
      - String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### ConnectionName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exclusions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
