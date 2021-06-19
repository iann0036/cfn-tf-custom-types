# TF::Quorum::BootstrapNetwork

Use this resource to create a new directory that represents a new Quorum network.

Bootstraping data will be kept in this folder.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Quorum::BootstrapNetwork",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#targetdir" title="TargetDir">TargetDir</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Quorum::BootstrapNetwork
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#targetdir" title="TargetDir">TargetDir</a>: <i>String</i>
</pre>

## Properties

#### Name

Name of a new network. Directory name restriction applied
- `target_dir` - (Optional) File system path to the directory on which new directory will be created. Default is current working directory.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetDir

File system path to the directory on which new directory will be created. Default is current working directory.

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

#### Id

Returns the <code>Id</code> value.

#### NetworkDirAbs

Returns the <code>NetworkDirAbs</code> value.

