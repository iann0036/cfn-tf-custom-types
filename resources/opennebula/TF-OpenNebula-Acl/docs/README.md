# TF::OpenNebula::Acl

Provides an OpenNebula ACL resource.

This resource allows you to manage ACLs on your OpenNebula clusters. When applied,
a new ACL is created. When destroyed, this ACL is removed. Note that ACLs currently cannot be changed, hence they are deleted and re-created upon change.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OpenNebula::Acl",
    "Properties" : {
        "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
        "<a href="#rights" title="Rights">Rights</a>" : <i>String</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OpenNebula::Acl
Properties:
    <a href="#resource" title="Resource">Resource</a>: <i>String</i>
    <a href="#rights" title="Rights">Rights</a>: <i>String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
</pre>

## Properties

#### Resource

Resource component of the new rule. Any combination of valid resources, separated by a `+`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rights

Rights component of the new rule. Any combination of valid Rights, separated by a `+`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

User component of the new rule.
- `#<id>` matches a single user id
- `@<id>` matches a group id
- `*` matches everything.

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

