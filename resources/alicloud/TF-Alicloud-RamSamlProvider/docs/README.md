# TF::Alicloud::RamSamlProvider

CloudFormation equivalent of alicloud_ram_saml_provider

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::RamSamlProvider",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encodedsamlmetadatadocument" title="EncodedsamlMetadataDocument">EncodedsamlMetadataDocument</a>" : <i>String</i>,
        "<a href="#samlprovidername" title="SamlProviderName">SamlProviderName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::RamSamlProvider
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encodedsamlmetadatadocument" title="EncodedsamlMetadataDocument">EncodedsamlMetadataDocument</a>: <i>String</i>
    <a href="#samlprovidername" title="SamlProviderName">SamlProviderName</a>: <i>String</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncodedsamlMetadataDocument

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SamlProviderName

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### UpdateDate

Returns the <code>UpdateDate</code> value.

