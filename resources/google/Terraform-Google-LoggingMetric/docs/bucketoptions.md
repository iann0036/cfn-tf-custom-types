# Terraform::Google::LoggingMetric BucketOptions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>" : <i>[ <a href="bucketoptions-explicitbuckets.md">ExplicitBuckets</a>, ... ]</i>,
    "<a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>" : <i>[ <a href="bucketoptions-exponentialbuckets.md">ExponentialBuckets</a>, ... ]</i>,
    "<a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>" : <i>[ <a href="bucketoptions-linearbuckets.md">LinearBuckets</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#explicitbuckets" title="ExplicitBuckets">ExplicitBuckets</a>: <i>
      - <a href="bucketoptions-explicitbuckets.md">ExplicitBuckets</a></i>
<a href="#exponentialbuckets" title="ExponentialBuckets">ExponentialBuckets</a>: <i>
      - <a href="bucketoptions-exponentialbuckets.md">ExponentialBuckets</a></i>
<a href="#linearbuckets" title="LinearBuckets">LinearBuckets</a>: <i>
      - <a href="bucketoptions-linearbuckets.md">LinearBuckets</a></i>
</pre>

## Properties

#### ExplicitBuckets

_Required_: No

_Type_: List of <a href="bucketoptions-explicitbuckets.md">ExplicitBuckets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExponentialBuckets

_Required_: No

_Type_: List of <a href="bucketoptions-exponentialbuckets.md">ExponentialBuckets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LinearBuckets

_Required_: No

_Type_: List of <a href="bucketoptions-linearbuckets.md">LinearBuckets</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

