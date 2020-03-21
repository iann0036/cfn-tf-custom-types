# Terraform::FlexibleEngine::DdsInstanceV3 Datastore

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#storageengine" title="StorageEngine">StorageEngine</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#storageengine" title="StorageEngine">StorageEngine</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### StorageEngine

Specifies the storage engine of the DB instance. Only wiredTiger is supported now.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Specifies the DB engine. Only DDS-Community is supported now.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

Specifies the DB instance version. Only 3.4 is supported now.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

