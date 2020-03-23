# Terraform::AWS::S3Bucket ReplicationConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    "<a href="#rules" title="Rules">Rules</a>" : <i>[ <a href="replicationconfiguration-rules.md">Rules</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#role" title="Role">Role</a>: <i>String</i>
<a href="#rules" title="Rules">Rules</a>: <i>
      - <a href="replicationconfiguration-rules.md">Rules</a></i>
</pre>

## Properties

#### Role

The ARN of the IAM role for Amazon S3 to assume when replicating the objects.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No

_Type_: List of <a href="replicationconfiguration-rules.md">Rules</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

