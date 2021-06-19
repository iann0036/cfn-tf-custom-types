# TF::Turbot::Grant

The `Turbot Grant` resource adds support for grants in Turbot. Turbot grant presents a cleaner and more explicit separation of duties on how users are managed in Turbot.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::Grant",
    "Properties" : {
        "<a href="#identity" title="Identity">Identity</a>" : <i>String</i>,
        "<a href="#level" title="Level">Level</a>" : <i>String</i>,
        "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::Grant
Properties:
    <a href="#identity" title="Identity">Identity</a>: <i>String</i>
    <a href="#level" title="Level">Level</a>: <i>String</i>
    <a href="#resource" title="Resource">Resource</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Identity

The profile for which the permissions are being granted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Level

The permission level to be granted. This is the `aka` of a permission level resource.
- `identity` - (Required) The profile for which the permissions are being granted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resource

The id or `aka` of the resource for which permissions are being granted.
- `type` - (Required) The type of permissions being granted. This is the `aka` of a permission type resource.
- `level` - (Required) The permission level to be granted. This is the `aka` of a permission level resource.
- `identity` - (Required) The profile for which the permissions are being granted.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of permissions being granted. This is the `aka` of a permission type resource.
- `level` - (Required) The permission level to be granted. This is the `aka` of a permission level resource.
- `identity` - (Required) The profile for which the permissions are being granted.

_Required_: Yes

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

#### IdentityAkas

Returns the <code>IdentityAkas</code> value.

#### PermissionLevelAkas

Returns the <code>PermissionLevelAkas</code> value.

#### PermissionTypeAkas

Returns the <code>PermissionTypeAkas</code> value.

#### ResourceAkas

Returns the <code>ResourceAkas</code> value.

