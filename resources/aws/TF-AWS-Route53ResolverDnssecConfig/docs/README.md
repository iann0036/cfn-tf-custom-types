# TF::AWS::Route53ResolverDnssecConfig

Provides a Route 53 Resolver DNSSEC config resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Route53ResolverDnssecConfig",
    "Properties" : {
        "<a href="#resourceid" title="ResourceId">ResourceId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Route53ResolverDnssecConfig
Properties:
    <a href="#resourceid" title="ResourceId">ResourceId</a>: <i>String</i>
</pre>

## Properties

#### ResourceId

The ID of the virtual private cloud (VPC) that you're updating the DNSSEC validation status for.

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

#### OwnerId

Returns the <code>OwnerId</code> value.

#### ValidationStatus

Returns the <code>ValidationStatus</code> value.

