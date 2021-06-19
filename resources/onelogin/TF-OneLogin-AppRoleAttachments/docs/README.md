# TF::OneLogin::AppRoleAttachments

Manage App Role Attachment resources.

This resource allows you to create and configure App Roles Attachments. The App Role Attachment is not an API-managed resource and is only a means to attach roles to apps in Terraform to avoid complications with circular dependencies.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OneLogin::AppRoleAttachments",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>Double</i>,
        "<a href="#roleid" title="RoleId">RoleId</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OneLogin::AppRoleAttachments
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>Double</i>
    <a href="#roleid" title="RoleId">RoleId</a>: <i>Double</i>
</pre>

## Properties

#### AppId

The id of the App resource to which the role should belong.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleId

The id of the Role being attached to the App.

_Required_: Yes

_Type_: Double

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

