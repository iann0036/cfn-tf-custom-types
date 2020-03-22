# Terraform::Cloudflare::CustomSsl

Provides a Cloudflare custom ssl resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cloudflare::CustomSsl",
    "Properties" : {
        "<a href="#customssloptions" title="CustomSslOptions">CustomSslOptions</a>" : <i>[ <a href="customssloptions.md">CustomSslOptions</a>, ... ]</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#customsslpriority" title="CustomSslPriority">CustomSslPriority</a>" : <i>[ <a href="customsslpriority.md">CustomSslPriority</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cloudflare::CustomSsl
Properties:
    <a href="#customssloptions" title="CustomSslOptions">CustomSslOptions</a>: <i>
      - <a href="customssloptions.md">CustomSslOptions</a></i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#customsslpriority" title="CustomSslPriority">CustomSslPriority</a>: <i>
      - <a href="customsslpriority.md">CustomSslPriority</a></i>
</pre>

## Properties

#### CustomSslOptions

The certificate, private key and associated optional parameters, such as bundle_method, geo_restrictions, and type.

_Required_: No

_Type_: List of <a href="customssloptions.md">CustomSslOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone id to the custom ssl cert should be added.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSslPriority

_Required_: No

_Type_: List of <a href="customsslpriority.md">CustomSslPriority</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ExpiresOn

Returns the <code>ExpiresOn</code> value.

#### Hosts

Returns the <code>Hosts</code> value.

#### Id

Returns the <code>Id</code> value.

#### Issuer

Returns the <code>Issuer</code> value.

#### ModifiedOn

Returns the <code>ModifiedOn</code> value.

#### Priority

Returns the <code>Priority</code> value.

#### Signature

Returns the <code>Signature</code> value.

#### Status

Returns the <code>Status</code> value.

#### UploadedOn

Returns the <code>UploadedOn</code> value.

