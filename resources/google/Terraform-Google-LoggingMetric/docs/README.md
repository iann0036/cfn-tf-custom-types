# Terraform::Google::LoggingMetric

Logs-based metric can also be used to extract values from logs and create a a distribution
of the values. The distribution records the statistics of the extracted values along with
an optional histogram of the values as specified by the bucket options.


To get more information about Metric, see:

* [API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/logging/docs/apis)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=logging_metric_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

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

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

