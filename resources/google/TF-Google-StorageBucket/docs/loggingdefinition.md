# TF::Google::StorageBucket LoggingDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#logbucket" title="LogBucket">LogBucket</a>" : <i>String</i>,
    "<a href="#logobjectprefix" title="LogObjectPrefix">LogObjectPrefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#logbucket" title="LogBucket">LogBucket</a>: <i>String</i>
<a href="#logobjectprefix" title="LogObjectPrefix">LogObjectPrefix</a>: <i>String</i>
</pre>

## Properties

#### LogBucket

The bucket that will receive log objects.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogObjectPrefix

The object prefix for log objects. If it's not provided,
by default GCS sets this to this bucket's name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

