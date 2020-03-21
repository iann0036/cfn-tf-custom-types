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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#labelextractors" title="LabelExtractors">LabelExtractors</a>" : <i>[ &lt;a href=&#34;labelextractors.md&#34;&gt;LabelExtractors&lt;/a&gt;, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#valueextractor" title="ValueExtractor">ValueExtractor</a>" : <i>String</i>,
        "<a href="#bucketoptions" title="BucketOptions">BucketOptions</a>" : <i>[ &lt;a href=&#34;bucketoptions.md&#34;&gt;BucketOptions&lt;/a&gt;, ... ]</i>,
        "<a href="#metricdescriptor" title="MetricDescriptor">MetricDescriptor</a>" : <i>[ &lt;a href=&#34;metricdescriptor.md&#34;&gt;MetricDescriptor&lt;/a&gt;, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>,
        "<a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>" : <i>[ &lt;a href=&#34;explicitbuckets.md&#34;&gt;ExplicitBuckets&lt;/a&gt;, ... ]</i>,
        "<a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>" : <i>[ &lt;a href=&#34;exponentialbuckets.md&#34;&gt;ExponentialBuckets&lt;/a&gt;, ... ]</i>,
        "<a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>" : <i>[ &lt;a href=&#34;linearbuckets.md&#34;&gt;LinearBuckets&lt;/a&gt;, ... ]</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::LoggingMetric
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#labelextractors" title="LabelExtractors">LabelExtractors</a>: <i>
      - &lt;a href=&#34;labelextractors.md&#34;&gt;LabelExtractors&lt;/a&gt;</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#valueextractor" title="ValueExtractor">ValueExtractor</a>: <i>String</i>
    <a href="#bucketoptions" title="BucketOptions">BucketOptions</a>: <i>
      - &lt;a href=&#34;bucketoptions.md&#34;&gt;BucketOptions&lt;/a&gt;</i>
    <a href="#metricdescriptor" title="MetricDescriptor">MetricDescriptor</a>: <i>
      - &lt;a href=&#34;metricdescriptor.md&#34;&gt;MetricDescriptor&lt;/a&gt;</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    <a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>: <i>
      - &lt;a href=&#34;explicitbuckets.md&#34;&gt;ExplicitBuckets&lt;/a&gt;</i>
    <a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>: <i>
      - &lt;a href=&#34;exponentialbuckets.md&#34;&gt;ExponentialBuckets&lt;/a&gt;</i>
    <a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>: <i>
      - &lt;a href=&#34;linearbuckets.md&#34;&gt;LinearBuckets&lt;/a&gt;</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
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

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelExtractors

_Required_: No

_Type_: List of &lt;a href=&#34;labelextractors.md&#34;&gt;LabelExtractors&lt;/a&gt;

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

_Type_: List of &lt;a href=&#34;bucketoptions.md&#34;&gt;BucketOptions&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MetricDescriptor

_Required_: No

_Type_: List of &lt;a href=&#34;metricdescriptor.md&#34;&gt;MetricDescriptor&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExplicitBuckets

_Required_: No

_Type_: List of &lt;a href=&#34;explicitbuckets.md&#34;&gt;ExplicitBuckets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExponentialBuckets

_Required_: No

_Type_: List of &lt;a href=&#34;exponentialbuckets.md&#34;&gt;ExponentialBuckets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinearBuckets

_Required_: No

_Type_: List of &lt;a href=&#34;linearbuckets.md&#34;&gt;LinearBuckets&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

