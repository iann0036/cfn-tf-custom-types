# TF::AWS::MacieS3BucketAssociation ClassificationTypeDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#continuous" title="Continuous">Continuous</a>" : <i>String</i>,
    "<a href="#onetime" title="OneTime">OneTime</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#continuous" title="Continuous">Continuous</a>: <i>String</i>
<a href="#onetime" title="OneTime">OneTime</a>: <i>String</i>
</pre>

## Properties

#### Continuous

A string value indicating that Macie perform a one-time classification of all of the existing objects in the bucket.
The only valid value is the default value, `FULL`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OneTime

A string value indicating whether or not Macie performs a one-time classification of all of the existing objects in the bucket.
Valid values are `NONE` and `FULL`. Defaults to `NONE` indicating that Macie only classifies objects that are added after the association was created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

