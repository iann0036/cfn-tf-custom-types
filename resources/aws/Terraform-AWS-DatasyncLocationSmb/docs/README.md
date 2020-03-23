# Terraform::AWS::DatasyncLocationSmb

Manages a SMB Location within AWS DataSync.

~> **NOTE:** The DataSync Agents must be available before creating this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DatasyncLocationSmb",
    "Properties" : {
        "<a href="#agentarns" title="AgentArns">AgentArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#serverhostname" title="ServerHostname">ServerHostname</a>" : <i>String</i>,
        "<a href="#subdirectory" title="Subdirectory">Subdirectory</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#mountoptions" title="MountOptions">MountOptions</a>" : <i>[ <a href="mountoptions.md">MountOptions</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DatasyncLocationSmb
Properties:
    <a href="#agentarns" title="AgentArns">AgentArns</a>: <i>
      - String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#serverhostname" title="ServerHostname">ServerHostname</a>: <i>String</i>
    <a href="#subdirectory" title="Subdirectory">Subdirectory</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#mountoptions" title="MountOptions">MountOptions</a>: <i>
      - <a href="mountoptions.md">MountOptions</a></i>
</pre>

## Properties

#### AgentArns

A list of DataSync Agent ARNs with which this location will be associated.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The name of the Windows domain the SMB server belongs to.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

The password of the user who can mount the share and has file permissions in the SMB.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerHostname

Specifies the IP address or DNS name of the SMB server. The DataSync Agent(s) use this to mount the SMB share.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subdirectory

Subdirectory to perform actions as source or destination. Should be exported by the NFS server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value pairs of resource tags to assign to the DataSync Location.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The user who can mount the share and has file and folder permissions in the SMB share.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountOptions

_Required_: No

_Type_: List of <a href="mountoptions.md">MountOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uri

Returns the <code>Uri</code> value.

