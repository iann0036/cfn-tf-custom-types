# Terraform::Panos::IkeCryptoProfile

This resource allows you to add/update/delete IKE crypto profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::IkeCryptoProfile",
    "Properties" : {
        "<a href="#authenticationmultiple" title="AuthenticationMultiple">AuthenticationMultiple</a>" : <i>Double</i>,
        "<a href="#authentications" title="Authentications">Authentications</a>" : <i>[ String, ... ]</i>,
        "<a href="#dhgroups" title="DhGroups">DhGroups</a>" : <i>[ String, ... ]</i>,
        "<a href="#encryptions" title="Encryptions">Encryptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#lifetimetype" title="LifetimeType">LifetimeType</a>" : <i>String</i>,
        "<a href="#lifetimevalue" title="LifetimeValue">LifetimeValue</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::IkeCryptoProfile
Properties:
    <a href="#authenticationmultiple" title="AuthenticationMultiple">AuthenticationMultiple</a>: <i>Double</i>
    <a href="#authentications" title="Authentications">Authentications</a>: <i>
      - String</i>
    <a href="#dhgroups" title="DhGroups">DhGroups</a>: <i>
      - String</i>
    <a href="#encryptions" title="Encryptions">Encryptions</a>: <i>
      - String</i>
    <a href="#lifetimetype" title="LifetimeType">LifetimeType</a>: <i>String</i>
    <a href="#lifetimevalue" title="LifetimeValue">LifetimeValue</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### AuthenticationMultiple

IKEv2 SA
reauthentication interval equals authetication-multiple * rekey-lifetime; 0
means reauthentication is disabled.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authentications

List of authentication types.  This c.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhGroups

List of DH Group entries.  Values should
have a prefix if `group`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryptions

List of encryption types.  Valid values
are `des`, `3des`, `aes-128-cbc`, `aes-192-cbc`, and `aes-256-cbc`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeType

The lifetime type.  Valid values are `seconds`,
`minutes`, `hours` (the default), and `days`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeValue

The lifetime value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The object's name.

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

