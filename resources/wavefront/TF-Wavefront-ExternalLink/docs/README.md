# TF::Wavefront::ExternalLink

CloudFormation equivalent of wavefront_external_link

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Wavefront::ExternalLink",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#islogintegration" title="IsLogIntegration">IsLogIntegration</a>" : <i>Boolean</i>,
        "<a href="#metricfilterregex" title="MetricFilterRegex">MetricFilterRegex</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pointtagfilterregexes" title="PointTagFilterRegexes">PointTagFilterRegexes</a>" : <i>[ <a href="pointtagfilterregexesdefinition.md">PointTagFilterRegexesDefinition</a>, ... ]</i>,
        "<a href="#sourcefilterregex" title="SourceFilterRegex">SourceFilterRegex</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Wavefront::ExternalLink
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#islogintegration" title="IsLogIntegration">IsLogIntegration</a>: <i>Boolean</i>
    <a href="#metricfilterregex" title="MetricFilterRegex">MetricFilterRegex</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pointtagfilterregexes" title="PointTagFilterRegexes">PointTagFilterRegexes</a>: <i>
      - <a href="pointtagfilterregexesdefinition.md">PointTagFilterRegexesDefinition</a></i>
    <a href="#sourcefilterregex" title="SourceFilterRegex">SourceFilterRegex</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
</pre>

## Properties

#### Description

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsLogIntegration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricFilterRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PointTagFilterRegexes

_Required_: No

_Type_: List of <a href="pointtagfilterregexesdefinition.md">PointTagFilterRegexesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceFilterRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

