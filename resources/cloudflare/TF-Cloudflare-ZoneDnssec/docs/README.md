# TF::Cloudflare::ZoneDnssec

CloudFormation equivalent of cloudflare_zone_dnssec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Cloudflare::ZoneDnssec",
    "Properties" : {
        "<a href="#modifiedon" title="ModifiedOn">ModifiedOn</a>" : <i>String</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Cloudflare::ZoneDnssec
Properties:
    <a href="#modifiedon" title="ModifiedOn">ModifiedOn</a>: <i>String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
</pre>

## Properties

#### ModifiedOn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

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

#### Algorithm

Returns the <code>Algorithm</code> value.

#### Digest

Returns the <code>Digest</code> value.

#### DigestAlgorithm

Returns the <code>DigestAlgorithm</code> value.

#### DigestType

Returns the <code>DigestType</code> value.

#### Ds

Returns the <code>Ds</code> value.

#### Flags

Returns the <code>Flags</code> value.

#### Id

Returns the <code>Id</code> value.

#### KeyTag

Returns the <code>KeyTag</code> value.

#### KeyType

Returns the <code>KeyType</code> value.

#### PublicKey

Returns the <code>PublicKey</code> value.

#### Status

Returns the <code>Status</code> value.

