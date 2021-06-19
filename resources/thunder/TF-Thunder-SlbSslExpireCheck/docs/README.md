# TF::Thunder::SlbSslExpireCheck

`thunder_slb_ssl_expire_check` Provides details about thunder slb ssl expire check

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbSslExpireCheck",
    "Properties" : {
        "<a href="#before" title="Before">Before</a>" : <i>Double</i>,
        "<a href="#expireaddress1" title="ExpireAddress1">ExpireAddress1</a>" : <i>String</i>,
        "<a href="#intervaldays" title="IntervalDays">IntervalDays</a>" : <i>Double</i>,
        "<a href="#sslexpireemailaddress" title="SslExpireEmailAddress">SslExpireEmailAddress</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#exception" title="Exception">Exception</a>" : <i>[ <a href="exceptiondefinition.md">ExceptionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbSslExpireCheck
Properties:
    <a href="#before" title="Before">Before</a>: <i>Double</i>
    <a href="#expireaddress1" title="ExpireAddress1">ExpireAddress1</a>: <i>String</i>
    <a href="#intervaldays" title="IntervalDays">IntervalDays</a>: <i>Double</i>
    <a href="#sslexpireemailaddress" title="SslExpireEmailAddress">SslExpireEmailAddress</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#exception" title="Exception">Exception</a>: <i>
      - <a href="exceptiondefinition.md">ExceptionDefinition</a></i>
</pre>

## Properties

#### Before

The number of days in advance notice before expiration, default is 5.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpireAddress1

Email address for certificate expiration check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IntervalDays

The interval of days notice after expiration, default is 2.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslExpireEmailAddress

Config Email address for certificate expiration check.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Exception

_Required_: No

_Type_: List of <a href="exceptiondefinition.md">ExceptionDefinition</a>

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

