# Terraform::AWS::CodebuildProject LogsConfig S3Logs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#encryptiondisabled" title="EncryptionDisabled">EncryptionDisabled</a>" : <i>Boolean</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#encryptiondisabled" title="EncryptionDisabled">EncryptionDisabled</a>: <i>Boolean</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### EncryptionDisabled

Set to `true` if you do not want S3 logs encrypted. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

The name of the S3 bucket and the path prefix for S3 logs. Must be set if status is `ENABLED`, otherwise it must be empty.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Current status of logs in S3 for a build project. Valid values: `ENABLED`, `DISABLED`. Defaults to `DISABLED`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

