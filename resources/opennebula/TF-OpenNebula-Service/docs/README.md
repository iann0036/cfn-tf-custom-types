# TF::OpenNebula::Service

Provides an OpenNebula service resource.

This resource allows you to manage services on your OpenNebula clusters. When applied,
a new service will be created. When destroyed, that service will be removed.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::Service",
    "Properties" : {
        "<a href="#extratemplate" title="ExtraTemplate">ExtraTemplate</a>" : <i>String</i>,
        "<a href="#gid" title="Gid">Gid</a>" : <i>Double</i>,
        "<a href="#gname" title="Gname">Gname</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
        "<a href="#templateid" title="TemplateId">TemplateId</a>" : <i>Double</i>,
        "<a href="#uid" title="Uid">Uid</a>" : <i>Double</i>,
        "<a href="#uname" title="Uname">Uname</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::Service
Properties:
    <a href="#extratemplate" title="ExtraTemplate">ExtraTemplate</a>: <i>String</i>
    <a href="#gid" title="Gid">Gid</a>: <i>Double</i>
    <a href="#gname" title="Gname">Gname</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
    <a href="#templateid" title="TemplateId">TemplateId</a>: <i>Double</i>
    <a href="#uid" title="Uid">Uid</a>: <i>Double</i>
    <a href="#uname" title="Uname">Uname</a>: <i>String</i>
</pre>

## Properties

#### ExtraTemplate

Service information to be merged with the template during instantiate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gid

Set the id of the group owner of the newly created service. The corresponding `gname` will be computed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gname

Set the name of the group owner of the newly created service. The corresponding `gid` will be computed.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Permissions applied on service. Defaults to the UMASK in OpenNebula (in UNIX Format: owner-group-other => Use-Manage-Admin).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateId

Service will be instantiated from the template ID.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uid

Set the id of the user owner of the newly created service. The corresponding `uname` will be computed.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uname

Set the name of the user owner of the newly created service. The corresponding `uid` will be computed.

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

#### Networks

Returns the <code>Networks</code> value.

#### Roles

Returns the <code>Roles</code> value.

#### State

Returns the <code>State</code> value.

