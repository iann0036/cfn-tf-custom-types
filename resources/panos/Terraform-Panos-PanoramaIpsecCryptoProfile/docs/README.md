# Terraform::Panos::PanoramaIpsecCryptoProfile

This resource allows you to add/update/delete Panorama IPSec crypto profiles
for both templates and template stacks.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaIpsecCryptoProfile",
    "Properties" : {
        "<a href="#authentications" title="Authentications">Authentications</a>" : <i>[ String, ... ]</i>,
        "<a href="#dhgroup" title="DhGroup">DhGroup</a>" : <i>String</i>,
        "<a href="#encryptions" title="Encryptions">Encryptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#lifesizetype" title="LifesizeType">LifesizeType</a>" : <i>String</i>,
        "<a href="#lifesizevalue" title="LifesizeValue">LifesizeValue</a>" : <i>Double</i>,
        "<a href="#lifetimetype" title="LifetimeType">LifetimeType</a>" : <i>String</i>,
        "<a href="#lifetimevalue" title="LifetimeValue">LifetimeValue</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaIpsecCryptoProfile
Properties:
    <a href="#authentications" title="Authentications">Authentications</a>: <i>
      - String</i>
    <a href="#dhgroup" title="DhGroup">DhGroup</a>: <i>String</i>
    <a href="#encryptions" title="Encryptions">Encryptions</a>: <i>
      - String</i>
    <a href="#lifesizetype" title="LifesizeType">LifesizeType</a>: <i>String</i>
    <a href="#lifesizevalue" title="LifesizeValue">LifesizeValue</a>: <i>Double</i>
    <a href="#lifetimetype" title="LifetimeType">LifetimeType</a>: <i>String</i>
    <a href="#lifetimevalue" title="LifetimeValue">LifetimeValue</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
</pre>

## Properties

#### Authentications

- List of authentication types.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhGroup

The DH group value.  Valid values should start with
the string `group`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryptions

- List of encryption types.  Valid values
are `des`, `3des`, `aes-128-cbc`, `aes-192-cbc`, `aes-256-cbc`, `aes-128-gcm`,
`aes-256-gcm`, and `null`.  Note that the "gcm" values are only available in
PAN-OS 7.0+.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifesizeType

The lifesize type.  Valid values are `kb`, `mb`,
`gb`, or `tb`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifesizeValue

the lifesize value.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeType

The lifetime type.  Valid values are `seconds`,
`minutes`, `hours` (the default), or `days`.

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

#### Protocol

The protocol.  Valid values are `esp` (the default)
or `ah`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack name.

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

