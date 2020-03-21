# Terraform::AWS::AcmpcaCertificateAuthority RevocationConfiguration CrlConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#customcname" title="CustomCname">CustomCname</a>" : <i>String</i>,
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#expirationindays" title="ExpirationInDays">ExpirationInDays</a>" : <i>Double</i>,
    "<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#customcname" title="CustomCname">CustomCname</a>: <i>String</i>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#expirationindays" title="ExpirationInDays">ExpirationInDays</a>: <i>Double</i>
<a href="#s3bucketname" title="S3BucketName">S3BucketName</a>: <i>String</i>
</pre>

## Properties

#### CustomCname

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpirationInDays

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3BucketName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

