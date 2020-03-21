# Terraform::Panos::IpsecCryptoProfile

CloudFormation equivalent of panos_ipsec_crypto_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::IpsecCryptoProfile",
    "Properties" : {
        "<a href="#authentications" title="Authentications">Authentications</a>" : <i>[ String, ... ]</i>,
        "<a href="#dhgroup" title="DhGroup">DhGroup</a>" : <i>String</i>,
        "<a href="#encryptions" title="Encryptions">Encryptions</a>" : <i>[ String, ... ]</i>,
        "<a href="#lifesizetype" title="LifesizeType">LifesizeType</a>" : <i>String</i>,
        "<a href="#lifesizevalue" title="LifesizeValue">LifesizeValue</a>" : <i>Double</i>,
        "<a href="#lifetimetype" title="LifetimeType">LifetimeType</a>" : <i>String</i>,
        "<a href="#lifetimevalue" title="LifetimeValue">LifetimeValue</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::IpsecCryptoProfile
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
</pre>

## Properties

#### Authentications

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DhGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryptions

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifesizeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifesizeValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeValue

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

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

