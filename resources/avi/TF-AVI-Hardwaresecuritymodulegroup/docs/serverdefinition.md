# TF::AVI::Hardwaresecuritymodulegroup ServerDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#partitionpasswd" title="PartitionPasswd">PartitionPasswd</a>" : <i>String</i>,
    "<a href="#partitionserialnumber" title="PartitionSerialNumber">PartitionSerialNumber</a>" : <i>String</i>,
    "<a href="#remoteip" title="RemoteIp">RemoteIp</a>" : <i>[ <a href="remoteipdefinition.md">RemoteIpDefinition</a>, ... ]</i>,
    "<a href="#servercert" title="ServerCert">ServerCert</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#partitionpasswd" title="PartitionPasswd">PartitionPasswd</a>: <i>String</i>
<a href="#partitionserialnumber" title="PartitionSerialNumber">PartitionSerialNumber</a>: <i>String</i>
<a href="#remoteip" title="RemoteIp">RemoteIp</a>: <i>
      - <a href="remoteipdefinition.md">RemoteIpDefinition</a></i>
<a href="#servercert" title="ServerCert">ServerCert</a>: <i>String</i>
</pre>

## Properties

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionPasswd

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionSerialNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteIp

_Required_: Yes

_Type_: List of <a href="remoteipdefinition.md">RemoteIpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCert

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

