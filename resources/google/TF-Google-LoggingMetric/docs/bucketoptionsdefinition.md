# TF::Google::LoggingMetric BucketOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>" : <i>[ <a href="explicitbucketsdefinition.md">ExplicitBucketsDefinition</a>, ... ]</i>,
    "<a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>" : <i>[ <a href="exponentialbucketsdefinition.md">ExponentialBucketsDefinition</a>, ... ]</i>,
    "<a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>" : <i>[ <a href="linearbucketsdefinition.md">LinearBucketsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>: <i>
      - <a href="explicitbucketsdefinition.md">ExplicitBucketsDefinition</a></i>
<a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>: <i>
      - <a href="exponentialbucketsdefinition.md">ExponentialBucketsDefinition</a></i>
<a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>: <i>
      - <a href="linearbucketsdefinition.md">LinearBucketsDefinition</a></i>
</pre>

## Properties

#### ExplicitBuckets

_Required_: No

_Type_: List of <a href="explicitbucketsdefinition.md">ExplicitBucketsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExponentialBuckets

_Required_: No

_Type_: List of <a href="exponentialbucketsdefinition.md">ExponentialBucketsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinearBuckets

_Required_: No

_Type_: List of <a href="linearbucketsdefinition.md">LinearBucketsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

