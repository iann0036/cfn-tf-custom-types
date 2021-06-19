# TF::Gitlab::GroupLdapLink

This resource allows you to add an LDAP link to an existing GitLab group.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Gitlab::GroupLdapLink",
    "Properties" : {
        "<a href="#accesslevel" title="AccessLevel">AccessLevel</a>" : <i>String</i>,
        "<a href="#cn" title="Cn">Cn</a>" : <i>String</i>,
        "<a href="#force" title="Force">Force</a>" : <i>Boolean</i>,
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#ldapprovider" title="LdapProvider">LdapProvider</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Gitlab::GroupLdapLink
Properties:
    <a href="#accesslevel" title="AccessLevel">AccessLevel</a>: <i>String</i>
    <a href="#cn" title="Cn">Cn</a>: <i>String</i>
    <a href="#force" title="Force">Force</a>: <i>Boolean</i>
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#ldapprovider" title="LdapProvider">LdapProvider</a>: <i>String</i>
</pre>

## Properties

#### AccessLevel

Acceptable values are: guest, reporter, developer, maintainer, owner.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cn

The CN of the LDAP group to link with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Force

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupId

The id of the GitLab group.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LdapProvider

The name of the LDAP provider as stored in the GitLab database.

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

