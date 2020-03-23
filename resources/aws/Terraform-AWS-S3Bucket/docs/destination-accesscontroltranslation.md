# Terraform::AWS::S3Bucket Destination AccessControlTranslation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#owner" title="Owner">Owner</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#owner" title="Owner">Owner</a>: <i>String</i>
</pre>

## Properties

#### Owner

The override value for the owner on replicated objects. Currently only `Destination` is supported.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

