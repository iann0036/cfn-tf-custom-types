# TF::Quorum::BootstrapDataDir

Use this resource to create a data dir locally. This equivalent to execute `geth init`.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Quorum::BootstrapDataDir",
    "Properties" : {
        "<a href="#datadir" title="DataDir">DataDir</a>" : <i>String</i>,
        "<a href="#genesis" title="Genesis">Genesis</a>" : <i>String</i>,
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Quorum::BootstrapDataDir
Properties:
    <a href="#datadir" title="DataDir">DataDir</a>: <i>String</i>
    <a href="#genesis" title="Genesis">Genesis</a>: <i>String</i>
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
</pre>

## Properties

#### DataDir

Directory to intialize a genesis block
- `genesis` - (Required) Genesis file content in JSON format
- `instance_name` - (Optional) The instance name of the node. This must be the same as the value in geth node config. Default is `geth`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Genesis

Genesis file content in JSON format
- `instance_name` - (Optional) The instance name of the node. This must be the same as the value in geth node config. Default is `geth`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceName

The instance name of the node. This must be the same as the value in geth node config. Default is `geth`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DataDirAbs

Returns the <code>DataDirAbs</code> value.

#### Id

Returns the <code>Id</code> value.

