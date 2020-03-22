# Terraform::ACME::Registration

The `acme_registration` resource can be used to create and manage accounts on an
ACME server. Once registered, the same private key that has been used for
registration can be used to request authorizations for certificates.

-> This resource is named `acme_registration` for historical reasons - in the
ACME v1 spec, a _registration_ referred to the account entity.  This resource
name is stable and more than likely will not change until a later major version
of the provider, if at all.

-> Keep in mind that when using this resource along with
[`acme_certificate`][resource-acme-certificate] within the same configuration, a
change in the provider-level `server_url` (example: from the Let's Encrypt
staging to production environment) within the same Terraform state will result
in a resource failure, as Terraform will attempt to look for the account in the
wrong CA. Consider different workspaces per environment, and/or using [multiple
provider instances][multiple-provider-instances].

[resource-acme-certificate]: /docs/providers/acme/r/certificate.html
[multiple-provider-instances]: /docs/configuration/providers.html#multiple-provider-instances

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::ACME::Registration",
    "Properties" : {
        "<a href="#accountkeypem" title="AccountKeyPem">AccountKeyPem</a>" : <i>String</i>,
        "<a href="#emailaddress" title="EmailAddress">EmailAddress</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::ACME::Registration
Properties:
    <a href="#accountkeypem" title="AccountKeyPem">AccountKeyPem</a>: <i>String</i>
    <a href="#emailaddress" title="EmailAddress">EmailAddress</a>: <i>String</i>
</pre>

## Properties

#### AccountKeyPem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAddress

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

#### RegistrationUrl

Returns the <code>RegistrationUrl</code> value.

