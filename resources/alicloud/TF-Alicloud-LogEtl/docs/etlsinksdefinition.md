# TF::Alicloud::LogEtl EtlSinksDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>" : <i>String</i>,
    "<a href="#accesskeysecret" title="AccessKeySecret">AccessKeySecret</a>" : <i>String</i>,
    "<a href="#endpoint" title="Endpoint">Endpoint</a>" : <i>String</i>,
    "<a href="#kmsencryptedaccesskeyid" title="KmsEncryptedAccessKeyId">KmsEncryptedAccessKeyId</a>" : <i>String</i>,
    "<a href="#kmsencryptedaccesskeysecret" title="KmsEncryptedAccessKeySecret">KmsEncryptedAccessKeySecret</a>" : <i>String</i>,
    "<a href="#logstore" title="Logstore">Logstore</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#project" title="Project">Project</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesskeyid" title="AccessKeyId">AccessKeyId</a>: <i>String</i>
<a href="#accesskeysecret" title="AccessKeySecret">AccessKeySecret</a>: <i>String</i>
<a href="#endpoint" title="Endpoint">Endpoint</a>: <i>String</i>
<a href="#kmsencryptedaccesskeyid" title="KmsEncryptedAccessKeyId">KmsEncryptedAccessKeyId</a>: <i>String</i>
<a href="#kmsencryptedaccesskeysecret" title="KmsEncryptedAccessKeySecret">KmsEncryptedAccessKeySecret</a>: <i>String</i>
<a href="#logstore" title="Logstore">Logstore</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#project" title="Project">Project</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### AccessKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccessKeySecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Endpoint

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedAccessKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsEncryptedAccessKeySecret

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logstore

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

