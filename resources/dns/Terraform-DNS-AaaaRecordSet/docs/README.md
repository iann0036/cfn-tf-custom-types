# Terraform::DNS::AaaaRecordSet

Creates a AAAA type DNS record set.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::DNS::AaaaRecordSet",
    "Properties" : {
        "<a href="#addresses" title="Addresses">Addresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>,
        "<a href="#zone" title="Zone">Zone</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::DNS::AaaaRecordSet
Properties:
    <a href="#addresses" title="Addresses">Addresses</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
    <a href="#zone" title="Zone">Zone</a>: <i>String</i>
</pre>

## Properties

#### Addresses

The IPv6 addresses this record set will point to.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the record set. The `zone` argument will be appended to this value to create the full record path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

The TTL of the record set. Defaults to `3600`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zone

DNS zone the record set belongs to. It must be an FQDN, that is, include the trailing dot.

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

