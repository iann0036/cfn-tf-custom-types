# TF::AWS::CodebuildReportGroup S3DestinationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
    "<a href="#encryptiondisabled" title="EncryptionDisabled">EncryptionDisabled</a>" : <i>Boolean</i>,
    "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>String</i>,
    "<a href="#packaging" title="Packaging">Packaging</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
<a href="#encryptiondisabled" title="EncryptionDisabled">EncryptionDisabled</a>: <i>Boolean</i>
<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>String</i>
<a href="#packaging" title="Packaging">Packaging</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
</pre>

## Properties

#### Bucket

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionDisabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Packaging

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

