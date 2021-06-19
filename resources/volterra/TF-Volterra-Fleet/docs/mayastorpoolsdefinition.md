# TF::Volterra::Fleet MayastorPoolsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#node" title="Node">Node</a>" : <i>String</i>,
    "<a href="#pooldiskdevices" title="PoolDiskDevices">PoolDiskDevices</a>" : <i>[ String, ... ]</i>,
    "<a href="#poolname" title="PoolName">PoolName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#node" title="Node">Node</a>: <i>String</i>
<a href="#pooldiskdevices" title="PoolDiskDevices">PoolDiskDevices</a>: <i>
      - String</i>
<a href="#poolname" title="PoolName">PoolName</a>: <i>String</i>
</pre>

## Properties

#### Node

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolDiskDevices

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PoolName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

