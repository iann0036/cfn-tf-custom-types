# Terraform::Google::LoggingMetric

CloudFormation equivalent of google_logging_metric

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::LoggingMetric",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
        "<a href="#labelextractors" title="LabelExtractors">LabelExtractors</a>" : <i>[ <a href="labelextractors.md">LabelExtractors</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#valueextractor" title="ValueExtractor">ValueExtractor</a>" : <i>String</i>,
        "<a href="#bucketoptions" title="BucketOptions">BucketOptions</a>" : <i>[ <a href="bucketoptions.md">BucketOptions</a>, ... ]</i>,
        "<a href="#metricdescriptor" title="MetricDescriptor">MetricDescriptor</a>" : <i>[ <a href="metricdescriptor.md">MetricDescriptor</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>" : <i>[ <a href="explicitbuckets.md">ExplicitBuckets</a>, ... ]</i>,
        "<a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>" : <i>[ <a href="exponentialbuckets.md">ExponentialBuckets</a>, ... ]</i>,
        "<a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>" : <i>[ <a href="linearbuckets.md">LinearBuckets</a>, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labels.md">Labels</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::LoggingMetric
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>String</i>
    <a href="#labelextractors" title="LabelExtractors">LabelExtractors</a>: <i>
      - <a href="labelextractors.md">LabelExtractors</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#valueextractor" title="ValueExtractor">ValueExtractor</a>: <i>String</i>
    <a href="#bucketoptions" title="BucketOptions">BucketOptions</a>: <i>
      - <a href="bucketoptions.md">BucketOptions</a></i>
    <a href="#metricdescriptor" title="MetricDescriptor">MetricDescriptor</a>: <i>
      - <a href="metricdescriptor.md">MetricDescriptor</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>: <i>
      - <a href="explicitbuckets.md">ExplicitBuckets</a></i>
    <a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>: <i>
      - <a href="exponentialbuckets.md">ExponentialBuckets</a></i>
    <a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>: <i>
      - <a href="linearbuckets.md">LinearBuckets</a></i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labels.md">Labels</a></i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelExtractors

_Required_: No

_Type_: List of <a href="labelextractors.md">LabelExtractors</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValueExtractor

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BucketOptions

_Required_: No

_Type_: List of <a href="bucketoptions.md">BucketOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricDescriptor

_Required_: No

_Type_: List of <a href="metricdescriptor.md">MetricDescriptor</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExplicitBuckets

_Required_: No

_Type_: List of <a href="explicitbuckets.md">ExplicitBuckets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExponentialBuckets

_Required_: No

_Type_: List of <a href="exponentialbuckets.md">ExponentialBuckets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinearBuckets

_Required_: No

_Type_: List of <a href="linearbuckets.md">LinearBuckets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

