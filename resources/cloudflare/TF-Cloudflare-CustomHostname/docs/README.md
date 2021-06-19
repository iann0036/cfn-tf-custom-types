# TF::Cloudflare::CustomHostname

Provides a Cloudflare custom hostname (also known as SSL for SaaS) resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::CustomHostname",
    "Properties" : {
        "<a href="#customoriginserver" title="CustomOriginServer">CustomOriginServer</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#ssl" title="Ssl">Ssl</a>" : <i>[ <a href="ssldefinition.md">SslDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::CustomHostname
Properties:
    <a href="#customoriginserver" title="CustomOriginServer">CustomOriginServer</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#ssl" title="Ssl">Ssl</a>: <i>
      - <a href="ssldefinition.md">SslDefinition</a></i>
</pre>

## Properties

#### CustomOriginServer

The custom origin server used for certificates.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

Hostname you intend to request a certificate for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The DNS zone ID where the custom hostname should be assigned.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ssl

_Required_: No

_Type_: List of <a href="ssldefinition.md">SslDefinition</a>

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

#### OwnershipVerification

Returns the <code>OwnershipVerification</code> value.

#### OwnershipVerificationHttp

Returns the <code>OwnershipVerificationHttp</code> value.

#### Status

Returns the <code>Status</code> value.

