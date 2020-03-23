# Terraform::AWS::S3Bucket ObjectLockConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#objectlockenabled" title="ObjectLockEnabled">ObjectLockEnabled</a>" : <i>String</i>,
    "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="objectlockconfiguration-rule.md">Rule</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#objectlockenabled" title="ObjectLockEnabled">ObjectLockEnabled</a>: <i>String</i>
<a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="objectlockconfiguration-rule.md">Rule</a></i>
</pre>

## Properties

#### ObjectLockEnabled

Indicates whether this bucket has an Object Lock configuration enabled. Valid value is `Enabled`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="objectlockconfiguration-rule.md">Rule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

