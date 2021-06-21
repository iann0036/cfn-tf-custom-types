# TF::Panos::UserTag

Manages a specific set of tags for a single user.

This resource only manages the given tags for the given user.  Any
other tags associated with the user are left as-is.

**NOTE:** This is for Firewall only.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::UserTag",
    "Properties" : {
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#user" title="User">User</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::UserTag
Properties:
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#user" title="User">User</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
</pre>

## Properties

#### Tags

List of tags.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### User

The user.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys location (default: `vsys1`).

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
